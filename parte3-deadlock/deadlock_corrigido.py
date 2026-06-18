import threading
import time
from datetime import datetime

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]


def log(msg):
    print(f'[{ts()}] {msg}', flush=True)


def executar_secao_critica(nome_thread):
    log(f'{nome_thread} tentando adquirir LOCK_A')
    with LOCK_A:
        log(f'{nome_thread} adquiriu LOCK_A')
        time.sleep(0.05)
        log(f'{nome_thread} tentando adquirir LOCK_B')
        with LOCK_B:
            log(f'{nome_thread} adquiriu LOCK_B')
            log(f'{nome_thread} executando secao critica')
            time.sleep(0.1)
        log(f'{nome_thread} liberou LOCK_B')
    log(f'{nome_thread} liberou LOCK_A e concluiu')


def main():
    t1 = threading.Thread(target=executar_secao_critica, args=('T1',))
    t2 = threading.Thread(target=executar_secao_critica, args=('T2',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    log('Execucao terminou sem deadlock porque ambas as threads seguem a mesma ordem global de aquisicao.')


if __name__ == '__main__':
    main()