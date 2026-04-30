import threading
import time
import sys
import asyncio
import traceback

TRACK_LENGTH = 40
HORSES = ["Alpha  ", "Bravo  ", "Charlie", "Delta  ", "Echo   "]

# Prevents threads from garbling each other's terminal output.
print_lock = threading.Lock()


def draw_row(row: int, name: str, pos: int) -> None:
    """Draw one horse on its own terminal row, safely."""
    with print_lock:
        bar = "─" * pos + "🐎" + "·" * (TRACK_LENGTH - pos)
        # ANSI: move cursor to (row, col 1), clear line, write text.
        sys.stdout.write(f"\033[{row};1H\033[2K  {name} {bar} {pos:2d}/{TRACK_LENGTH}")
        sys.stdout.flush()


def run_horse(row: int, name: str, finishers: list, lock: threading.Lock) -> None:
    """A horse trots from 0 to TRACK_LENGTH, sleeping random amounts per step."""
    for pos in range(TRACK_LENGTH + 1):
        sum(i * i for i in range(200_000))  # simulated CPU-bound step
        # Simulate a crash for one horse in the middle of the race
        # if name.strip() == "Charlie" and pos == TRACK_LENGTH // 2:
        #     raise RuntimeError(f"{name.strip()} crashed at pos {pos}")
        draw_row(row, name, pos)
    with lock:
        finishers.append(name.strip())


async def race_parallel() -> None:
    sys.stdout.write("\033[2J\033[H")  # clear screen, home cursor
    print("PARALLEL: all horses racing at once\n")
    finishers: list[str] = []
    finish_lock = threading.Lock()
    start = time.time()

    # Schedule each run_horse in a separate thread and gather awaitables.
    tasks = [asyncio.to_thread(run_horse, i + 3, name, finishers, finish_lock)
             for i, name in enumerate(HORSES)]

    errors: list[tuple] = []
    for coro in asyncio.as_completed(tasks):
        try:
            await coro
        except Exception:
            errors.append(traceback.format_exc())

    sys.stdout.write(f"\033[{len(HORSES) + 5};1H\n")
    print(f"Elapsed: {time.time() - start:.2f}s")
    print(f"Finish order: {' → '.join(finishers)}")
    if errors:
        print("\nErrors from worker threads:")
        for tb in errors:
            print(tb)


def race_sequential() -> None:
    sys.stdout.write("\033[2J\033[H")
    print("SEQUENTIAL: one horse at a time\n")
    finishers: list[str] = []
    start = time.time()
    for i, name in enumerate(HORSES):
        run_horse(i + 3, name, finishers, threading.Lock())
    sys.stdout.write(f"\033[{len(HORSES) + 5};1H\n")
    print(f"Elapsed: {time.time() - start:.2f}s")
    print(f"Finish order: {' → '.join(finishers)}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "parallel"
    if mode == "sequential":
        race_sequential()
    else:
        asyncio.run(race_parallel())