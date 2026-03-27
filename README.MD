# Sort Algorithm

Implementação, instrumentação e análise de algoritmos de ordenação com observabilidade via OpenTelemetry, Prometheus e Grafana.

---

## Algoritmos implementados

| Algoritmo | Complexidade | Documentação |
|---|---|---|
| Bubble Sort | O(n²) | [bubble_sort.md](sorts/bubble_sort/bubble_sort.md) |
| Insertion Sort | O(n²) | [insert_sort.md](sorts/insert_sort/insert_sort.md) |
| Merge Sort | O(n log n) | [merge_sort.md](sorts/merge_sort/merge_sort.md) |

---

## Estrutura do projeto

```
sort-algorithm/
├── data_arrays/                  # Arrays gerados em CSV
│   ├── array_1000.csv
│   ├── array_5000.csv
│   ├── array_10000.csv
│   └── array_50000.csv
├── sorts/
│   ├── bubble_sort/
│   │   ├── bubble_sort.py
│   │   └── bubble_sort.md
│   ├── insert_sort/
│   │   ├── insert_sort.py
│   │   └── insert_sort.md
│   └── merge_sort/
│       ├── merge_sort.py
│       └── merge_sort.md
├── generator_array_csv.py        # Gerador de arrays aleatórios
├── run_sorts.py                  # Runner principal com instrumentação
├── docker-compose.yml            # Stack de observabilidade
├── otel-collector-config.yml     # Configuração do OTel Collector
├── prometheus.yml                # Configuração do Prometheus
└── requirements.txt
```

---

## Pré-requisitos

- Python 3.12+
- Docker Desktop

---

## Instalação

```bash
pip install -r requirements.txt
```

---

## Como gerar os arrays

```bash
python generator_array_csv.py
```

Os arquivos são salvos em `data_arrays/` com o padrão `array_{tamanho}.csv`.
Para personalizar os tamanhos, edite a lista `sizes` no arquivo.

---

## Como executar os algoritmos

### 1. Suba a stack de observabilidade

```bash
docker-compose up -d
```

### 2. Execute o runner

```bash
python run_sorts.py
```

O script lê automaticamente todos os arrays em `data_arrays/`, executa os três algoritmos para cada tamanho e mantém o servidor de métricas no ar para o Prometheus coletar.

> ⚠️ Não feche o terminal enquanto quiser visualizar os dados no Grafana.

---

## Observabilidade

| Ferramenta | URL | Descrição |
|---|---|---|
| Métricas (raw) | http://localhost:8000 | Endpoint Prometheus do script |
| Prometheus | http://localhost:9090 | Consultas e visualização raw |
| Grafana | http://localhost:3000 | Dashboards (login: admin / admin) |

### Queries úteis no Prometheus

```promql
# Tempo de execução por algoritmo e tamanho
sort_execution_time_seconds_sum

# Filtrar por tamanho específico
sort_execution_time_seconds_sum{input_size="10000"}

# Filtrar por algoritmo
sort_execution_time_seconds_sum{algorithm="merge_sort"}
```

---

## Parando a stack

```bash
docker-compose down
```