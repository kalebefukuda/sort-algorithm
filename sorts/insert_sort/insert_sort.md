# Insert Sort

## Descrição

Insertion Sort é um algoritmo de ordenação que constrói o array ordenado **um elemento por vez**.

A cada iteração, pega o elemento atual e o **insere na posição correta** dentro da parte já ordenada do array — empurrando os elementos maiores uma posição para a direita até encontrar onde ele se encaixa. É o mesmo processo que a maioria das pessoas usa para ordenar cartas na mão.

---

## Complexidade

| Caso   | Tempo    | Espaço |
|--------|----------|--------|
| Melhor | `O(n)`   | `O(1)` |
| Médio  | `O(n²)`  | `O(1)` |
| Pior   | `O(n²)`  | `O(1)` |

- **Estável:** ✅ Sim
- **In-place:** ✅ Sim

---

## Visualização

![Insertion Sort](/images/insert-sort.png)

---

## Quando usar?

- Quando o array já está **quase ordenado** (melhor caso real é próximo de `O(n)`)
- Para entradas **pequenas**, onde a simplicidade supera a eficiência assintótica
- Quando memória extra é uma restrição (não aloca espaço adicional)
- Não ideal para arrays grandes e desordenados