import curses
import numpy as np


def map_input_to_numbers():
    pass


def draw_line(line_num, np_arr, stdscr):

    def itoc(digit):
        if digit == 0:
            return " "
        return str(digit)

    elems = [
            "║", itoc(np_arr[0]), "│", itoc(np_arr[1]), "│", itoc(np_arr[2]),
            "║", itoc(np_arr[3]), "│", itoc(np_arr[4]), "│", itoc(np_arr[5]),
            "║", itoc(np_arr[6]), "│", itoc(np_arr[7]), "│", itoc(np_arr[8]),
            "║"
            ]

    line = " ".join(elems)

    stdscr.addstr(line_num, 0, line)


def draw_board(stdscr, numbers):

    stdscr.addstr(0,0, "╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

    draw_line(1, numbers[0], stdscr)

    stdscr.addstr(2,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(3, numbers[1], stdscr)

    stdscr.addstr(4,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(5, numbers[2], stdscr)

    stdscr.addstr(6,0, "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")

    draw_line(7, numbers[3], stdscr)

    stdscr.addstr(8,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(9, numbers[4], stdscr)

    stdscr.addstr(10,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(11, numbers[5], stdscr)

    stdscr.addstr(12,0, "╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")

    draw_line(13, numbers[6], stdscr)

    stdscr.addstr(14,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(15, numbers[7], stdscr)

    stdscr.addstr(16,0, "╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    draw_line(17, numbers[8], stdscr)

    try:
        stdscr.addstr(18,0, "╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
    except curses.error:
        pass


def draw_menu(stdscr):

    # Resize to sudoku board dimensions
    stdscr.resize(19,37)

    k = 0
    cursor_x = 0
    cursor_y = 0
    
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Loop where k is the last character pressed
    while (k != ord('q')): # TODO: add Esc as the exit char

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k in range(49, 59): # 1 - 9 in ASCII
            if cursor_x in range(2, 35, 4) and cursor_y % 2 != 0: # checks if cursor is over a digit
                num_x = (cursor_x - 2) // 4
                num_y = (cursor_y - 1) // 2

                numbers[num_y, num_x] = k - 48

        draw_board(stdscr, numbers)

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()


def main():
    curses.wrapper(draw_menu)


if __name__ == "__main__":

    hard_example = [
            [1,2,2],
            [2,4,6], [2,9,3],
            [3,2,7], [3,3,4], [3,5,8],
            [4,6,3], [4,9,2],
            [5,2,8], [5,5,4], [5,8,1],
            [6,1,6], [6,4,5],
            [7,5,1], [7,7,7], [7,8,8],
            [8,1,5], [8,6,9],
            [9,8,4],
            ]

    # correct for 0 indexing
    for i in range(len(hard_example)):
        hard_example[i][0] -= 1
        hard_example[i][1] -= 1

    # create sudoku 9 * 9
    numbers = np.zeros((9,9), dtype=np.int8)
    for i in hard_example:
        numbers[i[0],i[1]] = i[2]

    main()
