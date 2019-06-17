#!/usr/bin/python3
import sys
import re

def read(name):
    with open(name) as f:
        return f.read()

def parseParam(propertyStr):
    param = {}
    for line in propertyStr.strip().split("\n"):
        pattern = line.strip().split(":")
        param[pattern[0]]=eval(pattern[1])
    return param

def calcTemp(template, param):
    fomulas = []
    for codeBlock in re.findall(r"\{.+?\}", template):
        value = str(eval(codeBlock[1:-1], param))
        template = template.replace(codeBlock, value)
    return template

template = read(sys.argv[1])
paramStr = read(sys.argv[2])
params = parseParam(paramStr)
results = calcTemp(template, params)


print(results)
