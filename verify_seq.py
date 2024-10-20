#!/usr/bin/env python3

import json
import os
import re

from mathics.session import MathicsSession
import stopit

session = MathicsSession()


def run_mathics(prog, expected, reset=True):
    if reset:
        try:
            session.evaluate_as_in_cli('Clear["Global`*"]', timeout=3)
        except:
            session.reset()

    print(f"> {prog}")

    try:
        with stopit.ThreadingTimeout(3.5) as to_ctx_mgr:
            result = session.evaluate_as_in_cli(prog, timeout=3)
            # print(result.get_data())
            result = result.get_data()["result"]
        if not to_ctx_mgr:
            print("Timeout")
            # session.reset()
            return "TIMEOUT"
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print("Error:", e)
        return "ERROR"

    if result is None:
        return "EMPTY"

    try:
        result = json.loads(result.replace("{", "[").replace("}", "]"))
    except:
        print("Unable to parse result:", result)
        return "PARSE"

    if type(result) is int:
        print("Integer result:", result)
        return "INT"

    if type(result) is not list:
        print("Invalid result type:", result)
        return "BADTYPE"

    if check(expected, result):
        return "OK"
    else:
        return "FAIL"


def check(expected, result):
    if expected == result:
        return True
    if type(result) is not list:
        return False
    for i in range(3):
        num_terms = min(len(result), len(expected[i:]))
        if num_terms > 7 and result[:num_terms] == expected[i:][:num_terms]:
            return True
    if len(result) > 1:
        print(f"Unable to match {result} to {expected}")
    return False


def check_expression(expr, expected):
    code = run_mathics(expr, expected)
    if code == "OK":
        return True

    if code == "EMPTY" and "Global`a" in session.definitions.get_user_names():
        code = run_mathics("a[10]", expected, reset=False)
        if code == "OK":
            return True

        if code == "INT":
            code = run_mathics("Array[a,10]", expected, reset=False)
            if code == "OK":
                return True

    return False


total = 0
passed = 0


def extract_programs(content):
    global total, passed
    terms = []
    lines = content.split("\n")
    for line in lines:
        if line.startswith("%N"):
            name = re.sub(r"^%N A\d+ ?", "", line)
        if line.startswith("%S") or line.startswith("%T") or line.startswith("%U"):
            terms += [
                int(term.strip())
                for term in re.sub(r"^%[STU] A\d+ ?", "", line).split(",")
                if term.strip() != ""
            ]
        if line.startswith("%t"):
            code_line = re.sub(r"^%[pto] A\d+ ?", "", line)
            total += 1
            if check_expression(code_line, terms):
                passed += 1
                print("OK")
            else:
                print("FAIL")
            print(f"***** {passed}/{total} ({100*passed/total:.2f}%) *****")


def process_file(input_filepath):
    # Extract sequence ID from the filepath
    sequence_id = os.path.splitext(os.path.basename(input_filepath))[0]
    print(sequence_id)

    # Read the file content
    with open(input_filepath, "r") as f:
        content = f.read()

    # Extract programs (this function remains unchanged)
    extract_programs(content)


def main():
    input_dir = "seq"

    for root, dirs, files in sorted(os.walk(input_dir)):
        for file in sorted(files):
            if file.endswith(".seq"):
                input_filepath = os.path.join(root, file)
                process_file(input_filepath)


if __name__ == "__main__":
    main()

# Kill threads
os._exit(0)
