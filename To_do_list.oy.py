import os
task=[]
def save_task():
    with open("task.txt","w") as file:
        for j in task:
            file.write(j+"\n")
def load_task():
    if os.path.exists("task.txt"):
        with open("task.txt","r") as file:
            return[line.strip() for line in file.readlines()]
    return[]
task=load_task()
while True:
    print("Menu")
    print("1.Add")
    print("2.View Task")
    print("3.Mark task as done")
    print("4.Delete task")
    print("5.Exit")
    choice=int(input("Enter your choice(1-5): "))
    if choice==1:
        print("You chose to add a new task")
        task.append(input("Enter your task: "))
        print(f"Task {task} added successfully")
    elif choice==2:
        if task:
            print("\nYour Tasks")
            for i in task:
                print(task)
        else:
            print("\nNo task are available.Please add Task")
    elif choice==3:
        if task:
            task_num=int(input("Enter your task number: "))
            if 0<task_num<len(task):
                task[task_num]+="Done"
                print(f"Task {task [task_num]} marked done")
            else:
                print("Invalid Task number.Please try again")
        print("You chose to mark task as done")
    elif choice==4:
        if task:
            task_num=int(input("Enter your task number you want to delete: "))
            if 0<=task_num<len(task):
                removed_task=task.pop(task_num)
                print(f"Task {removed_task} removed successfully")
            else:
                print("Invalid Task number.Please try again")
        else:
            print("No task are available to delete.")
    elif choice==5:
        print("exiting the program!")
        break
    else:
        print("Invalid choice")
        print("Please try again")


