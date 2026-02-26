import os
import math
import time
import sys
import shutil

# Platform detection
WINDOWS = os.name == "nt"
if WINDOWS:
    import msvcrt
else:
    import termios, tty, select

# Player state
player_x = 3.0
player_y = 3.0
player_angle = 0.0

FOV = math.pi / 3
DEPTH = 20
SPEED = 4.0

MAP = [
    "################",
    "#..............#",
    "#..####........#",
    "#..............#",
    "#......####....#",
    "#..............#",
    "#..............#",
    "################"
]

MAP_W = len(MAP[0])
MAP_H = len(MAP)

shade = " .:-=+*#%@"

def clear():
    os.system("cls" if WINDOWS else "clear")

def get_screen_size():
    cols, rows = shutil.get_terminal_size()
    return cols, rows

def is_wall(x, y):
    if x < 0 or x >= MAP_W or y < 0 or y >= MAP_H:
        return True
    return MAP[int(y)][int(x)] == "#"

def get_key():
    if WINDOWS:
        if msvcrt.kbhit():
            return msvcrt.getwch()
        return None
    else:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            return sys.stdin.read(1)
        return None

def try_move(dx, dy):
    """Attempt to move player by dx,dy but block if new position is inside a wall."""
    global player_x, player_y
    new_x = player_x + dx
    new_y = player_y + dy
    # small padding to avoid hugging walls
    padding = 0.25
    # check four surrounding sample points
    samples = [(new_x + sx*padding, new_y + sy*padding) for sx,sy in ((0,0),(1,0),(0,1),(-1,0),(0,-1))]
    for sx, sy in samples:
        if is_wall(sx, sy):
            return False
    player_x = new_x
    player_y = new_y
    return True

def render():
    cols, rows = get_screen_size()
    # Keep a minimum resolution to avoid zero/very small terminal sizes
    cols = max(20, cols)
    rows = max(10, rows)
    screen = [list(" " * cols) for _ in range(rows)]

    half_rows = rows // 2

    # sky / floor fill
    for r in range(half_rows):
        for c in range(cols):
            screen[r][c] = " "
    for r in range(half_rows, rows):
        for c in range(cols):
            screen[r][c] = "."

    # cast a ray per column
    for col in range(cols):
        ray_angle = (player_angle - FOV/2) + (col / float(cols)) * FOV
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        distance = 0.0
        hit = False
        step = 0.05  # smaller step = higher resolution but slower
        max_depth = DEPTH

        while not hit and distance < max_depth:
            distance += step
            test_x = player_x + cos_a * distance
            test_y = player_y + sin_a * distance
            if is_wall(test_x, test_y):
                hit = True

        if not hit:
            # nothing hit: leave sky/floor as is
            continue

        # correct fish-eye by projecting distance onto view direction
        # (optional basic correction)
        eye_dir = player_angle
        corrected_dist = distance * math.cos(ray_angle - eye_dir)
        if corrected_dist <= 0.001:
            corrected_dist = 0.001

        # determine wall slice height
        wall_height = int(rows / corrected_dist)
        wall_height = max(1, min(rows-1, wall_height))

        # shading based on distance
        shade_idx = int((corrected_dist / max_depth) * (len(shade)-1))
        shade_idx = min(len(shade)-1, max(0, shade_idx))
        wall_char = shade[shade_idx]

        top = max(0, half_rows - wall_height // 2)
        bottom = min(rows-1, half_rows + wall_height // 2)

        for r in range(top, bottom+1):
            screen[r][col] = wall_char

    # compose output
    out_lines = ["".join(row) for row in screen]
    clear()
    # show simple HUD
    fps = f"FPS: {int(1.0/max(1e-6, global_fps()))}"
    pos = f"Pos: ({player_x:.2f},{player_y:.2f}) Ang: {math.degrees(player_angle)%360:.0f}°"
    controls = "W/S forward/back  Q/E strafe  A/D turn  ESC quit"
    try:
        # put HUD on first line and controls on second if space allows
        if rows >= 3:
            out_lines[0] = f"{fps}  {pos}".ljust(cols)[:cols]
            out_lines[1] = controls.ljust(cols)[:cols]
    except:
        pass
    print("\n".join(out_lines))

# helper to get a smoothed instantaneous fps estimate via globalClock-like logic
_last_time = time.time()
_frame_dt = 1/60.0
def global_fps():
    global _last_time, _frame_dt
    now = time.time()
    dt = now - _last_time
    _last_time = now
    _frame_dt = _frame_dt * 0.9 + dt * 0.1
    return max(1e-6, 1.0 / _frame_dt)

def main():
    global player_x, player_y, player_angle

    last = time.time()

    while True:
        now = time.time()
        dt = now - last
        last = now

        key = get_key()
        if key:
            # Normalize Windows single-letter returns and special keys
            if key == '\x1b':  # ESC
                break
            if key.lower() == "w":
                dx = math.cos(player_angle) * SPEED * dt
                dy = math.sin(player_angle) * SPEED * dt
                try_move(dx, dy)
            elif key.lower() == "s":
                dx = -math.cos(player_angle) * SPEED * dt
                dy = -math.sin(player_angle) * SPEED * dt
                try_move(dx, dy)
            elif key.lower() == "a":
                player_angle -= 1.5 * dt
            elif key.lower() == "d":
                player_angle += 1.5 * dt
            elif key.lower() == "q":
                # strafe left
                dx = -math.sin(player_angle) * SPEED * dt
                dy =  math.cos(player_angle) * SPEED * dt
                try_move(dx, dy)
            elif key.lower() == "e":
                # strafe right
                dx = math.sin(player_angle) * SPEED * dt
                dy = -math.cos(player_angle) * SPEED * dt
                try_move(dx, dy)
            elif key.lower() == "r":
                # instant respawn to safe location
                player_x, player_y = 3.0, 3.0

        render()

if __name__ == "__main__":
    # Unix raw mode only
    if not WINDOWS:
        old_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin)
    try:
        main()
    finally:
        if not WINDOWS:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)
