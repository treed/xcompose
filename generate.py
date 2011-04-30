#!/usr/bin/env python

import json
import codecs
import unicodedata

def repeat(s, n):
  o = ""
  for i in range(n):
    o += s
  return o

def pad(s, l):
  return s + repeat(" ", l - len(s))

def unicharcode(v):
    return hex(ord(v))[2:].upper()

def nameof(c):
    try:
        return unicodedata.name(c)
    except ValueError:
        return "unknown unicode name"

def generate(js, prev):
    s = ""
    for k in js:
        keybinding = prev + "<" + k + "> "
        v = js[k]
        if type(v) is dict:
            s += generate(js[k], keybinding)
        else:
            if type(v) is not unicode:
                print "Error: value of type " + str(type(v)) + ".\n"
                exit
            s += pad(keybinding + ": ", 40)
            if len(v) == 1:
                s += "\"" + v + "\"    U" + unicharcode(v) + "    # " + nameof(v) + "\n"
            else:
                s += "\"" + v + "\"            # (multiple character binding)\n"
    return s



inf = open("converted.txt", "r")
inj = json.load(inf)

outs = generate(inj, "<Multi_key> ")

outf = codecs.open("dotXCompose.txt", "w","utf-8")

outf.write(outs)

