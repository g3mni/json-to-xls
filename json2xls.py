#!/usr/bin/env python
# encoding: utf-8
# 数据格式需形如：[{"a":1,"b":"leo"},{"a":2,"b":"alice"}....]
# 使用方式 python json2xls.py json_name.txt new_xls_name.xls
import json
import tablib
import sys

filename = sys.argv[1]
xlsname = sys.argv[2]

with open(filename, 'r') as f:
    rows = json.load(f)

header = tuple([i for i in rows[0].keys()])
data = []
for row in rows:
    body = []
    for v in row.values():
        body.append(v)
    data.append(tuple(body))

data = tablib.Dataset(*data, headers=header)

open(xlsname, 'wb').write(data.xls)
