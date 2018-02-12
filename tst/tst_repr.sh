#!/bin/bash

python3 ../src/compute_cosines.py
python3 tst_comp_csv.py
rm ./*.csv
