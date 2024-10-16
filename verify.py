#!/usr/bin/env python3

from contextlib import redirect_stdout
from io import StringIO
import json
import os
import re
import sys

from mathics.session import MathicsSession

session = MathicsSession()


def run_mathics(prog, reset=True):
    if reset:
        try:
            session.evaluate_as_in_cli('Clear["Global`*"]', timeout=3)
        except:
            session.reset()

    # print(f"> {prog}")

    try:
        result = session.evaluate_as_in_cli(prog, timeout=5)
        # print(result.get_data())
        result = result.get_data()["result"]
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print("Error:", e)
        return None

    if result is None:
        return None

    try:
        result = json.loads(result.replace("{", "[").replace("}", "]"))
    except:
        print("Unable to parse result:", result)
        return None

    if type(result) is not list:
        print("Invalid result type:", result)
        return None

    return result


def run_python(prog):
    try:
        f = StringIO()
        with redirect_stdout(f):
            exec(prog, {})
        result = f.getvalue()
        result = result.strip()
    except Exception as e:
        print("Error:", e)
        return None

    if result == "":
        return None

    if result[-1] == ",":
        result = f"[{result[:-1]}]"

    try:
        result = json.loads(result)
    except:
        print("Unable to parse result:", result)
        return None

    return result


def check(expected, result):
    if expected == result:
        return True
    if type(result) is not list:
        return False
    num_terms = min(len(result), len(expected))
    for i in range(3):
        if num_terms > 8 and result[:num_terms] == expected[i:num_terms+i]:
            return True
    if num_terms > 1:
        print(f"Unable to match {result} to {expected}")
    return False


def process_markdown_file(input_file):
    expected = None
    sequence_id = os.path.splitext(os.path.basename(input_file))[0]

    with open(input_file, "r") as f:
        content = f.read()

    # Regular expression to match code blocks
    pattern = r"```(\w+)\n(.*?)```"

    def replace_code_block(match):
        nonlocal expected
        language = match.group(1)
        code = match.group(2)

        # Call the rewrite function on the code content
        if language == "JSON":
            expected = json.loads(code)

        if language == "Mathematica":
            print(language, end="... ")
            if check(expected, run_mathics(code)):
                print("OK")
            elif check(expected, run_mathics("a[30]", reset=False)):
                print("List")
            elif check(expected, run_mathics("Array[a, 30]", reset=False)):
                print("Array")
            else:
                print("FAIL")

        """
        if language == "Python":
            print(language, end="... ")
            if check(expected, run_python(code)):
                print("OK")
            elif check(expected, run_python(f"{code}\nprint([a(n) for n in range(30)])")):
                print("range 0")
            elif check(expected, run_python(f"{code}\nprint([a(n) for n in range(1, 31)])")):
                print("range 1")
            elif check(expected, run_python(f"{code}\nprint([{sequence_id}(n) for n in range(30)])")):
                print("range 0")
            elif check(expected, run_python(f"{code}\nprint([{sequence_id}(n) for n in range(1, 31)])")):
                print("range 1")
            elif check(expected, run_python(f"{code}\nprint({sequence_id})")):
                print(f"{sequence_id}")
            elif check(expected, run_python(f"{code}\nprint({sequence_id}_list)")):
                print(f"{sequence_id}_list")
            else:
                print("FAIL")
        """

        # Reconstruct the code block
        return f"```{language}\n{code}```"

    # Replace all code blocks in the content
    processed_content = re.sub(pattern, replace_code_block, content, flags=re.DOTALL)

    # Write the processed content to the output file
    # with open(input_file, "w") as f:
    #     f.write(processed_content)


# Usage
input_file = sys.argv[1]
process_markdown_file(input_file)

# Kill threads
os._exit(0)
