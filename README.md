# prettierd format

Plugin for [Sublime Text](https://www.sublimetext.com/) to format files faster using [prettierd](https://github.com/fsouza/prettierd).

<br />

## Installation

1. Install [prettierd](https://github.com/fsouza/prettierd) globally using npm/yarn/pnpm:

```sh
npm i -g prettierd
```

2. Install this plugin via [Package Control](https://packagecontrol.io/packages/Prettierd%20Formatter) or manually.

<br />

## Usage

By default it formats any file natively supported by [Prettier](https://prettier.io/docs/en/) on save.

### Commands

To format a file via command palette:

- `Prettierd: Format this file`

To save a file without formatting:

- `Prettierd: Save without formatting`

### Options

Enable/disable formatting on save:

```json
"format_on_save": true
```

Exclude specific extensions from being formatted on save:

```json
"disabled_extensions": ["md"]
```

Exclude specific directories from being formatted on save:

```json
"disabled_directories": ["node_modules"]
```

Add additional file types to be formatted on save (enabled via plugins):

```json
"additional_extensions": ["php"]
```

<br />

## Notes

This plugin does nothing else than piping the file contents to `prettierd` and replacing the file contents with the output.

It is basically the equivalent of running `cat file.js | prettierd file.s` with the command line.

For this reason, any issue with plugins or additional prettier configuration should be reported to the [prettierd](https://github.com/fsouza/prettierd) as it is the one doing the actual formatting.

### Astro / Svelte

For Astro and Svelte files, you should not use this package but simply format using `LSP: format` command.
