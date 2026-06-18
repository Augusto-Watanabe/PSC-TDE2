import threading
import time
from datetime import datetime

LOCK_A = threading.Lock()
LOCK_B = threading.Lock()


def ts():
    return datetime.now().strftime('%H:%M:%S.%f')[:-3]


def log(msg):
    print(f'[{ts()}] {msg}', flush=True)


def thread1():
    log('T1 tentando adquirir LOCK_A')
    LOCK_A.acquire()
    log('T1 adquiriu LOCK_A')
    time.sleep(0.05)
    log('T1 tentando adquirir LOCK_B')
    LOCK_B.acquire()
    log('T1 adquiriu LOCK_B')
    log('T1 concluiu')
    LOCK_B.release()
    LOCK_A.release()


def thread2():
    log('T2 tentando adquirir LOCK_B')
    LOCK_B.acquire()
    log('T2 adquiriu LOCK_B')
    time.sleep(0.05)
    log('T2 tentando adquirir LOCK_A')
    LOCK_A.acquire()
    log('T2 adquiriu LOCK_A')
    log('T2 concluiu')
    LOCK_A.release()
    LOCK_B.release()


def main():
    t1 = threading.Thread(target=thread1, daemon=True)
    t2 = threading.Thread(target=thread2, daemon=True)

    t1.start()
    t2.start()

    t1.join(timeout=1.0)
    t2.join(timeout=1.0)

    if t1.is_alive() or t2.is_alive():
        log('Deadlock detectado: as threads permaneceram bloqueadas apos o timeout.')
    else:
        log('Execucao terminou sem deadlock.')


if __name__ == '__main__':
    main()