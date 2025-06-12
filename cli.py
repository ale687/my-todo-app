#from funciones import get_todos, write_todos
import funciones
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith("add"):
        todo = user_action[4:] 
        
        todos = funciones.get_todos()
        
        todos.append(todo + "\n")
        
        funciones.write_todos(todos)

    elif user_action.startswith("show"):
        
        todos = funciones.get_todos()
            
        for index, item in enumerate(todos):
            item = item.strip("\n")
            row=f"{index + 1}.{item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            
            number = number - 1
            
            todos = funciones.get_todos()
                
            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + "\n"
            
            funciones.write_todos(todos)
        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = funciones.get_todos()
            index = number - 1
            todo_remove = todos[index].strip("\n")
            todos.pop(index)
            
            funciones.write_todos(todos)

            message = f"todo {todo_remove} was removed from the list."
            print(message)    
        except IndexError:
            print("There is no item whit that number.")
            continue
        
    elif user_action.startswith("exit"):
        break
    else:
        print("command is not valid.")    
        
print("Bye")
    