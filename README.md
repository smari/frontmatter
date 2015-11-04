# Frontmatter

This is a simple Python tool that allows people to get/set Markdown+YAML
frontmatter from the command line.

## Usage

To get a value from a file:
```bash
$ frontmatter get file.md key
```
(Gets value of 'key')

To set a value in a file:
```bash
$ frontmatter set file.md key value
``` 
(Sets 'key' to 'value')

## Caveats

Currently doesn't know how to 'set' lists or dicts, only first-level scalars.

## Author

 * Smári McCarthy <smari@smarimccarthy.is>

