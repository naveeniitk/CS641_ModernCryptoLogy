#!/bin/bash
sed -i 's/\r//' to_automate_cleaning.sh;python3 clean.py < output.txt > final_output.txt; python3 clean.py < plaintext.txt > final_input.txt;