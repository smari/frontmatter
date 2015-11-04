#!/usr/bin/python
"""
Frontmatter tools for YAML-enhanced Markdown Metadata.
"""
import click
import yaml

def parse_file(src):
    lines = []
    if not src.readline() == "---\n":
        raise Exception('Not a valid Markdown+YAML file.')
    while True:
        line = src.readline()
        if line == "---\n":
            break
        lines.append(line)
    metadata = yaml.load("".join(lines))
    markdown = src.read()
    return metadata, markdown

def write_file(dst, metadata, markdown):
    fh = open(dst, "w")
    fh.write("---\n")
    fh.write(yaml.dump(metadata, allow_unicode=True))
    fh.write("---\n")
    fh.write(markdown)

@click.command()
@click.argument('src', type=click.File('r'))
@click.argument('key', type=click.STRING)
def get(src, key):
    """
    Get a key's value from Markdown frontmatter
    """
    meta, md = parse_file(src)
    if key in meta:
        print meta[key]
    else:
        print "Key '%s' is not defined" % key

@click.command()
@click.argument('src', type=click.File('rb'))
@click.argument('key', type=click.STRING)
@click.argument('value', type=click.STRING)
@click.option('-d', '--destination', default='<same>')
def set(src, key, value, destination):
    """
    Set a key's value in Markdown frontmatter.
    """
    if destination == '<same>':
        destination = src.name
    meta, md = parse_file(src)
    meta[key.encode('utf-8')] = value.encode('utf-8')
    write_file(destination, meta, md)

@click.group()
def cli():
    pass

cli.add_command(set)
cli.add_command(get)

if __name__=="__main__":
    cli()
