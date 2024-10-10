#!/usr/bin/env python3

import re
import os
from collections import defaultdict


def extract_programs(content):
    programs = defaultdict(list)
    current_lang = None
    current_program = []

    lines = content.split("\n")
    for line in lines:
        if "See Links" in line:
            continue
        line = line.replace("(Small Basic)", "(SmallBasic)")
        line = line.replace("(Scheme:)", "(Scheme)")
        line = line.replace("(MIT Scheme:)", "(Scheme)")
        line = re.sub(r"\(Scheme, [^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(MIT/GNU Scheme, [^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(Scheme functions [^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(Scheme with [^()]+\)", "(Scheme)", line)
        line = line.replace("(C#)", "(Csharp)")
        line = line.replace("(C++)", "(Cpp)")
        line = line.replace("(GNU bc)", "(bc)")
        line = line.replace("  (PARI)", " (PARI)")
        line = line.replace("）", ")")
        line = line.replace("(GW-BASIC)", "(GWBASIC)")
        line = line.replace("(MIT/GNU Scheme)", "(Scheme)")
        line = line.replace("(APL (NARS200 dialect))", "(APL)")
        line = line.replace("(Python3)", "(Python)")
        line = line.replace("(Python 3.x)", "(Python)")
        line = line.replace("(Python 3.10+)", "(Python)")
        line = line.replace("(Python 2.7)", "(Python)")
        line = line.replace("(SageMath)", "(Sage)")
        line = line.replace("(PFGW and SCRIPTIFY)", "(PFGW)")
        line = line.replace("(PFGW & SCRIPTIFY)", "(PFGW)")
        line = line.replace("#!/usr/bin/perl", "(Perl)")
        if line.startswith("%p"):
            code_line = re.sub(r"^%[pto] A\d+ ?", "", line)
            programs["Maple"].append(code_line)
        if line.startswith("%t"):
            code_line = re.sub(r"^%[pto] A\d+ ?", "", line)
            programs["Mathematica"].append(code_line)
        if line.startswith("%o"):
            code_line = re.sub(r"^%[pto] A\d+ ?", "", line)
            lang_tag_match = re.match(r"\((\w+)\)", code_line)
            if lang_tag_match:
                if current_program:
                    programs[current_lang].append("\n".join(current_program).strip())
                    current_program = []
                current_lang = lang_tag_match.group(1)
                code_line = re.sub(r"^\(\w+\)\s*", "", code_line)
            if current_lang:
                current_program.append(code_line)
            else:
                print(f"No language tag found: {line}")
                current_program = []

    if current_lang and current_program:
        programs[current_lang].append("\n".join(current_program).strip())

    return programs


def write_programs(programs, sequence_id):
    for lang, code_blocks in programs.items():
        for i, code in enumerate(code_blocks):
            lang_ext = get_language_extension(lang)
            if lang_ext is None:
                print(f"Unrecognised language: {lang}")
                lang_ext = "txt"

            # Create the output directory structure
            output_dir = os.path.join("prog", lang, sequence_id[:4])
            os.makedirs(output_dir, exist_ok=True)

            # Create the output filename
            filename = (
                f"{sequence_id}{chr(97 + i) if len(code_blocks) > 1 else ''}.{lang_ext}"
            )
            output_filepath = os.path.join(output_dir, filename)

            # Write the program to the file
            with open(output_filepath, "w") as f:
                f.write(code)


def get_language_extension(lang):
    extensions = {
        "Maple": "mpl",
        "Mathematica": "wl",
        "Axiom": "ax",
        "Magma": "m",
        "Maxima": "mac",
        "Macsyma": "mac",
        "PARI": "gp",
        "Python": "py",
        "Sage": "py",
        "Haskell": "hs",
        "Julia": "jl",
        "GAP": "g",
        "Scala": "scala",
        "Fortran": "f",
        "Scheme": "scm",
        "IntSeq": "scm",
        "SLIB": "scm",
        "MATLAB": "m",
        "JavaScript": "js",
        "SmallBasic": "bas",
        "Perl": "pl",
        "UBASIC": "bas",
        "BASIC": "bas",
        "GWBASIC": "bas",
        "JBASIC": "bas",
        "Java": "java",
        "C": "c",
        "ARIBAS": "ari",
        "R": "r",
        "Ruby": "rb",
        "Go": "go",
        "Clojure": "clj",
        "Csharp": "cs",
        "Cpp": "cpp",
        "bc": "bc",
        "Smalltalk": "st",
        "Prolog": "pl",
        "MiniZinc": "mzn",
        "Sidef": "sf",
        "APL": "apl",
        "PHP": "php",
        "Racket": "rkt",
        "Rust": "rs",
        "J": "j",
        "Delphi": "pas",
    }
    return extensions.get(lang)


def process_file(input_filepath):
    # Extract sequence ID from the filepath
    sequence_id = os.path.splitext(os.path.basename(input_filepath))[0]
    # print(sequence_id)

    # Read the file content
    with open(input_filepath, "r") as f:
        content = f.read()

    # Extract programs (this function remains unchanged)
    programs = extract_programs(content)

    # Write programs to appropriate directories
    write_programs(programs, sequence_id)


def main():
    input_dir = "seq"

    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".seq"):
                input_filepath = os.path.join(root, file)
                process_file(input_filepath)


if __name__ == "__main__":
    main()
