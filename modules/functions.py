def get_todos(filepath):
    """ reads file and returns list """
    with open(filepath, 'r') as file:
        tasks_local = file.readlines()
    return tasks_local
#print(help(get_todos)) documenting code
def write_todos(filepath, new_task):
    """ writes task in text file """
    with open(filepath,'w') as file:
        file.writelines(new_task)
if __name__ == '__main__':
    print(__name__)
    print('hi')