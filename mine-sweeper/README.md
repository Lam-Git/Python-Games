Minesweeper:

Check out the tutorial here: https://youtu.be/Fjw7Lc9zlyU

This is a Python implementation of 2-D Minesweeper!

(If you do not edit the parameters in the script, the script will automatically initialize it to a 10x10 board, with 10 bombs)
For now, this script does not have a GUI and you can use terminal.

In order to "dig" at a certain location, you type in the index of the row, then the column, separated by a comma (whitespace optional). The game "digs" recursively around that location if there are no bombs nearby.

You can continue digging until either you hit a bomb (which is game over) or you've successfully dug up all n-b non-bomb locations (which is victory)

The Rules:

Row, Col

0 = no bombs near by
1=
