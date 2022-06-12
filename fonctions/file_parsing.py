# Copyright : romainflcht

import os


def read_and_parse(file_path: str) -> list:
    """
    Read file and parse every line by removing \n, empty line and comment.
    :param file_path: path to the main.tur file (str).
    :return: list that contain every parsed line of code.
    """
    parsed_program = []

    # Check if the file exist.
    if os.path.isfile(file_path):
        with open(file_path, 'r') as program_file:
            raw_program = program_file.readlines()

        for index_line in range(len(raw_program)):
            # Removing evry comment in the file.
            if ';' in raw_program[index_line]:
                semicolon_index = raw_program[index_line].index(';')
                line = raw_program[index_line][:semicolon_index]

            else:
                line = raw_program[index_line][:]

            # Check if the line is not empty.
            if line not in ('\n', ''):
                # Remove any \n and split line between every space.
                parsed_line = line.replace('\n', '').split(' ')
                len_parsed_line = len(parsed_line)

                # Check if the line is in the right format.
                if len_parsed_line == 5:
                    parsed_program.append(parsed_line)

                elif len_parsed_line > 5:
                    if parsed_line[5] == '':
                        parsed_program.append(parsed_line[:5])

                    else:
                        # Raise format error
                        raise SyntaxError(f'in {file_path} at line {index_line + 1}.')
                else:
                    # Raise format error
                    raise SyntaxError(f'in {file_path} at line {index_line + 1}.')
    else:
        raise FileNotFoundError(f'{file_path} don\'t exist')
    return parsed_program


def separate_states(parsed_program: list) -> dict:
    """
    Separate each part of states written in the main.tur file.
    :param parsed_program: parsed data from the fonction 'read_and_parse' (list).
    :return: dict that contains every state with their lines.
    """
    dict_programs = {}

    for line in parsed_program:
        # Get state and symbol that the line read on tape.
        state = line[0]
        symbol = line[1]

        # Create a dictionnary for every symbol that every state has to read.
        if not dict_programs.get(state):
            dict_programs[state] = {symbol: line[2:]}

        else:
            dict_programs[state][symbol] = line[2:]
    return dict_programs


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
