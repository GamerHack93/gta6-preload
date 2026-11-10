#!/usr/bin/env python3
"""Checks that all LFS objects listed in build_manifest.json are present."""
import json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m = json.load(open(os.path.join(ROOT, "build_manifest.json"), encoding="utf-8"))
missing = 0
for f in m["files"]:
    p = os.path.join(ROOT, f["path"])
    if not os.path.exists(p):
        print("MISSING", f["path"]); missing += 1
print("{} files checked, {} missing".format(len(m["files"]), missing))
sys.exit(1 if missing else 0)
