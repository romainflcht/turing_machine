# Copyright : romainflcht

import os
import time
from fonctions.display import *


def state_execution(tape: list, cursor: int, states: dict, current_state: str, debug=False) -> tuple:
    """
    Fonction that execute the state that is passed in arguments.
    :param tape: tape used during the execution (list).
    :param cursor: cursor pointing to where the head is on the tape (int).
    :param states: every state that the program contain (dict).
    :param current_state: state that need to be executed (str)
    :param debug: write every action if set to True (bool).
    :return: the new cursor and the next state that need to be executed (tuple).
    """
    if debug:
        # Debug print.
        print('┌─ Started execute line : ──────────────────────────────────────────────')
        print(f'│ • [current_state] = {current_state}')
        print('│ • [tape] = [', end='')
        display_tape(tape)
        print(']\n│' + ' ' * 13 + ' ' * cursor + '↑')

    readed_value = '*'
    # Check if the cursor is in the right interval.
    if cursor < len(tape):
        # Read the tape value.
        readed_value = tape[cursor]

    # Check if there is a specific action to do with this read.
    if readed_value in states[current_state]:
        to_write, direction, next_state = states[current_state][readed_value]

    # Else execute the generic action.
    else:
        try:
            to_write, direction, next_state = states[current_state]['*']

        # Raison a SyntaxError because a case is missing in the main.tur file.
        except KeyError:
            raise SyntaxError(f'Missing case {readed_value} in the state {current_state}.')

    # Write the value if he has to.
    if to_write != '*':
        tape[cursor] = to_write

    # Change direction by updating the cursor if he has to.
    if direction != '*':
        if direction == 'r':
            cursor += 1

            # Add a new slot to the tape if the cursor go too far to the right.
            if cursor == len(tape):
                tape.append('_')

        elif direction == 'l':
            cursor -= 1

            # Add a new slot to the tape if the cursor go too far to the left.
            if cursor < 0:
                cursor = 0
                tape.insert(cursor, '_')
        else:
            # Raise a SyntaxError because a non autorized direction is in the main.tur file.
            raise SyntaxError(f'Bad direction ({direction}) in the state {current_state}.')

    if debug:
        # debug print.
        print(f'│ • [execute] Writing {to_write} at location {cursor} and go to {direction}')
        print('└─ Ended execute line ──────────────────────────────────────────────────', end='\n\n\n')
        time.sleep(.25)

    return cursor, next_state


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
