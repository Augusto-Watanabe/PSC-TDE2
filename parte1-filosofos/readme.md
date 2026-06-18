## Arquivos

- `filosofos_ingenua.py`: versao ingenua que pode entrar em deadlock.
- `filosofos_corrigida.py`: versao corrigida com hierarquia de recursos.

## Execucao

```bash
python filosofos_ingenua.py
python filosofos_corrigida.py
```

## Dinamica do problema

O Jantar dos Filosofos modela cinco processos concorrentes sentados em uma mesa circular. Cada filosofo alterna entre pensar e comer, e para comer precisa dos dois garfos vizinhos, que sao recursos compartilhados.

Na versao ingenua, cada filosofo tenta pegar primeiro um garfo e depois o outro. Se varios filosofos pegam o primeiro garfo ao mesmo tempo, cada um pode ficar aguardando o segundo indefinidamente, criando uma espera circular e, por consequencia, um deadlock.

## Solucao adotada

A versao corrigida usa hierarquia de recursos: cada filosofo sempre pega primeiro o garfo de menor indice e depois o de maior indice. Essa ordem global elimina a espera circular e impede o deadlock.

## Condicao de Coffman negada

A estrategia nega a condicao de **espera circular**.

## Pseudocodigo da solucao corrigida

```text
Dados:
  N = 5
  Garfos = 0..N-1

Para cada filosofo p:
  esquerda = p
  direita = (p + 1) mod N
  primeiro = min(esquerda, direita)
  segundo = max(esquerda, direita)

Loop:
  pensar()
  estado[p] <- "com fome"
  adquirir(primeiro)
  adquirir(segundo)
  estado[p] <- "comendo"
  comer()
  liberar(segundo)
  liberar(primeiro)
  estado[p] <- "pensando"
```

## Evidencia de execucao

Na versao ingenua, os logs mostram os filosofos ficando com fome e pegando apenas o primeiro garfo, o que pode levar ao travamento. Na versao corrigida, os logs mostram progresso continuo e o resumo final de refeicoes de cada filosofo.

## Observacao sobre progresso

A hierarquia de recursos garante ausencia de deadlock porque nao existe ciclo de espera entre os filosofos.
'''