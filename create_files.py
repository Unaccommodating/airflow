import os
import random
import string

def create_files(num_files=100, file_size=1000):
    if not os.path.exists('text_files'):
        os.makedirs('text_files')

    for i in range(num_files):
        filename = f'text_files/file_{i + 1}.txt'
        with open(filename, 'w') as f:
            f.write(''.join(random.choices(string.ascii_letters, k=file_size)))

if __name__ == '__main__':
    create_files()
