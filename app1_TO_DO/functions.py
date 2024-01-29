FILEPATH = "todos.txt"

def get_todos(filepath= FILEPATH):
    """ Read a text file and return the list of to-do items.  """
    with open(filepath , 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(local_todos, filepath = FILEPATH):
    """ write in a text file the list of to-do items. """
    with open(filepath, 'w') as file_local:
            file_local.writelines(local_todos)