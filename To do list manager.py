import os

filename = "my_todo_list.txt"

def read_file():
    
    if not os.path.exists(filename):
        return []
    
    
    with open(filename, "r") as f:
        data = f.read().splitlines()
    return data

def write_file(items):
    with open(filename, "w") as f:
        for i in items:
            f.write(i + "\n")

def display(items):
    print("\n--- Current List ---")
    
    for i in range(len(items)):
        print(str(i + 1) + ". " + items[i])
    print("--------------------")

def main():
    
    todo_items = read_file()

    while True:
        print("\n1. View")
        print("2. Add")
        print("3. Remove")
        print("4. Exit")
        
        user_input = input("Enter choice: ")

        if user_input == "1":
            display(todo_items)

        elif user_input == "2":
            new_item = input("Enter task name: ")
            todo_items.append(new_item)
            write_file(todo_items)
            print("Saved.")

        elif user_input == "3":
            display(todo_items)
            
            try:
                idx = int(input("Enter number to delete: "))
                
                del todo_items[idx - 1]
                write_file(todo_items)
                print("Deleted.")
            except:
                print("Error: Invalid index.")

        elif user_input == "4":
            break
        
        else:
            print("Invalid option.")

main()


