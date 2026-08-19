import os
import pickle
from datetime import datetime, date
from log import Log

FILE = "todos_pickle.pkl"

def load_todos(FILE):
    if not os.path.exists(FILE):
        return []

    if not os.path.getsize(FILE) > 0:
        return []

    with open(FILE, "rb") as f:
        return pickle.load(f)


def view_todos(todos):
    if not todos:
        print(f"Todos not available!\n")
        return
    for i, record in enumerate(todos, start=1):
        print(f"Available todos: \n")
        print(f"{i} -> {record}")

def save_todos(todos, file):
    # deschidem fisierul
    with open(file, "wb") as f:
        pickle.dump(todos, f)


def remove_todo(file):
    while True:
        rm = input(f"Insert todo ID you want to remove: \n")
        rm = int(rm)
        if rm < 1 or rm > len(file):
            print(f"Todo ID for removal not in list!\n")
            continue
        break
    file.pop(rm - 1)
    print(f"You removed todo number: {rm}!\n")

def clear_todo(file):
    while True:
        answer = input(f"Are you sure you want to clear the todos list? - Y/N \n").upper()
        if not answer:
            print(f"Answer missing!\n")
            continue
        if answer not in ("Y", "N"):
            print(f"Invalid answer!\n")
            continue
        break
    if answer == "Y":
        file.clear()
        print(f"You cleared the todo list!\n")



def view_expiring(file, expiring_days=10):
    today = date.today()
    for todo in file:
        # convert to todo.date in date for day extraction
        initial = todo.date.date()
        expired = (today - initial).days
        if expired > expiring_days:
            print(f"Expired todo: {todo}\n")

def add_todo(file):
    while True:
        date = input(f"Insert todo date: \n")
        if not date:
            print(f"Date inexistent!\n")
            continue
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Invalid date format!")

    while True:
        todo = input(f"Insert todo: \n").lower()
        if not todo:
            print(f"Todo missing!\n")
            continue
        if todo.isdigit():
            print(f"Todo must contain letters!\n")
            continue
        break

    while True:
        description = input(f"Insert todo description: \n").lower()
        if not description:
            print(f"Description inexistent!\n")
            continue
        if description.isdigit():
            print(f"Description must contain letters!\n")
            continue
        break

    add_todo = Log(date, todo, description)
    file.append(add_todo)
    print(f"You added a new todo!\n")

def main():
    todos = load_todos(FILE)
    while True:
        answer = input(
            "What do you want to do next?\n"
            "(1) View todos\n"
            "(2) Remove todos\n"
            "(3) Add todo\n"
            "(4) Save todos\n"
            "(5) View expiring todos\n"
            "(6) Exit program\n"
        ).strip()

        if answer == "1":
            view_todos(todos)
        elif answer == "2":
            remove_todo(todos)
        elif answer == "3":
            add_todo(todos)
        elif answer == "4":
            save_todos(todos, "todos_pickle.pkl")
        elif answer == "5":
            view_expiring(todos)
        elif answer == "6":
            print(f"Disconnecting...\n")
            break
        else:
            print(f"Option out of range!\n")

if __name__ == "__main__":
    main()

