#!/usr/bin/env python3

import os
import fileinput



stat_dir=os.path.join("dist", "static", "index.html")
dist_dir=os.path.join("dist", "index.html")
try:
  os.rename(stat_dir, dist_dir)
except FileNotFoundError:
  print("Already move")


with fileinput.FileInput(dist_dir, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace('src="', 'src="static/'), end='')

