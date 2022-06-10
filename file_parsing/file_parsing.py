import os


def read_and_parse(file_path: str) -> tuple:
    """
    Read file and parse every line by removing \n and empty line.
    :param file_path: path to the main.tur file.
    :return: list that contain every parsed line of code.
    """
    parsed_program = []
    if os.path.isfile(file_path):

        with open(file_path, 'r') as program_file:
            raw_program = program_file.readlines()

        for line in raw_program:
            if line != '\n':
                parsed_line = line.rstrip().split(' ')
                # print(parsed_line)

                if len(parsed_line) == 5:
                    parsed_program.append(parsed_line)

        first_line = parsed_program[0]

    else:
        return ()
    return parsed_program, first_line


def separate_states(parsed_program: list) -> dict:
    """
    Separate each part of states written in the main.tur file.
    :param parsed_program: parsed data from the fonction 'read_and_parse'.
    :return: Dict that contains every state with their lines.
    """
    dict_programs = {}

    for line in parsed_program:
        state = line[0]
        symbol = line[1]

        if not dict_programs.get(state):
            dict_programs[state] = {symbol: line[2:]}

        else:
            dict_programs[state][symbol] = line[2:]

    return dict_programs


if __name__ == '__main__':
    print(f'{__file__} not executable')
