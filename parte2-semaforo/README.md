## Arquivos

- `contador_sem_sincronizacao.py`: evidencia perda de incrementos.
- `contador_com_semaforo.py`: produz o valor correto com semaforo binario.

## Execucao

```bash
python contador_sem_sincronizacao.py
python contador_com_semaforo.py
```

## Objetivo

Demonstrar uma condicao de corrida em um contador compartilhado acessado por varias threads e corrigi-la com um semaforo binario.

## Resultados

Execuções sem sincronizacao:

1 exec:
Esperado = 1600000, Obtido = 1200000
Tempo de execução: 0.1109 segundos

2 exec:
Esperado = 1600000, Obtido = 1600000
Tempo de execução: 0.1090 segundos

3 exec:
Esperado = 1600000, Obtido = 1600000
Tempo de execução: 0.1043 segundos

Execuções com sincronização:

1 exec:
Esperado = 1600000, Obtido = 1600000
Tempo de execução: 1.4511 segundos

2 exec:
Esperado = 1600000, Obtido = 1600000
Tempo de execução: 1.4415 segundos

3 exec:
Esperado = 1600000, Obtido = 1600000
Tempo de execução: 1.4486 segundos

## Discussao tecnica

A versao sem sincronizacao pode perder incrementos porque a operacao `count = count + 1` nao e atomica: uma thread pode ler o valor, ser interrompida, e outra thread sobrescrever o contador antes da primeira concluir a escrita. Isso gera uma condicao de corrida e faz o resultado final variar entre execucoes.

A versao com semaforo binario e correta porque so permite que uma thread por vez entre na secao critica. Assim, cada incremento ocorre sem interferencia de outras threads, preservando o valor final esperado `T x M`.

O trade-off e claro: a versao sem sincronizacao tende a ser mais rapida, mas incorreta; a versao com semaforo reduz o throughput por serializar o acesso ao contador, mas garante corretude.

Quanto a visibilidade e ordenacao, em Java o `release()` de uma thread estabelece happens-before com o `acquire()` de outra. Em Python, o semaforo tambem atua como barreira pratica de sincronizacao, garantindo que as alteracoes feitas na secao critica fiquem consistentes para a proxima thread que entrar.

## Observacao

Os resultados da versao sem sincronizacao podem variar entre execucoes, o que e esperado em um experimento de concorrencia sem protecao.
'''