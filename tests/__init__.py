"""
Init tests
"""
import sys
import os

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.dirname(current_directory)


if current_directory not in sys.path:
    sys.path.append(current_directory)
if parent_directory not in sys.path:
    sys.path.append(parent_directory)
