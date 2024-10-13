#!/usr/bin/env python3

import re
import os
from collections import defaultdict
import yaml

languages = yaml.safe_load(open("languages.yml"))


def extract_programs(content):
    programs = defaultdict(list)
    terms = []
    current_lang = None
    current_program = []

    programs["JSON"]

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
        if "See Links" in line or "See link" in line or ": (Start)" in line:
            continue
        line = line.replace("(UBASIC)", "(BASIC)")
        line = line.replace("(Small Basic)", "(BASIC)")
        line = line.replace("(Visual Basic)", "(VBA)")
        line = line.replace("(Visual Basic for Excel)", "(VBA)")
        line = line.replace("(VBA/Excel)", "(VBA)")
        line = line.replace("(VBA for Excel)", "(VBA)")
        line = line.replace("(Excel, VBA)", "(VBA)")
        line = line.replace("(True Basic)", "(BASIC)")
        line = line.replace("(True BASIC)", "(BASIC)")
        line = line.replace("(TI-BASIC)", "(BASIC)")
        line = line.replace("(Chipmunk BASIC)", "(BASIC)")
        line = line.replace("(Scheme:)", "(Scheme)")
        line = line.replace("(MIT Scheme:)", "(Scheme)")
        line = re.sub(r"\(PARI[^()]+\)", "(PARI)", line)
        line = re.sub(r"\(Scheme, [^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(Scheme function.+:\)", "(Scheme)", line)
        line = re.sub(r"\(MIT/GNU Scheme[^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(MIT Scheme[^()]+\)", "(Scheme)", line)
        line = re.sub(r"\(Scheme[^()]+\)", "(Scheme)", line)
        line = re.sub(r"\([^()]*Scheme[^()]*:\)", "(Scheme)", line)
        line = re.sub(r"\(Python[^()]+\)", "(Python)", line)
        line = re.sub(r"\(Ruby[^()]+\)", "(Ruby)", line)
        line = re.sub(r"\(PFGW[^()]+\)", "(PFGW)", line)
        line = re.sub(r"\(MATLAB[^()]+\)", "(MATLAB)", line)
        line = re.sub(r";;PLT DrScheme.+", "(Scheme)", line)
        line = re.sub(r"/\* bc .* \*/", "(bc)", line)
        line = line.replace("(C#)", "(Csharp)")
        line = line.replace("(C#.NET)", "(Csharp)")
        line = line.replace("(C++)", "(Cpp)")
        line = line.replace("(C/C++)", "(Cpp)")
        line = line.replace("(C++ 11)", "(Cpp)")
        line = line.replace("(Other) #include", "(Cpp) #include")
        line = line.replace("(GNU bc)", "(bc)")
        line = line.replace("  (PARI)", " (PARI)")
        line = line.replace("）", ")")
        line = line.replace("(GW-BASIC)", "(GWBASIC)")
        line = line.replace("(MIT/GNU Scheme)", "(Scheme)")
        line = line.replace("(PLT Scheme)", "(Scheme)")
        line = line.replace("(PLT DrScheme)", "(Scheme)")
        line = line.replace("(APL (NARS200 dialect))", "(APL)")
        line = line.replace("(SageMath)", "(Sage)")
        line = line.replace("(SageMath 9.2)", "(Sage)")
        line = line.replace("#(sage)", "(Sage)")
        line = line.replace("(Perl 5)", "(Perl)")
        line = line.replace("#!/usr/bin/perl", "(Perl)")
        line = line.replace("#!/usr/bin/python", "(Python)")
        line = line.replace("#!/bin/bash", "(Shell)")
        line = line.replace("(APL, Dyalog dialect)", "(APL)")
        line = line.replace("(APL, Dyalog Dialect)", "(APL)")
        line = line.replace("(nauty/bash)", "(Shell)")
        line = line.replace("(bash+nauty)", "(Shell)")
        line = line.replace("(nauty/shell)", "(Shell)")
        line = line.replace("(nauty with Laman plugin)", "(Shell)")
        line = line.replace("(Nauty with Laman plugin)", "(Shell)")
        line = line.replace("(bash/plantri)", "(Shell)")
        line = line.replace("(Macsyma)", "(Maxima)")
        line = line.replace("(Octave, MATLAB)", "(MATLAB)")
        line = line.replace("(OCTAVE, MATLAB)", "(MATLAB)")
        line = line.replace("(Octave/MATLAB)", "(MATLAB)")
        line = line.replace("(MATLAB/Octave)", "(MATLAB)")
        line = line.replace("(MATLAB with CPLEX)", "(MATLAB)")
        line = line.replace("(MATLAB with CPLEX API)", "(MATLAB)")
        line = line.replace("(MATLAB and FreeMat)", "(MATLAB)")
        line = line.replace("(S/R)", "(R)")
        line = line.replace("[S/R]", "(R)")
        line = line.replace("(sh)", "(Shell)")
        line = line.replace("(Common Lisp)", "(Lisp)")
        line = line.replace("(Common LISP)", "(Lisp)")
        line = line.replace("(Lisp, MacGambit)", "(Lisp)")
        line = line.replace("{Haskell}", "(Haskell)")
        line = line.replace("{PARI}", "(PARI)")
        line = line.replace("{MAGMA)", "(Magma)")
        line = line.replace("(Delphi)", "(Pascal)")
        line = line.replace("(Turbo-Pascal)", "(Pascal)")
        line = line.replace("(Java or beanShell script)", "(Java)")
        line = line.replace("(FORTRAN)", "(Fortran)")
        line = line.replace("(FORTRAN 77)", "(Fortran)")
        line = line.replace("(Iverson's J language)", "(J)")
        line = line.replace("(ANS Forth)", "(Forth)")
        line = line.replace("(ANS-Forth)", "(Forth)")
        line = line.replace("(Wolfram|Alpha)", "(Mathematica)")
        line = line.replace("(Isabelle/HOL)", "(Isabelle)")
        line = line.replace("(SWI-Prolog)", "(Prolog)")
        line = line.replace("(newLISP)", "(NewLisp)")
        line = line.replace("(End)", "")
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
            elif code_line.startswith("(define "):
                if current_program:
                    programs[current_lang].append("\n".join(current_program).strip())
                    current_program = []
                current_lang = "Scheme"
                current_program.append(code_line)
            elif ": n in [1.." in code_line:
                if current_program:
                    programs[current_lang].append("\n".join(current_program).strip())
                    current_program = []
                current_lang = "Magma"
                current_program.append(code_line)
            elif code_line.startswith("def ") and code_line.endswith("):"):
                if current_program:
                    programs[current_lang].append("\n".join(current_program).strip())
                    current_program = []
                current_lang = "Python"
                current_program.append(code_line)
            else:
                print(f"No language tag found: {line}")
                current_program = []

    if current_lang and current_program:
        programs[current_lang].append("\n".join(current_program).strip())

    programs["JSON"].append(repr(terms))

    return programs, name


