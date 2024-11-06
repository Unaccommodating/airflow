import os
import subprocess
from multiprocessing import Pool

def count_a(file_number):
    filename = f'text_files/file_{file_number}.txt'
    subprocess.run(['python', 'count_a.py', filename])

if __name__ == '__main__':
    os.makedirs('results', exist_ok=True)
    with Pool(processes=100) as pool:
        pool.map(count_a, range(1, 101))
