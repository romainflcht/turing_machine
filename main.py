# Copyright : romainflcht

from fonctions.file_parsing import *
from fonctions.instruction_processing import *
from fonctions.tape_init import *

FILE_PATH = 'main.tur'
FIRST_STATE_NAME = '0'


if __name__ == '__main__':
    is_running = True
    current_state = FIRST_STATE_NAME
    tape = tape_init(input('coucou >'))
    cursor = 0

    parsed_program = read_and_parse(FILE_PATH)
    states = separate_states(parsed_program)

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
