import curses

COLOR_MENU_BG = 21
COLOR_DESKTOP_BG = 22

CP_MENU_NORMAL = 21
CP_MENU_HL = 22
CP_DESKTOP_NORMAL = 23

State = {}

def init(win):
    rows, cols = win.getmaxyx()
    State['rows'] = rows
    State['cols'] = cols

    curses.init_color(COLOR_MENU_BG, 894, 894, 894)
    curses.init_color(COLOR_DESKTOP_BG, 699, 812, 921)

    curses.init_pair(CP_MENU_NORMAL, curses.COLOR_BLACK, COLOR_MENU_BG)
    curses.init_pair(CP_MENU_HL, curses.COLOR_RED, COLOR_MENU_BG)
    curses.init_pair(CP_DESKTOP_NORMAL, curses.COLOR_BLACK, COLOR_DESKTOP_BG)

def draw_menu(win, text):
    w = State['cols']
    padded_text = text.ljust(w)
    win.addstr(0, 0, padded_text, curses.color_pair(CP_MENU_NORMAL))

def draw_status(win, text):
    w = State['cols']
    r = State['rows']
    padded_text = text.ljust(w - 1)
    win.addstr(r-1, 0, padded_text, curses.color_pair(CP_MENU_NORMAL))

def draw_desktop(win):
    w = State['cols']
    r = State['rows']
    for i in range(1, r - 1):
        padded_text = ' '.ljust(w - 1)
        win.addstr(i , 0, padded_text, curses.color_pair(CP_DESKTOP_NORMAL))

def main(stdscr: curses.window):
    init(stdscr)
    stdscr.clear()
    draw_menu(stdscr, 'Sample menu')
    draw_desktop(stdscr)
    # stdscr.addstr(1, 0, f'first line {curses.has_colors()}')
    stdscr.addstr(2, 0, f'second line {curses.COLORS}', curses.color_pair(1))
    stdscr.addstr(f'third line {curses.can_change_color()}')
    draw_status(stdscr, 'Sample Status')
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)