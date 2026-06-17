import threading
import time
from datetime import datetime

N = 5
RUN_TIME = 8

forks = [threading.Lock() for _ in range(N)]
start_barrier = threading.Barrier(N)
stop_event = threading.Event()


def ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]


def log(msg):
    print(f'[{ts()}] {msg}', flush=True)


def pensar(pid):
    log(f'Filosofo {pid} pensando')
    time.sleep(0.3)


def comer(pid):
    log(f'Filosofo {pid} comendo')
    time.sleep(0.3)


def filosofo(pid):
    esquerda = pid
    direita = (pid + 1) % N

    start_barrier.wait()

    while not stop_event.is_set():
        pensar(pid)
        log(f'Filosofo {pid} com fome')

        forks[esquerda].acquire()
        log(f'Filosofo {pid} pegou garfo {esquerda}')

        time.sleep(0.05)

        forks[direita].acquire()
        log(f'Filosofo {pid} pegou garfo {direita}')

        comer(pid)

        forks[direita].release()
        forks[esquerda].release()
        log(f'Filosofo {pid} voltou a pensar')


def main():
    threads = [threading.Thread(target=filosofo, args=(i,), daemon=True) for i in range(N)]

    for t in threads:
        t.start()

    time.sleep(RUN_TIME)
    stop_event.set()
    log('Execucao encerrada. Esta versao pode entrar em deadlock.')