#!/usr/bin/env python

from json import loads
import pipes
import subprocess
import vim

text = vim.eval("join(getline(1,'$'), '\n')")
cmd = "sourcekitten --syntax-text %s" % pipes.quote(text)
# cmd = "sourcekitten --syntax %s" % vim.eval("expand('%:p')")
output = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          shell=True).stdout.read()
json = loads(output)

types = {
    "source.lang.swift.syntaxtype.attribute.builtin": "Function",
    "source.lang.swift.syntaxtype.comment": "Comment",
    "source.lang.swift.syntaxtype.comment.url": "SpecialComment",
    "source.lang.swift.syntaxtype.identifier": "Identifier",
    "source.lang.swift.syntaxtype.keyword": "Keyword",
    "source.lang.swift.syntaxtype.number": "Number",
    "source.lang.swift.syntaxtype.string": "String",
    "source.lang.swift.syntaxtype.typeidentifier": "Type",
}

vim.eval("clearmatches()")
vim.command("normal! mi")
for j in json:
    offset = j["offset"]
    length = j["length"]
    color = types.get(j["type"], None)
    if color is None:
        continue
    cmd = ":goto %d" % (offset + 1)
    vim.command(cmd)
    line = int(vim.eval("line('.')"))
    col = int(vim.eval("col('.')"))
    cmd = "call matchaddpos('%s', [[%d, %d, %d]])" % (color, line, col, length)
    vim.command(cmd)

vim.command("normal! `i")
