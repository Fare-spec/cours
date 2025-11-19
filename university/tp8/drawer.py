import time as tm
import turtle as tl

import board as bd

screen = tl.Screen()
screen.setup(width=800, height=600)
screen.tracer(0, 0)


def draw_board(board: bd.Grid):
    tl.clear()  # instead of resetscreen()
    tl.hideturtle()
    tl.penup()

    if not board:
        screen.update()
        return

    cell_size = 60

    rows = len(board)
    cols = max(len(line) for line in board)

    origin_x = -cols * cell_size / 2
    origin_y = rows * cell_size / 2

    for i, line in enumerate(board):
        for j, cell in enumerate(line):
            x = origin_x + j * cell_size
            y = origin_y - i * cell_size

            tl.goto(x, y)
            tl.pendown()
            for _ in range(4):
                tl.forward(cell_size)
                tl.right(90)
            tl.penup()

            tl.goto(x + cell_size / 2, y - 0.8 * cell_size)
            tl.write(
                cell, align="center", font=("Courier", int(cell_size / 2), "normal")
            )

    screen.update()
    tm.sleep(100)
