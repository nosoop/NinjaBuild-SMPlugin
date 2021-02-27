# Github Action

This directory contains a Github action that, by default, will create a release for a pushed tag
`v*` with a package containing the `{configs,scripting,plugins,gamedata}/` outputs from the
build.

## Configuration

1.  Copy `build.yml` to `.github/workflows/`.
2.  Modify to suit your needs.
