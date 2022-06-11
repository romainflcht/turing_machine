# Copyright : romainflcht

import time


def execute_line(tape: list, cursor: int, states: dict, current_state: str, debug: bool):
    if debug:
        print('• Started execute line : ')
        print(f'• [current_state] = {current_state}')
        print('  ' + '     ' * cursor + '↓')
        print(f'{tape}', end='\n\n')

    readed_value = '*'
    if cursor < len(tape):
        readed_value = tape[cursor]

    if readed_value in states[current_state]:
        to_write, direction, next_state = states[current_state][readed_value]
    else:
        to_write, direction, next_state = states[current_state]['*']

    if to_write != '*':
        tape[cursor] = to_write

    if direction != '*':
        if direction == 'r':
            cursor += 1
            if cursor == len(tape):
                tape.append('_')
        elif direction == 'l':
            cursor -= 1
            if cursor < 0:
                cursor = 0
                tape.insert(cursor, '_')
        else:
            raise Exception(f'Bad direction : {direction}')

    if debug:
        print(f'\t• [to_write] = {to_write}')
        print(f'\t• [direction] = {to_write}', end='\n\n')

        print('~ Execution Done !')
        print(tape)
        print('  ' + '     ' * cursor + '↑')
        print(f'• [next_state] = {next_state}')
        print('Ended execute line -----------------------------------------', end='\n\n\n')
        time.sleep(.25)

    return cursor, next_state


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
