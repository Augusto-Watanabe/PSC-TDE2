Parte 1 - Jantar dos Filosofos


*Arquivos*
filosofos_ingenua.py: versao ingenua que pode entrar em deadlock.

filosofos_corrigida.py: versao corrigida com hierarquia de recursos.

*Execucao*
bash
python filosofos_ingenua.py
python filosofos_corrigida.py

*Exemplo de execucao*

filosofos_ingenua.py
[22:15:17.821] Filosofo 4 pensando
[22:15:17.821] Filosofo 2 pensando
[22:15:17.821] Filosofo 0 pensando
[22:15:17.821] Filosofo 3 pensando
[22:15:17.821] Filosofo 1 pensando
[22:15:18.121] Filosofo 0 com fome
[22:15:18.121] Filosofo 2 com fome
[22:15:18.121] Filosofo 1 com fome
[22:15:18.121] Filosofo 4 com fome
[22:15:18.122] Filosofo 0 pegou garfo 0
[22:15:18.122] Filosofo 2 pegou garfo 2
[22:15:18.122] Filosofo 1 pegou garfo 1
[22:15:18.121] Filosofo 3 com fome
[22:15:18.122] Filosofo 4 pegou garfo 4
[22:15:18.122] Filosofo 3 pegou garfo 3
[22:15:25.821] Execucao encerrada. Esta versao pode entrar em deadlock.

