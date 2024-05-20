#!/bin/bash
sed -i 's/\r//' plaintext to cipher text.sh;
touch output.txt;( cat plaintext.txt | ssh student@65.0.124.36 bash -s | tee -a ) > output.txt;