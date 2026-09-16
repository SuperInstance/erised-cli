#!/usr/bin/env python3
"""yq.py — convert simple YAML scenarios to JSON. No pyyaml dep."""
import sys, json, re

def simple_yaml(text):
    """Tiny YAML parser for our scenario template format."""
    out = {}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s or s.startswith("#"):
            i += 1; continue
        if ":" not in line:
            i += 1; continue
        key, val = line.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val == "|":
            # block scalar
            i += 1
            block = []
            while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
                if lines[i].strip(): block.append(lines[i].strip())
                i += 1
            out[key] = "\n".join(block)
        elif val == "" and i + 1 < len(lines) and lines[i+1].lstrip().startswith("- "):
            # list
            i += 1
            lst = []
            while i < len(lines) and lines[i].lstrip().startswith("- "):
                item = lines[i].lstrip()[2:]
                if ":" in item and "{" not in item:
                    k, v = item.split(":", 1)
                    lst.append({k.strip(): parse_value(v.strip())})
                else:
                    lst.append(item)
                i += 1
            out[key] = lst
        else:
            out[key] = parse_value(val)
            i += 1
    return out

def parse_value(v):
    if v.startswith('"') and v.endswith('"'):
        return v[1:-1]
    if v.lower() in ("true","false"): return v.lower() == "true"
    try: return int(v)
    except: pass
    try: return float(v)
    except: pass
    return v

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: yq.py file.yaml > file.json")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        d = simple_yaml(f.read())
    print(json.dumps(d, indent=2))
