#!/bin/bash

# Initialize counters
passes=0
total=0

# Function to test a single Python script
test_script() {
    python_file="$1"
    json_file="${python_file/Python/JSON}"
    json_file="${json_file%.py}"
    json_file="${json_file%[a-z]}.json"
    seqname="$(basename "$json_file" .json)"

    echo -n "Testing $python_file ... "

    # Run the Python script and compare with JSON
    output="$(timeout 10 python "$python_file")"
    if echo "$output" | ./diff.py "$json_file" > /dev/null 2>&1; then
        echo "PASS ($passes / $total)"
        ((passes++))
    elif echo "[${output%, }]" | ./diff.py "$json_file" > /dev/null 2>&1; then
        echo MALFORMED
        ((passes++))
    elif [ -z "$output" ]; then
        output="$((cat "$python_file"; echo; echo "print([$seqname(n) for n in range(30)])") | timeout 10 python 2>/dev/null)"
        if echo "$output" | ./diff.py "$json_file" > /dev/null 2>&1; then
            echo DEF
            ((passes++))
        else
            echo EMPTY
        fi
    else
        echo FAIL
        echo "Differences:"
        echo "$output" | diff -Z "$json_file" -
    fi
    ((total++))
}

# Traverse the Python directory
find prog/Python -name "*.py" | sort | while read -r python_file; do
    test_script "$python_file"
done

# Print summary
echo "Total passes: $passes"
echo "Total fails: $fails"
