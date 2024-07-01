import argparse

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def find_differences(file1_lines, file2_lines):
    differences = []
    i, j = 0, 0

    while i < len(file1_lines) and j < len(file2_lines):
        if file1_lines[i] != file2_lines[j]:
            differences.append(f"Line {i + 1} in file1: {file1_lines[i].strip()}")
            differences.append(f"Line {j + 1} in file2: {file2_lines[j].strip()}")
        i += 1
        j += 1

    while i < len(file1_lines):
        differences.append(f"Line {i + 1} in file1 but not in file2: {file1_lines[i].strip()}")
        i += 1

    while j < len(file2_lines):
        differences.append(f"Line {j + 1} in file2 but not in file1: {file2_lines[j].strip()}")
        j += 1

    return differences

def write_differences(differences, output_file):
    with open(output_file, 'w') as file:
        for diff in differences:
            file.write(f"{diff}\n")
    print(f"Differences have been written to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Find differences between two sorted files.')
    parser.add_argument('file1', type=str, help='Path to the first file')
    parser.add_argument('file2', type=str, help='Path to the second file')
    parser.add_argument('-o', '--output', type=str, default='differences.txt', help='Output file to write differences (default: differences.txt)')
    
    args = parser.parse_args()

    file1_lines = read_file(args.file1)
    file2_lines = read_file(args.file2)
    differences = find_differences(file1_lines, file2_lines)
    write_differences(differences, args.output)

if __name__ == "__main__":
    main()
