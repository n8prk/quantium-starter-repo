#!/bin/bash

# Run the test suite using the venv's Python directly (avoids CRLF issues with activate)
.venv/Scripts/python.exe -m pytest tests/test.py

# Return 0 if all tests passed, 1 otherwise
if [ $? -eq 0 ]; then
    exit 0
else
    exit 1
fi
