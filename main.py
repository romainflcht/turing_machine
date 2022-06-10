from file_parsing.file_parsing import *
from instruction_processing.instruction_processing import *

FILE_PATH = 'main.tur'
# tape = ['0', '1', '_', '_', '_', '1', '_']
# tape = ['1', '0', '0', '1', '0', '0', '1', ]
tape = [elt for elt in '1101_11010']
cursor = 0
current_state = '0'
is_running = True


if __name__ == '__main__':
    parsed_program, first_line = read_and_parse(FILE_PATH)
    states = separate_states(parsed_program)
    print(states)
    """for key in states:
        print(f'State : {key}')
        print(f'\tnb_line : {len(states[key].items())}')

        print()"""

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
    # print(states)

