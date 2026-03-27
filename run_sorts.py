import csv
import importlib.util
import os
import time
import glob
import logging

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

from prometheus_client import Histogram, Counter, start_http_server

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger("sort-algorithm")

OTEL_ENDPOINT = "http://localhost:4318"

tracer_provider = TracerProvider()
tracer_provider.add_span_processor(
    BatchSpanProcessor(OTLPSpanExporter(endpoint=f"{OTEL_ENDPOINT}/v1/traces"))
)
trace.set_tracer_provider(tracer_provider)
tracer = trace.get_tracer("sort-algorithm")

execution_time = Histogram(
    "sort_execution_time_seconds",
    "Tempo de execução em segundos",
    labelnames=["algorithm", "input_size"]
)

comparacoes_counter = Counter(
    "sort_comparacoes_total",
    "Total de comparações realizadas",
    labelnames=["algorithm", "input_size"]
)

trocas_counter = Counter(
    "sort_trocas_total",
    "Total de trocas realizadas",
    labelnames=["algorithm", "input_size"]
)

start_http_server(8000)

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
    logger.info(f"Iniciando {name} com {len(arr)} elementos")
    with tracer.start_as_current_span(name) as span:
        span.set_attribute("algorithm", name)
        span.set_attribute("input.size", len(arr))

        try:
            start = time.perf_counter()
            result, comparacoes, trocas = fn(arr.copy())
            elapsed = time.perf_counter() - start

            span.set_attribute("execution_time_s", elapsed)
            span.set_attribute("comparacoes", comparacoes)
            span.set_attribute("trocas", trocas)

            execution_time.labels(algorithm=name, input_size=str(len(arr))).observe(elapsed)
            comparacoes_counter.labels(algorithm=name, input_size=str(len(arr))).inc(comparacoes)
            trocas_counter.labels(algorithm=name, input_size=str(len(arr))).inc(trocas)

            logger.info(f"Finalizado {name} | {len(arr)} elementos | {elapsed:.6f}s | comparações: {comparacoes} | trocas: {trocas}")
            print(f"  [{name}] {len(arr)} elementos → {elapsed:.6f}s | comparações: {comparacoes} | trocas: {trocas}")
            return result

        except Exception as e:
            logger.error(f"Erro ao executar {name}: {e}")
            span.set_attribute("error", str(e))
            raise

BASE   = os.path.dirname(os.path.abspath(__file__))
bubble = load_module("bubble_sort", os.path.join(BASE, "sorts", "bubble_sort", "bubble_sort.py"))
insert = load_module("insert_sort", os.path.join(BASE, "sorts", "insert_sort", "insert_sort.py"))
merge  = load_module("merge_sort",  os.path.join(BASE, "sorts", "merge_sort",  "merge_sort.py"))

arrays = load_all_arrays(os.path.join(BASE, "data_arrays"))

for size, arr in arrays:
    print(f"\n── Array {size} elementos ──")
    run_sort("bubble_sort", bubble.bubbleSort, arr)
    run_sort("insert_sort", insert.insertSort, arr)
    run_sort("merge_sort",  merge.mergeSort,   arr)

print("\nMétricas em http://localhost:8000")

while True:
    time.sleep(5)