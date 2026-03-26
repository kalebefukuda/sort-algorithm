import csv
import importlib.util
import os

def load_module(name: str, filepath: str):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def load_array(filepath: str) -> list[int]:
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        return [int(x) for x in next(reader)]

ARRAY_FILE = "data_arrays/array_10000.csv"
BASE       = os.path.dirname(os.path.abspath(__file__))

bubble = load_module("bubble_sort", os.path.join(BASE, "sorts", "bubble_sort", "bubble_sort.py"))
merge  = load_module("merge_sort",  os.path.join(BASE, "sorts", "merge_sort",  "merge_sort.py"))

arr = load_array(ARRAY_FILE)

result_bubble = bubble.bubbleSort(arr.copy())
result_merge  = merge.mergeSort(arr.copy())

print(f"Array original ({len(arr)} elementos): {arr[:5]}...")
print(f"Bubble Sort:   {result_bubble[:5]}...")
print(f"Merge Sort:    {result_merge[:5]}...")