# Ninja Project for SourceMod Plugins

A project repository template that builds SourceMod plugins with [Ninja][].

[Ninja]: https://ninja-build.org/

## Setup

1. [Use this template][] to create a new repository.
	- If you have an existing repository, you may want to instead copy `configure.py` and
	`misc/ninja_syntax.py`, as well as create / update your `.gitignore` to exclude generated
	outputs (see this repository's version).
2. Set up a project.
	- Create script(s) in the `scripting/` directory.
	- Add script(s) to the `plugins` list in the `configure.py` file.
	Only the base script should be added (that is, don't add `#include`d `.sp` files)
	- Add gamedata / configs / include file paths to the `copy_files` list.
	- Update / remove this `README` file!
4. Run `python configure.py --spcomp-dir {DIR}` within the project root, where `{DIR}` is a
directory containing the SourcePawn compiler (`spcomp`) and SourceMod's base include files.
If `--spcomp-dir` isn't specified, the script will try to detect the compiler from your path.
5. Run `ninja`.  Files will be generated and copied to `build/`, creating any intermediate
folders if they don't exist.  Re-run `ninja` whenever you make changes; it will also reconfigure
the build if `configure.py` is modified.

[Use this template]: https://github.com/nosoop/NinjaBuild-SMPlugin/generate
