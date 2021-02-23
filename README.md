# Ninja Project Template for SourceMod Plugins

A project repository template that builds SourceMod plugins with [Ninja][].

[Ninja]: https://ninja-build.org/

## Setup

1. [Use this template][] to create a new repository.
	- If you have an existing repository, you may want to instead copy `configure.py` and
	`misc/`, as well as create / update your `.gitignore` to exclude generated outputs
	(see this repository's version).
2. Set up a project.
	- Create script(s) in the `scripting/` directory.
	- Add script(s) to the `plugins` list in the `configure.py` file.
	Only the base script should be added (that is, don't add `#include`d `.sp` files)
	- Add file paths that you want to copy to the build output (gamedata, configs, include,
	non-base scripts) to the `copy_files` list.
	- Look over the rest of `configure.py` and modify settings to your liking.
	- Update / remove this `README` file!  You'll want to provide building steps similar to the
	ones below.

## Building

1. Run `python configure.py --spcomp-dir {DIR}` within the project root, where `{DIR}` is a
directory containing the SourcePawn compiler (`spcomp`) and SourceMod's base include files.
This will create the `build.ninja` script.
	- If `--spcomp-dir` isn't specified, the script will try to detect the compiler based on an
	existing `spcomp` executable in your path.
	- It is highly recommended that you use a toolchain that is free of third-party include
	files; those files should be added to the project directly.
	- Do not add `build.ninja` to version control; it should always be generated from
	`configure.py`.
2. Run `ninja`.  Files will be generated and copied to `build/`, creating any intermediate
folders if they don't exist.  Re-run `ninja` whenever you make changes; it will also reconfigure
the build if `configure.py` is modified.

[Use this template]: https://github.com/nosoop/NinjaBuild-SMPlugin/generate
