# Ninja Project Template for SourceMod Plugins

A project repository template that builds SourceMod plugins with [Ninja][].

[Ninja]: https://ninja-build.org/

## Setup

Make sure to read over and download the things specified in the [Prerequisites][] page.

1. [Use this template][] to create a new repository, then clone the resulting repository
locally.
	- If this is your first time with the template, verify that the prerequisites have been
	successfully installed by following the building instructions; the project is configured by
	default to compile `scripting/sample_plugin.sp` to `build/plugins/sample_plugin.smx`.
	- If you have an existing repository, you may want to instead copy `configure.py` and
	`misc/`, as well as create / update your `.gitignore` to exclude generated outputs
	(see this repository's version).
2. Configure the project for your needs.
	- Create script(s) in the `scripting/` directory.
	- Add script(s) to the `plugins` list in the `configure.py` file.
	Only scripts compiled directly should be added (that is, don't add `#include`d `.sp` files).
	- Add file paths that you want to copy to the build output (gamedata, configs, include,
	non-base scripts) to the `copy_files` list.
	- Look over the rest of `configure.py` and modify settings to your liking.
	- Update / remove this `README` file!  You'll want to provide building steps similar to the
	ones below.

[Prerequisites]: https://github.com/nosoop/NinjaBuild-SMPlugin/wiki/Prerequisites
[Use this template]: https://github.com/nosoop/NinjaBuild-SMPlugin/generate

## Building

1. Run `python configure.py --spcomp-dir {DIR}` within the project root, where `{DIR}` is a
directory containing the SourcePawn compiler (`spcomp`) and SourceMod's base include files.
This will create the `build.ninja` script.
	- If `--spcomp-dir` isn't specified, the script will try to detect the compiler based on an
	existing `spcomp` executable in your path.
	- It is highly preferred that you use a toolchain that is free of third-party include
	files; those files should be added to the project directly.
	- Do not add `build.ninja` to version control; it should always be generated from
	`configure.py`.
2. Run `ninja`; this will read the `build.ninja` script and build things as necessary.  Files
will be generated and copied to `build/`, creating any intermediate folders if they don't exist.
Re-run `ninja` whenever you make changes; it will also reconfigure the build if `configure.py`
is modified.
	- Any files removed from `configure.py` will remain in `build/`; run `ninja -t cleandead`
	to remove any lingering files.
