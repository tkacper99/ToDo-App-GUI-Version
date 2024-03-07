def get_todos():
    """
    Function that open file, and get content from it.
    :return: todos from file
    """
    with open('data.txt', 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg):
    """
    Function that upload content to external file
    :param todos_arg:
    """
    with open('data.txt', "w") as file:
        file.writelines(todos_arg)
