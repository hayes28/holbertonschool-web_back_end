#!/bin/bash

# Create virtual environment
python3 -m venv myenv

# Activate virtual environment
source myenv/bin/activate

# Install dependencies
pip install -r requirements.txt
