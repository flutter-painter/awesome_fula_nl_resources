#!/usr/bin/env python3
"""
Script to combine all src_*.txt files into one file and all tgt_*.txt files into another.
"""

import os
import glob
from pathlib import Path

def combine_files(pattern, output_filename):
    """Combine all files matching the pattern into a single output file."""
    # Get all matching files sorted alphabetically
    files = sorted(glob.glob(pattern))
    
    if not files:
        print(f"No files found matching pattern: {pattern}")
        return
    
    print(f"Combining {len(files)} files matching '{pattern}' into '{output_filename}'...")
    
    with open(output_filename, 'w', encoding='utf-8') as outfile:
        for filepath in files:
            filename = os.path.basename(filepath)
            print(f"  Processing: {filename}")
            
            with open(filepath, 'r', encoding='utf-8') as infile:
                # Copy all lines from input file to output file
                for line in infile:
                    outfile.write(line)
    
    print(f"✓ Successfully created: {output_filename}")
    print()

if __name__ == "__main__":
    # Get the directory where the script is located
    script_dir = Path(__file__).parent
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Combine src_ files
    combine_files("src_*.txt", "combined_src.txt")
    
    # Combine tgt_ files
    combine_files("tgt_*.txt", "combined_tgt.txt")
    
    print("Done!")
