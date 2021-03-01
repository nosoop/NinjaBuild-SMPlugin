# Github Workflow

This directory contains a Github workflow that, by default, will create a release for a pushed
tag `v*` with a package containing the `{configs,scripting,plugins,gamedata}/` outputs from the
build.

## Configuration

1.  Copy the desired `build-*.yml` to `.github/workflows/`.  You may rename it if desired.
2.  Modify to suit your needs.
