# Copyright : romainflcht

def tape_init(user_input: str) -> list:
    """
    Fonction that create a tape with what user write into the console.
    :param user_input: String that contain user input.
    :return: List that is the initialised tape.
    """

    # Semicolon not supported as value to read on tape.
    user_input = user_input.replace(';', '')

    # Switch every space to '_'.
    user_input = user_input.replace(' ', '_')
    initialised_tape = [elt for elt in user_input]

    return initialised_tape


if __name__ == '__main__':
    print('This script is not supposed to be executed alone, import it to use it.')
