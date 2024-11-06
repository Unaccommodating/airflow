import sys

def count_a_in_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
    return content.count('a')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python count_a.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    count = count_a_in_file(filename)
    output_filename = filename.replace('text_files/file_', 'results/file_') + '.res'
    with open(output_filename, 'w') as output_file:
        output_file.write(str(count))
