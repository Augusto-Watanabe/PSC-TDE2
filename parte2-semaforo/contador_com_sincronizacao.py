import threading
import time

T = 8
M = 200_000
count = 0
sem = threading.Semaphore(1)

def worker():
    global count
    for i in range(M):
        sem.acquire()
        try:
            tmp = count
            if i % 1000 == 0:
                time.sleep(0)
            count = tmp + 1
        finally:
            sem.release()

def main():
    start_time = time.time()
    threads = [threading.Thread(target=worker) for _ in range(T)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    end_time = time.time()
    print(f'Esperado = {T*M}, Obtido = {count}')
    print(f'Tempo de execução: {end_time - start_time:.4f} segundos')

if __name__ == '__main__':
    main()