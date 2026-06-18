Parte 3 - Deadlock
Arquivos
deadlock_reproducao.py: reproduz o deadlock com duas threads e dois locks.

deadlock_corrigido.py: corrige o problema impondo ordem global de aquisicao.

Execucao
bash
python deadlock_reproducao.py
python deadlock_corrigido.py
Descricao do problema
O deadlock ocorre quando duas ou mais threads ficam bloqueadas indefinidamente, cada uma esperando um recurso que esta retido pela outra. No experimento desta parte, a Thread 1 adquire LOCK_A e depois tenta LOCK_B, enquanto a Thread 2 adquire LOCK_B e depois tenta LOCK_A.

Com essa ordem invertida, pode surgir um ciclo de espera: T1 segura LOCK_A e espera LOCK_B, enquanto T2 segura LOCK_B e espera LOCK_A. Como nenhuma das duas libera o lock que ja possui, o programa trava.

Quatro condicoes de Coffman observadas
Exclusao mutua: os locks so podem ser usados por uma thread de cada vez.

Manter e esperar: cada thread segura um lock enquanto espera pelo outro.

Nao preempcao: os locks nao sao retirados a forca das threads.

Espera circular: T1 espera um recurso de T2 e T2 espera um recurso de T1.

Solucao aplicada
A correcao consiste em impor uma hierarquia de recursos: todas as threads devem adquirir primeiro LOCK_A e depois LOCK_B. Assim, a condicao de espera circular e quebrada, e o deadlock deixa de ser possivel.

Pseudocodigo da versao corrigida
text
Regra global:
  sempre adquirir LOCK_A antes de LOCK_B

Thread 1 e Thread 2:
  adquirir(LOCK_A)
  adquirir(LOCK_B)
  secao critica
  liberar(LOCK_B)
  liberar(LOCK_A)
Evidencia esperada
Na versao deadlock_reproducao.py, os logs mostram a tentativa de aquisicao cruzada e, ao final, a mensagem de deteccao de deadlock apos o timeout. Na versao deadlock_corrigido.py, ambas as threads concluem normalmente.

Log versão com travamento:
[22:28:59.932] T1 tentando adquirir LOCK_A
[22:28:59.932] T1 adquiriu LOCK_A
[22:28:59.932] T2 tentando adquirir LOCK_B
[22:28:59.932] T2 adquiriu LOCK_B
[22:28:59.982] T1 tentando adquirir LOCK_B
[22:28:59.983] T2 tentando adquirir LOCK_A
[22:29:01.941] Deadlock detectado: as threads permaneceram bloqueadas apos o timeout.

Log versão sem travamento:
[22:29:42.593] T1 tentando adquirir LOCK_A
[22:29:42.593] T1 adquiriu LOCK_A
[22:29:42.594] T2 tentando adquirir LOCK_A
[22:29:42.644] T1 tentando adquirir LOCK_B
[22:29:42.644] T1 adquiriu LOCK_B
[22:29:42.644] T1 executando secao critica
[22:29:42.744] T1 liberou LOCK_B
[22:29:42.745] T1 liberou LOCK_A e concluiu
[22:29:42.745] T2 adquiriu LOCK_A
[22:29:42.795] T2 tentando adquirir LOCK_B
[22:29:42.795] T2 adquiriu LOCK_B
[22:29:42.795] T2 executando secao critica
[22:29:42.895] T2 liberou LOCK_B
[22:29:42.896] T2 liberou LOCK_A e concluiu
[22:29:42.896] Execucao terminou sem deadlock porque ambas as threads seguem a mesma ordem global de aquisicao.