filosofos_corrigida.py
[22:11:40.236] Filosofo 4 pensando
[22:11:40.236] Filosofo 0 pensando
[22:11:40.236] Filosofo 3 pensando
[22:11:40.236] Filosofo 1 pensando
[22:11:40.236] Filosofo 2 pensando
[22:11:40.522] Filosofo 4 com fome
[22:11:40.522] Filosofo 4 pegou garfo 0
[22:11:40.542] Filosofo 4 pegou garfo 4
[22:11:40.542] Filosofo 4 comendo
[22:11:40.555] Filosofo 2 com fome
[22:11:40.556] Filosofo 2 pegou garfo 2
[22:11:40.557] Filosofo 0 com fome
[22:11:40.576] Filosofo 2 pegou garfo 3
[22:11:40.576] Filosofo 2 comendo
[22:11:40.636] Filosofo 1 com fome
[22:11:40.636] Filosofo 1 pegou garfo 1
[22:11:40.732] Filosofo 3 com fome
[22:11:40.917] Filosofo 4 voltou a pensar
[22:11:40.917] Filosofo 0 pegou garfo 0
[22:11:40.917] Filosofo 4 pensando
[22:11:40.936] Filosofo 2 voltou a pensar
[22:11:40.936] Filosofo 3 pegou garfo 3
[22:11:40.936] Filosofo 2 pensando
[22:11:40.936] Filosofo 1 pegou garfo 2
[22:11:40.936] Filosofo 1 comendo
[22:11:40.956] Filosofo 3 pegou garfo 4
[22:11:40.956] Filosofo 3 comendo
[22:11:41.142] Filosofo 1 voltou a pensar
[22:11:41.142] Filosofo 1 pensando
[22:11:41.142] Filosofo 0 pegou garfo 1
[22:11:41.142] Filosofo 0 comendo
[22:11:41.188] Filosofo 4 com fome
[22:11:41.314] Filosofo 3 voltou a pensar
[22:11:41.314] Filosofo 3 pensando
[22:11:41.372] Filosofo 2 com fome
[22:11:41.372] Filosofo 2 pegou garfo 2
[22:11:41.391] Filosofo 1 com fome
[22:11:41.392] Filosofo 2 pegou garfo 3
[22:11:41.392] Filosofo 2 comendo
[22:11:41.460] Filosofo 0 voltou a pensar
[22:11:41.460] Filosofo 1 pegou garfo 1
[22:11:41.460] Filosofo 0 pensando
[22:11:41.460] Filosofo 4 pegou garfo 0
[22:11:41.481] Filosofo 4 pegou garfo 4
[22:11:41.481] Filosofo 4 comendo
[22:11:41.672] Filosofo 0 com fome
[22:11:41.721] Filosofo 3 com fome
[22:11:41.758] Filosofo 2 voltou a pensar
[22:11:41.758] Filosofo 3 pegou garfo 3
[22:11:41.758] Filosofo 2 pensando
[22:11:41.758] Filosofo 1 pegou garfo 2
[22:11:41.758] Filosofo 1 comendo
[22:11:41.765] Filosofo 4 voltou a pensar
[22:11:41.765] Filosofo 0 pegou garfo 0
[22:11:41.765] Filosofo 4 pensando
[22:11:41.779] Filosofo 3 pegou garfo 4
[22:11:41.779] Filosofo 3 comendo
[22:11:41.985] Filosofo 3 voltou a pensar
[22:11:41.986] Filosofo 3 pensando
[22:11:42.143] Filosofo 2 com fome
[22:11:42.157] Filosofo 1 voltou a pensar
[22:11:42.157] Filosofo 2 pegou garfo 2
[22:11:42.157] Filosofo 1 pensando
[22:11:42.157] Filosofo 0 pegou garfo 1
[22:11:42.157] Filosofo 0 comendo
[22:11:42.178] Filosofo 2 pegou garfo 3
[22:11:42.178] Filosofo 2 comendo
[22:11:42.186] Filosofo 4 com fome
[22:11:42.255] Filosofo 3 com fome
[22:11:42.378] Filosofo 2 voltou a pensar
[22:11:42.378] Filosofo 3 pegou garfo 3
[22:11:42.378] Filosofo 2 pensando
[22:11:42.399] Filosofo 3 pegou garfo 4
[22:11:42.399] Filosofo 3 comendo
[22:11:42.511] Filosofo 0 voltou a pensar
[22:11:42.511] Filosofo 4 pegou garfo 0
[22:11:42.511] Filosofo 0 pensando
[22:11:42.565] Filosofo 1 com fome
[22:11:42.565] Filosofo 1 pegou garfo 1
[22:11:42.585] Filosofo 1 pegou garfo 2
[22:11:42.585] Filosofo 1 comendo
[22:11:42.773] Filosofo 3 voltou a pensar
[22:11:42.773] Filosofo 3 pensando
[22:11:42.773] Filosofo 4 pegou garfo 4
[22:11:42.773] Filosofo 4 comendo
[22:11:42.827] Filosofo 1 voltou a pensar
[22:11:42.827] Filosofo 1 pensando
[22:11:42.857] Filosofo 2 com fome
[22:11:42.857] Filosofo 2 pegou garfo 2
[22:11:42.877] Filosofo 2 pegou garfo 3
[22:11:42.877] Filosofo 2 comendo
[22:11:42.916] Filosofo 0 com fome
[22:11:43.024] Filosofo 4 voltou a pensar
[22:11:43.024] Filosofo 0 pegou garfo 0
[22:11:43.024] Filosofo 4 pensando
[22:11:43.044] Filosofo 0 pegou garfo 1
[22:11:43.044] Filosofo 0 comendo
[22:11:43.140] Filosofo 2 voltou a pensar
[22:11:43.140] Filosofo 2 pensando
[22:11:43.167] Filosofo 1 com fome
[22:11:43.188] Filosofo 3 com fome
[22:11:43.188] Filosofo 3 pegou garfo 3
[22:11:43.208] Filosofo 3 pegou garfo 4
[22:11:43.208] Filosofo 3 comendo
[22:11:43.315] Filosofo 0 voltou a pensar
[22:11:43.315] Filosofo 1 pegou garfo 1
[22:11:43.315] Filosofo 0 pensando
[22:11:43.336] Filosofo 1 pegou garfo 2
[22:11:43.336] Filosofo 1 comendo
[22:11:43.450] Filosofo 3 voltou a pensar
[22:11:43.450] Filosofo 3 pensando
[22:11:43.451] Filosofo 2 com fome
[22:11:43.468] Filosofo 4 com fome
[22:11:43.468] Filosofo 4 pegou garfo 0
[22:11:43.489] Filosofo 4 pegou garfo 4
[22:11:43.489] Filosofo 4 comendo
[22:11:43.614] Filosofo 0 com fome
[22:11:43.637] Filosofo 1 voltou a pensar
[22:11:43.638] Filosofo 2 pegou garfo 2
[22:11:43.638] Filosofo 1 pensando
[22:11:43.658] Filosofo 2 pegou garfo 3
[22:11:43.658] Filosofo 2 comendo
[22:11:43.818] Filosofo 3 com fome
[22:11:43.888] Filosofo 4 voltou a pensar
[22:11:43.888] Filosofo 0 pegou garfo 0
[22:11:43.888] Filosofo 4 pensando
[22:11:43.892] Filosofo 2 voltou a pensar
[22:11:43.892] Filosofo 3 pegou garfo 3
[22:11:43.892] Filosofo 2 pensando
[22:11:43.908] Filosofo 0 pegou garfo 1
[22:11:43.908] Filosofo 0 comendo
[22:11:43.912] Filosofo 3 pegou garfo 4
[22:11:43.912] Filosofo 3 comendo
[22:11:44.051] Filosofo 1 com fome
[22:11:44.102] Filosofo 4 com fome
[22:11:44.145] Filosofo 0 voltou a pensar
[22:11:44.145] Filosofo 1 pegou garfo 1
[22:11:44.146] Filosofo 0 pensando
[22:11:44.145] Filosofo 4 pegou garfo 0
[22:11:44.166] Filosofo 1 pegou garfo 2
[22:11:44.166] Filosofo 1 comendo
[22:11:44.238] Filosofo 3 voltou a pensar
[22:11:44.238] Filosofo 4 pegou garfo 4
[22:11:44.239] Filosofo 3 pensando
[22:11:44.239] Filosofo 4 comendo
[22:11:44.376] Filosofo 2 com fome
[22:11:44.391] Filosofo 0 com fome
[22:11:44.521] Filosofo 1 voltou a pensar
[22:11:44.521] Filosofo 2 pegou garfo 2
[22:11:44.521] Filosofo 1 pensando
[22:11:44.542] Filosofo 2 pegou garfo 3
[22:11:44.542] Filosofo 2 comendo
[22:11:44.637] Filosofo 4 voltou a pensar
[22:11:44.637] Filosofo 0 pegou garfo 0
[22:11:44.637] Filosofo 4 pensando
[22:11:44.658] Filosofo 0 pegou garfo 1
[22:11:44.658] Filosofo 0 comendo
[22:11:44.704] Filosofo 3 com fome
[22:11:44.872] Filosofo 0 voltou a pensar
[22:11:44.873] Filosofo 0 pensando
[22:11:44.899] Filosofo 2 voltou a pensar
[22:11:44.899] Filosofo 3 pegou garfo 3
[22:11:44.899] Filosofo 2 pensando
[22:11:44.919] Filosofo 3 pegou garfo 4
[22:11:44.919] Filosofo 3 comendo
[22:11:44.961] Filosofo 1 com fome
[22:11:44.962] Filosofo 1 pegou garfo 1
[22:11:44.982] Filosofo 1 pegou garfo 2
[22:11:44.982] Filosofo 1 comendo
[22:11:45.063] Filosofo 4 com fome
[22:11:45.063] Filosofo 4 pegou garfo 0
[22:11:45.149] Filosofo 2 com fome
[22:11:45.170] Filosofo 3 voltou a pensar
[22:11:45.170] Filosofo 4 pegou garfo 4
[22:11:45.170] Filosofo 3 pensando
[22:11:45.170] Filosofo 4 comendo
[22:11:45.306] Filosofo 1 voltou a pensar
[22:11:45.306] Filosofo 2 pegou garfo 2
[22:11:45.306] Filosofo 1 pensando
[22:11:45.327] Filosofo 2 pegou garfo 3
[22:11:45.327] Filosofo 2 comendo
[22:11:45.348] Filosofo 0 com fome
[22:11:45.412] Filosofo 4 voltou a pensar
[22:11:45.412] Filosofo 0 pegou garfo 0
[22:11:45.412] Filosofo 4 pensando
[22:11:45.433] Filosofo 0 pegou garfo 1
[22:11:45.433] Filosofo 0 comendo
[22:11:45.525] Filosofo 1 com fome
[22:11:45.622] Filosofo 3 com fome
[22:11:45.689] Filosofo 2 voltou a pensar
[22:11:45.689] Filosofo 3 pegou garfo 3
[22:11:45.689] Filosofo 2 pensando
[22:11:45.710] Filosofo 3 pegou garfo 4
[22:11:45.710] Filosofo 3 comendo
[22:11:45.823] Filosofo 0 voltou a pensar
[22:11:45.823] Filosofo 1 pegou garfo 1
[22:11:45.823] Filosofo 0 pensando
[22:11:45.843] Filosofo 1 pegou garfo 2
[22:11:45.843] Filosofo 1 comendo
[22:11:45.857] Filosofo 4 com fome
[22:11:45.857] Filosofo 4 pegou garfo 0
[22:11:45.949] Filosofo 3 voltou a pensar
[22:11:45.949] Filosofo 4 pegou garfo 4
[22:11:45.950] Filosofo 3 pensando
[22:11:45.950] Filosofo 4 comendo
[22:11:46.146] Filosofo 2 com fome
[22:11:46.170] Filosofo 1 voltou a pensar
[22:11:46.170] Filosofo 2 pegou garfo 2
[22:11:46.170] Filosofo 1 pensando
[22:11:46.190] Filosofo 2 pegou garfo 3
[22:11:46.190] Filosofo 2 comendo
[22:11:46.245] Filosofo 4 voltou a pensar
[22:11:46.245] Filosofo 4 pensando
[22:11:46.261] Filosofo 0 com fome
[22:11:46.261] Filosofo 0 pegou garfo 0
[22:11:46.281] Filosofo 0 pegou garfo 1
[22:11:46.281] Filosofo 0 comendo
[22:11:46.380] Filosofo 3 com fome
[22:11:46.390] Filosofo 1 com fome
[22:11:46.460] Filosofo 2 voltou a pensar
[22:11:46.460] Filosofo 3 pegou garfo 3
[22:11:46.460] Filosofo 2 pensando
[22:11:46.480] Filosofo 3 pegou garfo 4
[22:11:46.480] Filosofo 3 comendo
[22:11:46.610] Filosofo 0 voltou a pensar
[22:11:46.610] Filosofo 1 pegou garfo 1
[22:11:46.611] Filosofo 0 pensando
[22:11:46.631] Filosofo 1 pegou garfo 2
[22:11:46.631] Filosofo 1 comendo
[22:11:46.644] Filosofo 4 com fome
[22:11:46.644] Filosofo 4 pegou garfo 0
[22:11:46.685] Filosofo 3 voltou a pensar
[22:11:46.685] Filosofo 4 pegou garfo 4
[22:11:46.685] Filosofo 3 pensando
[22:11:46.685] Filosofo 4 comendo
[22:11:46.726] Filosofo 2 com fome
[22:11:46.834] Filosofo 1 voltou a pensar
[22:11:46.834] Filosofo 2 pegou garfo 2
[22:11:46.835] Filosofo 1 pensando
[22:11:46.855] Filosofo 2 pegou garfo 3
[22:11:46.855] Filosofo 2 comendo
[22:11:46.890] Filosofo 3 com fome
[22:11:47.007] Filosofo 4 voltou a pensar
[22:11:47.007] Filosofo 4 pensando
[22:11:47.049] Filosofo 1 com fome
[22:11:47.050] Filosofo 1 pegou garfo 1
[22:11:47.096] Filosofo 2 voltou a pensar
[22:11:47.096] Filosofo 3 pegou garfo 3
[22:11:47.097] Filosofo 2 pensando
[22:11:47.096] Filosofo 1 pegou garfo 2
[22:11:47.097] Filosofo 1 comendo
[22:11:47.106] Filosofo 0 com fome
[22:11:47.106] Filosofo 0 pegou garfo 0
[22:11:47.117] Filosofo 3 pegou garfo 4
[22:11:47.117] Filosofo 3 comendo
[22:11:47.293] Filosofo 4 com fome
[22:11:47.339] Filosofo 1 voltou a pensar
[22:11:47.339] Filosofo 0 pegou garfo 1
[22:11:47.339] Filosofo 1 pensando
[22:11:47.339] Filosofo 0 comendo
[22:11:47.341] Filosofo 3 voltou a pensar
[22:11:47.341] Filosofo 3 pensando
[22:11:47.541] Filosofo 2 com fome
[22:11:47.541] Filosofo 2 pegou garfo 2
[22:11:47.561] Filosofo 2 pegou garfo 3
[22:11:47.561] Filosofo 2 comendo
[22:11:47.706] Filosofo 0 voltou a pensar
[22:11:47.706] Filosofo 4 pegou garfo 0
[22:11:47.706] Filosofo 0 pensando
[22:11:47.726] Filosofo 4 pegou garfo 4
[22:11:47.726] Filosofo 4 comendo
[22:11:47.751] Filosofo 3 com fome
[22:11:47.836] Filosofo 1 com fome
[22:11:47.836] Filosofo 1 pegou garfo 1
[22:11:47.853] Filosofo 2 voltou a pensar
[22:11:47.853] Filosofo 3 pegou garfo 3
[22:11:47.853] Filosofo 2 pensando
[22:11:47.856] Filosofo 1 pegou garfo 2
[22:11:47.856] Filosofo 1 comendo
[22:11:48.041] Filosofo 0 com fome
[22:11:48.056] Filosofo 4 voltou a pensar
[22:11:48.056] Filosofo 3 pegou garfo 4
[22:11:48.056] Filosofo 0 pegou garfo 0
[22:11:48.057] Filosofo 3 comendo
[22:11:48.057] Filosofo 4 pensando
[22:11:48.096] Filosofo 2 com fome
[22:11:48.155] Filosofo 1 voltou a pensar
[22:11:48.155] Filosofo 2 pegou garfo 2
[22:11:48.155] Filosofo 1 pensando
[22:11:48.155] Filosofo 0 pegou garfo 1
[22:11:48.156] Filosofo 0 comendo
[22:11:48.291] Filosofo 3 voltou a pensar
[22:11:48.291] Filosofo 2 pegou garfo 3
[22:11:48.291] Filosofo 2 comendo
[22:11:48.357] Filosofo 1 com fome
[22:11:48.458] Filosofo 4 com fome
[22:11:48.490] Filosofo 0 voltou a pensar
[22:11:48.491] Filosofo 1 pegou garfo 1
[22:11:48.491] Filosofo 4 pegou garfo 0
[22:11:48.511] Filosofo 4 pegou garfo 4
[22:11:48.512] Filosofo 4 comendo
[22:11:48.568] Filosofo 2 voltou a pensar
[22:11:48.568] Filosofo 1 pegou garfo 2
[22:11:48.569] Filosofo 1 comendo
[22:11:48.737] Resumo de refeicoes: P0=9, P1=10, P2=11, P3=10, P4=9
[22:11:48.737] Execucao encerrada. Esta versao evita deadlock ao quebrar a espera circular.


*Resumo tecnico*
Na versao ingenua, cada filosofo tenta pegar primeiro o garfo da esquerda e depois o da direita. Se todos fizerem isso ao mesmo tempo, cada thread pode manter um garfo e esperar indefinidamente pelo outro, caracterizando impasse.
Na versao corrigida, cada filosofo sempre adquire primeiro o garfo de menor indice e depois o de maior indice. Essa regra cria uma ordem global de aquisicao dos recursos e elimina a condicao de espera circular, impedindo o deadlock.

*Condicao de Coffman negada*
A solucao corrige o problema ao quebrar a espera circular.

*Pseudocodigo da solucao corrigida*
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
  
*Justica e progresso*
A hierarquia de recursos garante ausencia de deadlock porque nao existe ciclo de espera entre os filosofos. O progresso pode ser observado nos logs da versao corrigida, onde diferentes filosofos continuam conseguindo comer ao longo da execucao.