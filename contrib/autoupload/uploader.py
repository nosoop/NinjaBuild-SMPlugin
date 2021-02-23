#!/usr/bin/python3

# daemon to detect modified build outputs and send them to your development machine
# because windows doesn't have a good rsync client (without buying into the MSYS2 ecosystem),
# otherwise I'd have modd fill this purpose :(

# run from root project as `python path/to/uploader.py build/`

import os
import sys
import time
import logging
from watchdog.observers import Observer
import watchdog.events
import pathlib
import string
import shlex
import signal

import subprocess

import configparser

def is_subpath_of(src_path, parent_path):
	abs_src_path = src_path.resolve()
	abs_parent_path = parent_path.resolve()
	if len(src_path.parts) < len(parent_path.parts):
		return False
	return all(s == p for s, p in zip(abs_src_path.parts, abs_parent_path.parts))

class UploadingEventHandler(watchdog.events.FileSystemEventHandler):
	def __init__(self, config, rootdir):
		super().__init__()
		self.config = config
		self.rootdir = pathlib.Path(rootdir)
		
		# sort paths in descending order to ensure longer paths take priority
		self.path_mapping_keys = sorted(config['path_mappings'].keys(), key = pathlib.Path, reverse = True)
		
		# write to stderr; modd doesn't record stdout
		print(f"Monitoring paths within '{self.rootdir}':", self.path_mapping_keys, file = sys.stderr)
	
	def on_modified(self, event):
		'''
		Uploads files that have been modified.
		'''
		super().on_modified(event)
		
		# path is relative to working dir, since we need the full path
		src = pathlib.Path(event.src_path)
		
		if not src.is_file():
			# only process files
			return
		
		if not any(is_subpath_of(src, self.rootdir / pathlib.Path(p)) for p in self.path_mapping_keys):
			# ignoring non-mapped path
			return
		
		# dest is relative to our monitored root
		dest = src.relative_to(self.rootdir)
		
		for mapped_path in self.path_mapping_keys:
			if is_subpath_of(dest, pathlib.Path(mapped_path)):
				dest_path = pathlib.Path(config.get('path_mappings', mapped_path))
				dest = dest_path / dest.relative_to(mapped_path)
				break
		
		upload_command = string.Template(self.config.get("uploader", "command"))
		command_args = shlex.split(upload_command.substitute({'in': src, 'out': dest}))
		
		print('>>', shlex.join(command_args), file = sys.stderr)
		proc = subprocess.run(command_args)
		print(f'Process exited with code {proc.returncode}', file = sys.stderr)

if __name__ == "__main__":
	path = sys.argv[1] if len(sys.argv) > 1 else '.'
	
	config = configparser.ConfigParser()
	config.read('uploader.ini')
	
	event_handler = UploadingEventHandler(config = config, rootdir = path)
	observer = Observer()
	observer.schedule(event_handler, path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	finally:
		observer.stop()
		observer.join()
