import csv
import importlib.util
import os
import time
import glob

from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader

# setup OpenTelemetry
tracer_provider = TracerProvider()
tracer_provider.add_span_processor(BatchSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer("sort-algorithm")

reader = PeriodicExportingMetricReader(ConsoleMetricExporter(), export_interval_millis=1000)
meter_provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(meter_provider)
meter = metrics.get_meter("sort-algorithm")

execution_time = meter.create_histogram(
    name="sort.execution_time",
    description="Tempo de execução em segundos",
    unit="s",
)

# helpers
def load_module(name: str, filepath: str):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod  = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def load_array(filepath: str) -> list[int]:
    with open(filepath, newline="") as f:
        reader = csv.reader(f)
        return [int(x) for x in next(reader)]

def load_all_arrays(folder: str) -> list[tuple[int, list[int]]]:
    files = sorted(glob.glob(os.path.join(folder, "array_*.csv")))
    arrays = []
    for f in files:
        size = int(os.path.basename(f).replace("array_", "").replace(".csv", ""))
        arrays.append((size, load_array(f)))
    return arrays

def run_sort(name: str, fn, arr: list[int]):
    with tracer.start_as_current_span(name) as span:
        span.set_attribute("algorithm", name)
        span.set_attribute("input.size", len(arr))

        start = time.perf_counter()
        result = fn(arr.copy())
        elapsed = time.perf_counter() - start

        span.set_attribute("execution_time_s", elapsed)
        execution_time.record(elapsed, attributes={"algorithm": name})

        print(f"  [{name}] {len(arr)} elementos → {elapsed:.6f}s")
        return result

# carrega algoritmos
BASE   = os.path.dirname(os.path.abspath(__file__))
bubble = load_module("bubble_sort", os.path.join(BASE, "sorts", "bubble_sort", "bubble_sort.py"))
merge  = load_module("merge_sort",  os.path.join(BASE, "sorts", "merge_sort",  "merge_sort.py"))
insert = load_module("insert_sort", os.path.join(BASE, "sorts", "insert_sort", "insert_sort.py"))

# execução para todos os arrays da pasta
arrays = load_all_arrays(os.path.join(BASE, "data_arrays"))

for size, arr in arrays:
    print(f"\n── Array {size} elementos ──")
    run_sort("bubble_sort", bubble.bubbleSort, arr)
    run_sort("merge_sort",  merge.mergeSort,   arr)
    run_sort("insert_sort", insert.insertSort, arr)

time.sleep(2)