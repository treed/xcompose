#!/usr/bin/env python

# Purpose: parse an XCompose file and output as equivalent JSON.
# Very hacky one-time script!

inf = open("dotXCompose", "r")
lines = inf.read().splitlines()

def decomment(l):
  outline = ""
  for c in l:
    if c == "#":
      return outline
    else:
      outline += c
  return outline

for i in range(len(lines)):
    lines[i] = decomment(lines[i]).strip()

relevant = []
for l in lines:
  if l != "":
    relevant.append(l)


import re


def parseKeyb(s):
    s = s.strip()
    keys = []
    for k in re.finditer(r"\<([^\<\>]+)\>", s):
        keys.append(k.group(1))
    if keys[0] != "Multi_key":
        print "Things are fucked up!"
        exit
    else:
        keys = keys[1:]
    return keys


def pqs(s):
    if s[0] == "\"":
        return ""
    elif s[0] == '\\' and s[1] == "\"":
        return "\"" + pqs(s[2:])
    else:
        return s[0] + pqs(s[1:])


def parseChar(s):
    s = s.strip()
    return pqs(s[1:]) # remove first quote

outj = {}

def add(keyb, char, to):
    if len(keyb) == 1:
        to[keyb[0]] = char
    else:
        if not keyb[0] in to:
            to[keyb[0]] = {}
        add(keyb[1:], char, to[keyb[0]])
        

for l in relevant:
  a = l.split(":", 1)
  keyb = parseKeyb(a[0])
  char = parseChar(a[1])
  add(keyb, char, outj)

import codecs

outf = codecs.open("converted.txt", "w")

import json
json.dump(outj, outf, ensure_ascii = False, sort_keys = True, indent=2)
