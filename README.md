# Ninja Project Template for SourceMod Plugins

A project repository template that builds SourceMod plugins with [Ninja][].

## Template Setup

1. [Use this template][] to create a new repository, then clone the resulting repository
locally.
    - If this is your first time with the template, read over the instructions provided in
    `BUILD.md`.  The template is configured to build an example plugin immediately, so you'll
    want to succeed at that before you start modifying.
    - If you have an existing repository, you may want to instead copy `configure.py` and
    `misc/`, as well as create / update your `.gitignore` to exclude generated outputs
    (see this repository's version).
2. Configure the project for your specific needs.
    - Create script(s) in the `scripting/` directory.
    - Add script(s) to the `plugins` list in the `configure.py` file.
    Only scripts compiled directly should be added (that is, don't add `#include`d `.sp` files).
    - Add file paths that you want to copy to the build output (gamedata, configs, include,
    non-base scripts) to the `copy_files` list.
    - To add third-party includes, copy them into the project in some directory, then add that
    path to the `include_dirs` list in `configure.py`.
    - Look over the rest of `configure.py` and modify settings to your liking.
    - If you need to stray from the existing build instructions, note any changes under the
    building section.
3. Edit this README for your project.
    - Remove this template setup section.
    - Make sure to point readers to the project's `BUILD.md`, as they may not be familiar with
    how to build the project.
    - An example section you can preserve is provided below, though you're not required to
    follow it exactly.

[Use this template]: https://github.com/nosoop/NinjaBuild-SMPlugin/generate

----

## Building

This project is configured for building via [Ninja][]; see `BUILD.md` for detailed
instructions on how to build it.

If you'd like to use the build system for your own projects,
[the template is available here](https://github.com/nosoop/NinjaBuild-SMPlugin).

[Ninja]: https://ninja-build.org/