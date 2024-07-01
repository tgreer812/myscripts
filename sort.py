import argparse
import csv

def sort_csv(file_path, output_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        sorted_lines = sorted(reader)
    
    with open(output_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(sorted_lines)
    
    print(f"Sorted file has been written to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Sort a CSV file.')
    parser.add_argument('input', type=str, help='Path to the input CSV file')
    parser.add_argument('output', type=str, help='Path to the output sorted CSV file')
    
    args = parser.parse_args()
    
    sort_csv(args.input, args.output)

if __name__ == "__main__":
    main()
