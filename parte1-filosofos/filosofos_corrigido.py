import threading
import time
import random
from datetime import datetime

N = 5
RUN_TIME = 8

forks = [threading.Lock() for _ in range(N)]
start_barrier = threading.Barrier(N)
stop_event = threading.Event()
meal_count = [0] * N
meal_lock = threading.Lock()


def ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]


def log(msg):
    print(f'[{ts()}] {msg}', flush=True)


def pensar(pid):
    log(f'Filosofo {pid} pensando')
    time.sleep(random.uniform(0.2, 0.5))


def comer(pid):
    log(f'Filosofo {pid} comendo')
    time.sleep(random.uniform(0.2, 0.4))


def filosofo(pid):
    garfo_esquerda = pid
    garfo_direita = (pid + 1) % N
    primeiro = min(garfo_esquerda, garfo_direita)
    segundo = max(garfo_esquerda, garfo_direita)

    start_barrier.wait()

    while not stop_event.is_set():
        pensar(pid)
        log(f'Filosofo {pid} com fome')

        forks[primeiro].acquire()
        log(f'Filosofo {pid} pegou garfo {primeiro}')

        time.sleep(0.02)

        forks[segundo].acquire()
        log(f'Filosofo {pid} pegou garfo {segundo}')

        comer(pid)

        with meal_lock:
            meal_count[pid] += 1

        forks[segundo].release()
        forks[primeiro].release()
        log(f'Filosofo {pid} voltou a pensar')


def main():
    threads = [threading.Thread(target=filosofo, args=(i,), daemon=True) for i in range(N)]

    for t in threads:
        t.start()

    time.sleep(RUN_TIME)
    stop_event.set()
    time.sleep(0.5)

    resumo = ', '.join(f'P{i}={meal_count[i]}' for i in range(N))
    log(f'Resumo de refeicoes: {resumo}')
    log('Execucao encerrada. Esta versao evita deadlock ao quebrar a espera circular.')


if __name__ == '__main__':
    main()