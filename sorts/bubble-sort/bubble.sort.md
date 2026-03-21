# Bubble Sort

## Descrição
Bubble Sort é um algoritmo de ordenação baseado em comparações entre elementos vizinhos.

A cada passagem pelo array, compara elementos adjacentes dois a dois — o da esquerda com o da direita — e os troca de posição se o da esquerda for maior. Isso faz com que o maior elemento vá até o final do array. O processo se repete, e a cada passagem o próximo maior elemento vai para o seu lugar, até que o array inteiro esteja ordenado.

## Complexidade

| Caso   | Tempo      | Espaço |
|--------|------------|--------|
| Melhor | `O(n)`     | `O(1)` |
| Médio  | `O(n²)`    | `O(1)` |
| Pior   | `O(n²)`    | `O(1)` |

- **Estável:** ✅ Sim
- **In-place:** ✅ Sim (não usa memória extra)

## Visualização
![Bubble Sort](/images/bubble-sort.png)

## Quando usar?
- Quando o array já está quase ordenado (melhor caso `O(n)` com a otimização de parada antecipada)
- Não ideal para arrays grandes devido à complexidade `O(n²)` no caso médio e pior
  
## Otimização?
- A cada loop nao precisamos verificar o array inteiro, pois como o maior valor já está ao fim do array, sempre regredimos a busca do range