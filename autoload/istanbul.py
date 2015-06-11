#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import vim
import os


def load_json_content(file_dir):
    coverage_path = os.path.join(file_dir, g_coverage_json_path)
    with open(coverage_path) as json_file:
        return json.loads(json_file.read())

def check_file(file_path, path):
    return os.path.abspath(path) == file_path

def sign_covered_lines():
    file_path = vim.eval("escape(expand('%:p'), '\')")
    bufname = vim.eval("escape(bufname('%'), '\')")
    current_dir = vim.eval('getcwd()')
    buffernr = vim.eval("bufnr('%')")

    json_content = load_json_content(current_dir)
    for path, field in json_content.items():
        if check_file(file_path, path):
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

            branchMap = field['branchMap']
            for i, br in branchMap.items():
                line = br['line']
                if field['b'][i][0] < 1 and field['b'][i][1] > 0:
                    sign_place = "sign place {} line={} name={} buffer={}"\
                        .format(line, line, 'branch_true', buffernr)
                    vim.command(sign_place)
                if field['b'][i][1] < 1 and field['b'][i][0] > 0:
                    sign_place = "sign place {} line={} name={} buffer={}"\
                        .format(line, line, 'branch_false', buffernr)
                    vim.command(sign_place)

            fn_map = field['fnMap']
            for i,fn in fn_map.items():
                line = fn['line']
                sign_place = "sign place {} line={} name=fstatno buffer={}"\
                    .format(i, line, buffernr)
                #vim.command(sign_place)
