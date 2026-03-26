import csv
import random
import os

def generate_array_csv(size: int, min_val: int = 0, max_val: int = 100000):
    os.makedirs("data-arrays", exist_ok=True)

    filename = f"data-arrays/array_{size}.csv"
    array = [random.randint(min_val, max_val) for _ in range(size)]

    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(array)

    print(f"Arquivo gerado: {filename} ({size} elementos)")

if __name__ == "__main__":
    sizes = [1000, 5000, 10000]

    for size in sizes:
        generate_array_csv(size)