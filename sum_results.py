import os

def sum_results():
    total_count = 0
    for i in range(1, 101):
        result_file = f'results/file_{i}.txt.res'
        if os.path.exists(result_file):
            with open(result_file, 'r') as f:
                total_count += int(f.read())
    with open('total_count.txt', 'w') as f:
        f.write(f'Total count of "a": {total_count}')

if __name__ == '__main__':
    sum_results()
