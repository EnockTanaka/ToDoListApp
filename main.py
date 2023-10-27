"""
displaying a menu to the user with options such as:

Add a task
View tasks
Mark task as done
Remove task
Quit

"""
class ToDoList:
    def __init__(self) -> None:
        self.tasks = []

    def main_menu(self):
        """
        Displays the menu to the user.
        """
        print("Good day! Choose an option from the menu below:\n")

        menu_options = {
            "1": "Add a task",
            "2": "View tasks",
            "3": "Mark task as done",
            "4": "Remove task",
            "5": "Quit"
        }

        for key, value in menu_options.items():
            print(f"{key}. {value}")

        option = input("\nEnter an option: ")
        print()

        if option == '1':
            print( menu_options[option])
            print(self.add_task())

        elif option == '2':
            print( menu_options[option])
            print(self.view_tasks())

        elif option == '3':
            print( menu_options[option])
            return self.mark_task_as_done()

        elif option == '4':
            print( menu_options[option])
            return self.remove_task()

        elif option == '5':
            print( menu_options[option])
            return quit()

        else:
            print("Invalid option\n")
            return self.main_menu()

    def add_task(self):
        """
        Adds a task to the list.
        """
        print("Enter your Tasks and if you have finished enter 'done'")
        while True:

            task = input("Enter a task: ").strip()

            try:
                if task.lower() == "done":
                    print("Your Tasks have been added and to view them go to main menu option 2")
                    print(self.tasks)
                    return self.main_menu()
                self.tasks.append(task)

            except EOFError:
                print("You have exited you Add task")
                exit()


    def view_tasks(self):
        """
        Displays the tasks in the list.
        """
        print("Here are your tasks:")
        print(self.tasks)
        return self.main_menu()

    def mark_task_as_done(self):
        """
        Marks a task as done.
        """
        print("Here are your tasks:")
        print()
        return

    def remove_task(self):
        """
        Removes a task from the list.
        """
        print("Here are your tasks:")
        print()
        return

    def quit_app(self):
        """
        Quits the app.
        """
        print("Goodbye!")
        return


if __name__ == "__main__":
    todo  = ToDoList()
    todo.main_menu()