"""
def write_programs(programs, sequence_id):
    if "Python" not in programs:
        return
    for lang, code_blocks in programs.items():
        if lang != "Python" and lang != "JSON" and lang != "Mathematica":
            continue
        if len(code_blocks) > 5:
            print(f"Skipping {sequence_id} due to too many code blocks: {"\n".join(code_blocks)}")
            continue
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
"""


def write_programs(programs, sequence_id, name):
    if "Python" not in programs:
        return

    # Create the output directory structure
    output_dir = os.path.join("md", sequence_id[:4])
    os.makedirs(output_dir, exist_ok=True)

    # Create the output filename
    filename = f"{sequence_id}.md"
    output_filepath = os.path.join(output_dir, filename)

    # Write the program to the file
    with open(output_filepath, "w") as f:
        name = re.sub(r"([_*\[\]()~`>#+=|{}.!-])", r"\\\1", name)
        print(f"# {name}", file=f)
        print(f"https://oeis.org/{sequence_id}", file=f)
        for lang, code_blocks in programs.items():
            if lang == "Cpp":
                lang = "C++"
            if lang == "Csharp":
                lang = "C#"
            if lang in ("Alpertron", "Derive", "Excel", "GAUSS", "Other"):
                print(f"Skipping {lang} in {sequence_id}: {code_blocks}")
                continue
            if (
                lang
                not in (
                    "ARIBAS",
                    "Axiom",
                    "bc",
                    "Lisp",
                    "Magma",
                    "Maple",
                    "Maxima",
                    "MiniZinc",
                    "PARI",
                    "PFGW",
                )
                and lang not in languages
                and lang.lower() not in languages
            ):
                raise ValueError(f"Unknown language in {sequence_id}: {lang}")
            print(f"## {lang}", file=f)
            if lang == "Maple" or len(code_blocks) > 10:
                print(f"```{lang}", file=f)
                print("\n".join(code_blocks), file=f)
                print("```", file=f)
                continue
            for code in code_blocks:
                print(f"```{lang}", file=f)
                print(code, file=f)
                print("```", file=f)


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
        "JSON": "json",
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
    programs, name = extract_programs(content)

    # Write programs to appropriate directories
    write_programs(programs, sequence_id, name)


def main():
    input_dir = "seq"

    for root, dirs, files in sorted(os.walk(input_dir)):
        for file in sorted(files):
            if file.endswith(".seq"):
                input_filepath = os.path.join(root, file)
                process_file(input_filepath)


if __name__ == "__main__":
    main()
