# Copyright : romainflcht

from file_parsing.file_parsing import *
from instruction_processing.instruction_processing import *

FILE_PATH = 'main.tur'

tape = [elt for elt in '110110_101011']
cursor = 0
current_state = '0'
is_running = True


if __name__ == '__main__':
    parsed_program = read_and_parse(FILE_PATH)
    states = separate_states(parsed_program)
    print(states)

    while is_running:
        cursor, next_state = execute_line(tape, cursor, states, current_state, False)

        if next_state == 'halt':
            is_running = False

        else:
            current_state = next_state

    for elt in tape:
        if elt == '_':
            print(' ', end='')
        else:
            print(elt, end='')
