#!/usr/bin/env python3

import os
import json

from mathics.session import MathicsSession

session = MathicsSession()

def verify(file_path, content):
    file_path = os.path.join("verified", file_path)
    print("Writing to", file_path)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(content)

for root, dirs, files in sorted(os.walk("prog/Mathematica")):
    for file in sorted(files):
        prog_path = os.path.join(root, file)
        prog = open(prog_path).read()
        json_path = os.path.join(
            "prog/JSON",
            os.path.relpath(root, "prog/Mathematica"),
            file[:7] + ".json",
        )
        seq = json.load(open(json_path))

        print(f"Testing {prog_path}...")
        print(prog)
        try:
            result = session.evaluate_as_in_cli(prog, timeout=5).get_data()[
                "result"
            ]
        except KeyboardInterrupt:
            raise
        except:
            result = None
        if result is None:
            print("EMPTY")
            continue

        try:
            result = json.loads(result.replace("{", "[").replace("}", "]"))
        except:
            print("Unable to parse result:", result)
            continue

        if result == seq:
            print("PASS")
            verify(prog_path, prog)
            continue

        num_terms = min(len(result), len(seq))
        if num_terms > 10 and result[:num_terms] == seq[:num_terms]:
            print("PREFIX")
            verify(prog_path, prog)
            continue

        print("DIFF:")
        print("RESULT:", result)
        try:
            session.evaluate_as_in_cli('Clear["Global`*"]', timeout=3)
        except:
            session.reset()
        print("EXPECTED:", seq)
        print()
