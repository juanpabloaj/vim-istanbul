#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import vim
import os


def load_json_content(file_dir):
    coverage_path = os.path.join(file_dir, 'coverage/coverage.json')
    with open(coverage_path) as json_file:
        return json.loads(json_file.read())


def sign_covered_lines():
    file_path = vim.eval("escape(expand('%:p'), '\')")
    bufname = vim.eval("escape(bufname('%'), '\')")
    current_dir = vim.eval('getcwd()')
    buffernr = vim.eval("bufnr('%')")

    json_content = load_json_content(current_dir)
    for path, field in json_content.items():
        if path == file_path:

            statementMap = field['statementMap']
            for i, st in statementMap.items():
                start, end = [ st[s]['line'] for s in ['start', 'end']]
                if field['s'][i] < 1:
                    name = 'uncovered'
                else:
                    name = 'covered'

                sign_place = "sign place {} line={} name={} buffer={}"\
                    .format(start, start, name, buffernr)
                vim.command(sign_place)

            fn_map = field['fnMap']
            for i,fn in fn_map.items():
                line = fn['line']
                sign_place = "sign place {} line={} name=fstatno buffer={}"\
                    .format(i, line, buffernr)
                #vim.command(sign_place)
