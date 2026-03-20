# Merge Sort

## Descrição

Merge Sort é um algoritmo de ordenação baseado na estratégia **dividir para conquistar**.

Ele divide o array ao meio recursivamente até que cada parte tenha apenas **1 elemento** — que por definição já está ordenado. Em seguida, no caminho de volta da recursão, vai **unindo (merge)** pares de arrays ordenados: comparando elemento a elemento e sempre inserindo o menor, até reconstruir o array completo e ordenado.

---

## Complexidade

| Caso   | Tempo        | Espaço |
|--------|--------------|--------|
| Melhor | `O(n log n)` | `O(n)` |
| Médio  | `O(n log n)` | `O(n)` |
| Pior   | `O(n log n)` | `O(n)` |

- **Estável:** ✅ Sim
- **In-place:** ❌ Não (usa memória extra)

---

## Visualização

![Merge Sort](/images/merge-sort.png)


## Quando usar?

- Quando a estabilidade da ordenação importa
- Quando o pior caso precisa ser garantido em `O(n log n)`
- Para ordenar **listas encadeadas** (mais eficiente que outros algoritmos)
- Não ideal quando memória extra é uma restrição