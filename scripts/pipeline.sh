#!/bin/bash

# This will cause bash to stop executing the script if there's an error
set -e

# Run scraper
python scripts/run_scraper.py --url "https://goodresearch.dev/" --depth 3 --html_element 'p' --out_dir "results/"

