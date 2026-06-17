Parte 2 - Threads e semaforos
Arquivo
contador_semaforo.py: executa a versao sem sincronizacao e a versao com semaforo binario.

Execucao
bash
python contador_semaforo.py
Objetivo
Demonstrar uma condicao de corrida em um contador compartilhado acessado por varias threads e corrigi-la com um semaforo binario.

Parametros utilizados
T = 8 threads

M = 200000 incrementos por thread

3 rodadas por versao

O que acontece em cada versao
Sem sincronizacao
As threads leem e escrevem o contador compartilhado sem protecao. Como a operacao de incremento envolve leitura, modificacao e escrita, diferentes threads podem sobrescrever atualizacoes umas das outras, causando perda de incrementos.

Com semaforo binario
O semaforo com 1 permissao garante exclusao mutua na secao critica. Assim, apenas uma thread por vez atualiza o contador, e o valor final passa a ser corretamente igual a T x M.

Discussao tecnica
A versao sem sincronizacao pode apresentar throughput maior, mas produz resultado incorreto por causa da condicao de corrida. A versao com semaforo tende a ser mais lenta, porque serializa o acesso ao contador, mas garante corretude.

Em Python, o uso do semaforo tambem impõe uma ordenacao pratica entre as entradas na secao critica: a thread que adquire a permissao executa a atualizacao antes da proxima. Isso evita intercalacoes perigosas na leitura e escrita do contador.

Tabela de resultados
Depois de executar o script, copie a tabela impressa no terminal para esta secao do README.