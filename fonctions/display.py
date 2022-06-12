# Copyright : romainflcht

MENU = """
╔════════════════════════════════════════════════════════════════╗
║                         Turing Machine                         ║
╠════════════════════════════════════════════════════════════════╣
║ This program is a reproduction of a Turing machine in Python.  ║
║                                                                ║
║ • How to use it ?                                              ║
║       - Put your program in the main.tur file, select          ║
║         'Set initial tape' put your initial input,             ║
║         press ENTER and the program will be executed.          ║
║                                                                ║
║ • Select an option :                                           ║
║       [1]. Set initial tape.                                   ║
║       [2]. See HELP section.                                   ║
║       [3]. exit.                                               ║
╚════════════════════════════════════════════════════════════════╝"""

HELP = """
╔════════════════════════════════════════════════════════════════╗
║                              HELP                              ║
╠════════════════════════════════════════════════════════════════╣
║ Every line has to be in the right format :                     ║
║ [state] [current symbol] [new symbol] [direction] [new state]  ║
║                                                                ║
║ • [state] and [new state] :                                    ║
║    - Can be anything (number and letter) but ';', '*' and ' '. ║
║    - To stop the program, use the halt state.                  ║
║                                                                ║
║ • [current symbol] and [new symbol] :                          ║
║    - use _ to read and write space.                            ║
║    - use * to read anything or write nothing.                  ║
║    - you can't use ;                                           ║
║                                                                ║
║ • [direction] :                                                ║
║    - use r to go right on the tape.                            ║
║    - use l to go left on the tape.                             ║
║    - use * to not move.                                        ║
║    - you can't use ;                                           ║
║                                                                ║
║ • You can use ; to put comment in your program.                ║
╚════════════════════════════════════════════════════════════════╝"""


def display_tape(tape: list) -> None:
    """
    Fonction that display correctly the tape.
    :param tape: tape that will be shown (list)
    :return: nothing.
    """
    for elt in tape:
        # Replace every _ by a space on print.
        if elt == '_':
            print(' ', end='')
        else:
            print(elt, end='')
    return


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
