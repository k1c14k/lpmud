#!/usr/bin/env python3
import sys
import os

if len(sys.argv) < 3:
    print("Usage: genfkntab.py PREFIX FNAME", file=sys.stderr)
    sys.exit(1)

prefix = sys.argv[1]
fname = sys.argv[2]

prefix_upper = prefix.upper()
header_name = f"{fname}.h"
data_name = f"{fname}.t"

with open(header_name, "w") as header_file, open(data_name, "w") as data_file:
    data_file.write(f"static struct fkntab {fname}_fkntab[] =\n{{\n")
    func_index = 0
    for line in sys.stdin:
        func_name = line.strip()
        if not func_name or func_name.startswith("#"):
            continue
        # Write to header file
        header_file.write(f"#define {prefix_upper}_{func_name.upper()} {func_index}\n")
        func_index += 1
        # Write to data file
        data_file.write(f"    {{ \"{func_name}\", 0, 0 }},\n")
    data_file.write("    { NULL, 0, 0 }\n")
    data_file.write("};\n")

