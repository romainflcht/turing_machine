from file_parsing.file_parsing import *

FILE_PATH = 'main.tur'
tape = ['0', '1', '_', '_', '_', '1', '_']
cursor = 0
current_state = '0'
is_running = True


def execute_line(tape: list, cursor: int, states: dict, current_state: str):
    print('Started execute line -----------------------------------------')
    print(f'actual cursor {cursor}')
    print(tape)
    print(f'current state: {current_state}')

    readed_value = '*'
    if cursor < len(tape):
        readed_value = tape[cursor]

    to_write, direction, next_state = states[current_state][readed_value]
    if to_write != '*':
        tape[cursor] = to_write

    if direction != '*':
        if direction == 'r':
            cursor += 1
        elif direction == 'l':
            cursor -= 1
        else:
            raise Exception(f'Bad direction : {direction}')
    print('after exec')
    print(tape)
    print(f'Next cursor {cursor}')
    print(f'Next state {next_state}')
    print('Ended execute line -----------------------------------------', end='\n\n\n')
    return cursor, next_state




if __name__ == '__main__':
    parsed_program, first_line = read_and_parse(FILE_PATH)
    states = separate_states(parsed_program)
    print(states)

    while is_running:
        cursor, next_state = execute_line(tape, cursor, states, current_state)

        if next_state == 'halt':
            is_running = False

        else:
            current_state = next_state

    print(is_running)
    # print(states)

