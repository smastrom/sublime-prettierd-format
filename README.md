# Prettierd Format

Sublime Text plugin to finally format files fast using [prettierd](https://github.com/fsouza/prettierd).

<br />

## Installation

1. Install [prettierd](https://github.com/fsouza/prettierd) globally using npm/yarn/pnpm:

```sh
npm i -g prettierd
```

2. Install this plugin using [Package Control](https://packagecontrol.io/packages/Prettierd%20Formatter):

`Package Control: Install Package` → `Prettierd Format`

3. Restart Sublime Text

<br />

## Usage

By default it formats on save any file natively supported by [Prettier](https://prettier.io/docs/en/).

### Commands

To format a file via command palette:

- `Prettierd: Format`

To save a file without formatting:

- `Prettierd: Save without formatting`

### Options

Enable/disable formatting on save:

```json
"format_on_save": true
```

Add additional file types (added via plugins) to be formatted either on save or via command palette:

```json
"additional_extensions": ["php"]
```

Exclude extensions from being formatted on save:

```json
"disabled_extensions_on_save": ["md"]
```

Exclude directories from being formatted on save:

```json
"disabled_directories_on_save": ["*/node_modules/*"]
```

<br />

## Notes

This plugin does nothing else than piping the input to `prettierd` and replacing the file contents with the output.

It is basically just like executing `cat file.js | prettierd file.js` with the command line.

For this reason, any issue with plugins or additional prettier configuration should be reported to the [prettierd](https://github.com/fsouza/prettierd) as it is the one doing the actual formatting.

### Astro / Svelte

As of September 2023, there are some upstream issues with Astro and Svelte files.

However, you can format them using `LSP: format` after installing the relevant language server which seems to respect the `.prettierrc` file.

<br />

## License

0BSD
