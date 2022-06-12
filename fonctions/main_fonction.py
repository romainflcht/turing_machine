# Copyright : romainflcht

from fonctions.file_parsing import *
from fonctions.instruction_processing import *
from fonctions.tape_init import *
from fonctions.display import *

DEBUG = False


def main(file_path, first_state_name) -> None:
    """
    Main fonction of the project.
    :param file_path: Path of the main.tur file (str).
    :param first_state_name: name of the first state that will be executed (str).
    :return: nothing.
    """

    # Initialisation of the tape, cursor and the current state.
    tape = []
    cursor = 0
    current_state = first_state_name
    is_running = False

    # Printing the WELCOME menu and wait for the user input.
    print(MENU)
    while not is_running:
        user_input = input('• Enter your selection HERE : ')

        if user_input == '1':
            # Run the main.tur file.

            tape = tape_init(input('• [✔] Enter you initial tape HERE : '))
            print(' • [~] Execution started.')
            is_running = True

        elif user_input == '2':
            # Show the HELP section.
            print(HELP)

        else:
            # Exit the program.
            print('\nGoodbye :)')
            exit(0)

    # Parse the program.
    parsed_program = read_and_parse(file_path)
    states = separate_states(parsed_program)

    while is_running:
        # Execute the current_state.
        cursor, next_state = state_execution(tape, cursor, states, current_state, debug=DEBUG)

        # Check if the next state is halt, halt-accept or halt-reject.
        if next_state in ('halt', 'halt-accept', 'halt-reject'):
            # Stop running.
            is_running = False

        else:
            # Update the current state.
            current_state = next_state

    # Show the result.
    print(' • [✔] Execution done.', end='\n\n')
    print('Result tape : ', end='')
    display_tape(tape)

    # Exit the program.
    print('\nGoodbye :)')


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
