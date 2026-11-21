import multiprocessing as mp
import time
import sys

def burn(stop_at):
    x = 0
    while time.time() < stop_at:
        x = (x * 31 + 7) % 1000003  # kalkulasi sia-sia biar CPU sibuk

if __name__ == "__main__":
    durasi = int(sys.argv[1]) if len(sys.argv) > 1 else 60  # detik
    jumlah = int(sys.argv[2]) if len(sys.argv) > 2 else mp.cpu_count()

    print(f"Stress CPU: {jumlah} proses selama {durasi} detik. Ctrl+C untuk berhenti.")
    stop_at = time.time() + durasi
    procs = [mp.Process(target=burn, args=(stop_at,)) for _ in range(jumlah)]

    try:
        for p in procs:
            p.start()
        for p in procs:
            p.join()
    except KeyboardInterrupt:
        for p in procs:
            p.terminate()
        print("Dihentikan.")
    print("Selesai.")