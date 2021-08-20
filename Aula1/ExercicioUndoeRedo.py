"""
    Make one to-do list with following options:
    Add tasks
    list tasks
    Undo option
    Redo option

"""

def show_list(to_do):
    print("To-do List")
    print(to_do)

def add_task(task, to_do):
    to_do.append(task)

def undo_list(to_do, redo):
    if not to_do:
        print("Nothing to undo")
        return

    last_to_do = to_do.pop()
    redo.append(last_to_do)

def redo_list(to_do, redo):
    if not redo:
        print("Nothing to redo")
        return

    redo_ls = redo.pop()
    to_do.append(redo_ls)

to_do = []
redo = []

while True:
    task = input("Add tasks or type undo, redo, ls: ")

    if task == 'ls':
        show_list(to_do)
        continue

    elif task == 'undo':
        undo_list(to_do, redo)
        continue

    elif task == 'redo':
        redo_list(to_do, redo)
        continue

    add_task(task, to_do)



