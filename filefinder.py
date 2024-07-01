import argparse
import os
import re
import json
import csv

def file_matches_pattern(file, pattern):
    return re.match(pattern, file) is not None

def find_files(path, pattern, recursive):
    matched_files = []
    if recursive:
        for root, _, files in os.walk(path):
            for file in files:
                if file_matches_pattern(file, pattern):
                    matched_files.append(os.path.join(root, file))
    else:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)) and re.match(pattern, file):
                matched_files.append(os.path.join(path, file))
    return matched_files

def export_files(file_list, export_type, summarize):
    if summarize:
        print(f"Number of files found: {len(file_list)}")
    else:
        if export_type == "json":
            with open('file_list.json', 'w') as f:
                json.dump(file_list, f, indent=4)
            print("File list exported to file_list.json")
        elif export_type == "txt":
            with open('file_list.txt', 'w') as f:
                for file in file_list:
                    f.write(f"{file}\n")
            print("File list exported to file_list.txt")
        elif export_type == "csv":
            with open('file_list.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["File Path"])
                for file in file_list:
                    writer.writerow([file])
            print("File list exported to file_list.csv")

def run(args):
    files = find_files(args.path, args.pattern, args.recursive)
    export_files(files, args.export, args.summarize)

def main():
    parser = argparse.ArgumentParser(description='Find files matching a regex pattern.')
    parser.add_argument('path', type=str, help='The path to search for files')
    parser.add_argument('pattern', type=str, help='The regex pattern to match files')
    parser.add_argument('--recursive', action='store_true', help='Recursively search through directories')
    parser.add_argument('--export', type=str, choices=['json', 'txt', 'csv'], default='json', help='Export type: json, txt, csv')
    parser.add_argument('--summarize', action='store_true', help='Summarize the number of files found')

    args = parser.parse_args()

    run(args)

if __name__ == "__main__":
    main()