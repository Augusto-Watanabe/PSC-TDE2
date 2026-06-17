import threading
import time
from statistics import mean

T = 8
M = 200_000
RODADAS = 3


def run_without_semaphore(num_threads=T, increments=M):
    global count
    count = 0

    def worker():
        global count
        for _ in range(increments):
            temp = count
            if _ % 1000 == 0:
                time.sleep(0)
            temp += 1
            count = temp

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    start = time.perf_counter()

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    return count, elapsed


def run_with_semaphore(num_threads=T, increments=M):
    global count
    count = 0
    sem = threading.Semaphore(1)

    def worker():
        global count
        for _ in range(increments):
            sem.acquire()
            try:
                temp = count
                if _ % 1000 == 0:
                    time.sleep(0)
                temp += 1
                count = temp
            finally:
                sem.release()

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    start = time.perf_counter()

    for t in threads:
        t.start()
    for t in threads:
        t.join()

    elapsed = time.perf_counter() - start
    return count, elapsed


def format_table(rows):
    header = f"{'Versao':<18} {'Rodada':<8} {'Esperado':<12} {'Obtido':<12} {'Tempo (s)':<10}"
    sep = '-' * len(header)
    lines = [header, sep]
    for row in rows:
        lines.append(f"{row['versao']:<18} {row['rodada']:<8} {row['esperado']:<12} {row['obtido']:<12} {row['tempo']:<10.4f}")
    return '
'.join(lines)


def main():
    expected = T * M
    results = []

    print(f'Parametros: T={T}, M={M}, esperado={expected}')
    print()

    for rodada in range(1, RODADAS + 1):
        obtained, elapsed = run_without_semaphore()
        results.append({
            'versao': 'sem semaforo',
            'rodada': rodada,
            'esperado': expected,
            'obtido': obtained,
            'tempo': elapsed,
        })
        print(f'[sem semaforo] rodada {rodada}: esperado={expected}, obtido={obtained}, tempo={elapsed:.4f}s')

    print()

    for rodada in range(1, RODADAS + 1):
        obtained, elapsed = run_with_semaphore()
        results.append({
            'versao': 'com semaforo',
            'rodada': rodada,
            'esperado': expected,
            'obtido': obtained,
            'tempo': elapsed,
        })
        print(f'[com semaforo] rodada {rodada}: esperado={expected}, obtido={obtained}, tempo={elapsed:.4f}s')

    print('
Tabela resumida:
')
    print(format_table(results))

    sem_times = [r['tempo'] for r in results if r['versao'] == 'sem semaforo']
    com_times = [r['tempo'] for r in results if r['versao'] == 'com semaforo']
    print('
Medias:')
    print(f"sem semaforo: {mean(sem_times):.4f}s")
    print(f"com semaforo: {mean(com_times):.4f}s")


if __name__ == '__main__':
    main()