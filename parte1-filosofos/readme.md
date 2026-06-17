Parte 1 - Jantar dos Filosofos
Arquivos
filosofos_ingenua.py: versao ingenua que pode entrar em deadlock.

filosofos_corrigida.py: versao corrigida com hierarquia de recursos.

Execucao
bash
python filosofos_ingenua.py
python filosofos_corrigida.py
Resumo tecnico
Na versao ingenua, cada filosofo tenta pegar primeiro o garfo da esquerda e depois o da direita. Se todos fizerem isso ao mesmo tempo, cada thread pode manter um garfo e esperar indefinidamente pelo outro, caracterizando impasse.

Na versao corrigida, cada filosofo sempre adquire primeiro o garfo de menor indice e depois o de maior indice. Essa regra cria uma ordem global de aquisicao dos recursos e elimina a condicao de espera circular, impedindo o deadlock.

Condicao de Coffman negada
A solucao corrige o problema ao quebrar a espera circular.

Pseudocodigo da solucao corrigida
text
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
  
Justica e progresso
A hierarquia de recursos garante ausencia de deadlock porque nao existe ciclo de espera entre os filosofos. O progresso pode ser observado nos logs da versao corrigida, onde diferentes filosofos continuam conseguindo comer ao longo da execucao.