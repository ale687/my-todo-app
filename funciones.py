FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Leer in archivo de texto y devolver la lista de
    tareas pendientes.
    """
    with open(filepath,"r") as file_local:
        return [line.strip() for line in file_local.readlines()]
 
 
def write_todos(todos_arg , filepath=FILEPATH):
    """ Escribe en la lista de tareas pendientes en el archivo de texto."""
    with open(filepath, "w") as file:
            file.writelines([todo + "\n" for todo in todos_arg])
 
 
if __name__ == "__main__":
    print("Hello fron funciones")
    print(get_todos())
     