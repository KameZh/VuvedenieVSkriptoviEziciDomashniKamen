import os
import math
import time
import sys

MAP = [
    "################",
    "#..............#",
    "#..............#",
    "#......##......#",
    "#..............#",
    "#..............#",
    "#..............#",
    "################"
]

H = len(MAP)
W = len(MAP[0])

player_x = 3.0
player_y = 3.0
player_angle = 0.0
FOV = math.pi / 3
DEPTH = 16

def cast_ray(px, py, angle):
    sin_a = math.sin(angle)
    cos_a = math.cos(angle)
    step = 0.2
    dist = 0.0
    while dist < DEPTH:
        dist += step
        tx = px + cos_a * dist
        ty = py + sin_a * dist
        ix = int(tx)
        iy = int(ty)
        if iy < 0 or iy >= H or ix < 0 or ix >= W:
            return DEPTH
        if MAP[iy][ix] == "#":
            return dist
    return DEPTH

# Unix (curses) renderer left mostly intact
def curses_loop(stdscr):
    import curses
    curses.curs_set(0)
    stdscr.nodelay(True)

    global player_x, player_y, player_angle

    while True:
        stdscr.erase()
        height, width = stdscr.getmaxyx()

        for col in range(width):
            angle = player_angle - FOV/2 + FOV * col / width
            dist = cast_ray(player_x, player_y, angle)

            # avoid zero
            wall_height = height // int(dist if dist >= 1e-3 else 1)

            shade_chars = "#@%XO+=-:. "
            shade = shade_chars[min(int(dist), len(shade_chars)-1)]

            for row in range(height):
                if height//2 - wall_height//2 <= row <= height//2 + wall_height//2:
                    try:
                        stdscr.addch(row, col, shade)
                    except curses.error:
                        pass
                elif row < height // 2:
                    try:
                        stdscr.addch(row, col, ".")
                    except curses.error:
                        pass
                else:
                    try:
                        stdscr.addch(row, col, ",")
                    except curses.error:
                        pass

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_LEFT:
            player_angle -= 0.1
        if key == curses.KEY_RIGHT:
            player_angle += 0.1
        if key == curses.KEY_UP:
            nx = player_x + math.cos(player_angle) * 0.2
            ny = player_y + math.sin(player_angle) * 0.2
            if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                player_x = nx
                player_y = ny
        if key == curses.KEY_DOWN:
            nx = player_x - math.cos(player_angle) * 0.2
            ny = player_y - math.sin(player_angle) * 0.2
            if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                player_x = nx
                player_y = ny

        stdscr.refresh()
        time.sleep(0.01)

# Windows-friendly renderer (no curses)
def windows_loop():
    import shutil
    try:
        import msvcrt
    except Exception:
        print("msvcrt not available; windows fallback requires msvcrt.")
        return

    global player_x, player_y, player_angle

    shade_chars = "#@%XO+=-:. "
    last_time = time.time()

    while True:
        cols, rows = shutil.get_terminal_size()
        cols = max(20, cols)
        rows = max(10, rows)

        # build buffer as list of char arrays
        buffer = [list(" " * cols) for _ in range(rows)]

        for col in range(cols):
            angle = player_angle - FOV/2 + FOV * col / cols
            dist = cast_ray(player_x, player_y, angle)
            wall_height = rows // int(dist if dist >= 1e-3 else 1)
            wall_height = max(1, min(rows-1, wall_height))
            shade = shade_chars[min(int(dist), len(shade_chars)-1)]
            top = max(0, rows//2 - wall_height//2)
            bottom = min(rows-1, rows//2 + wall_height//2)
            for row in range(rows):
                if top <= row <= bottom:
                    buffer[row][col] = shade
                elif row < rows//2:
                    buffer[row][col] = " "
                else:
                    buffer[row][col] = ",",

        # HUD
        fps = int(1.0 / max(1e-6, time.time() - last_time))
        last_time = time.time()
        hud = f"FPS:{fps} Pos:({player_x:.2f},{player_y:.2f}) Angle:{int(math.degrees(player_angle))%360}  Q to quit"
        if len(hud) < cols:
            for i, ch in enumerate(hud):
                buffer[0][i] = ch

        # clear and print
        os.system("cls")
        print("\n".join("".join(row) for row in buffer))

        # --- input handling (non-blocking)
        move = False
        # poll keys: arrow keys produce prefix then code
        while msvcrt.kbhit():
            ch = msvcrt.getwch()
            if ch == '\x00' or ch == '\xe0':  # special keys (arrows)
                key2 = msvcrt.getwch()
                if key2 == 'K':  # left
                    player_angle -= 0.1
                elif key2 == 'M':  # right
                    player_angle += 0.1
                elif key2 == 'H':  # up
                    nx = player_x + math.cos(player_angle) * 0.2
                    ny = player_y + math.sin(player_angle) * 0.2
                    if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                        player_x = nx; player_y = ny
                elif key2 == 'P':  # down
                    nx = player_x - math.cos(player_angle) * 0.2
                    ny = player_y - math.sin(player_angle) * 0.2
                    if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                        player_x = nx; player_y = ny
            else:
                # normal keys
                if ch.lower() == 'q':
                    return
                if ch.lower() == 'a':
                    player_angle -= 0.1
                if ch.lower() == 'd':
                    player_angle += 0.1
                if ch.lower() == 'w':
                    nx = player_x + math.cos(player_angle) * 0.2
                    ny = player_y + math.sin(player_angle) * 0.2
                    if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                        player_x = nx; player_y = ny
                if ch.lower() == 's':
                    nx = player_x - math.cos(player_angle) * 0.2
                    ny = player_y - math.sin(player_angle) * 0.2
                    if 0 <= int(ny) < H and 0 <= int(nx) < W and MAP[int(ny)][int(nx)] != "#":
                        player_x = nx; player_y = ny

        time.sleep(0.02)

# Entrypoint selects appropriate loop
if os.name == "nt":
    # Windows
    windows_loop()
else:
    # Unix-like: use curses
    try:
        import curses
        curses.wrapper(curses_loop)
    except Exception as e:
        print("Curses mode failed:", e)
        print("On Windows you can run this script without curses; otherwise install curses package or run in compatible terminal.")
