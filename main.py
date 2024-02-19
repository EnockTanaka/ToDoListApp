import getpass

class ToDoList:
    def __init__(self, file = None, user_file = None) -> None:

        self.file_path = file or 'tasks.txt'
        self.user_file_path = user_file or 'users.txt'
        self.username = None
        self.file = None
        self.tasks = []
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open(self.user_file_path, 'r') as user_file:
                for line in user_file:
                    username, password = line.strip().split(',')
                    self.users[username] = password
        except FileNotFoundError:
            pass

    def save_users(self):
        with open(self.user_file_path, 'w') as user_file:
            for username, password in self.users.items():
                user_file.write(f"{username},{password}\n")

    def register(self):
        print("Register a new user:")
        username = input("Enter your username: ")

        while True:
            password = getpass.getpass("Enter your password: ")
            confirm_password = getpass.getpass("Confirm your password: ")

            if password == confirm_password:
                self.users[username] = password
                self.save_users()
                print("Registration successful!")
                break
            else:
                print("Passwords do not match. Please try again.")

    def login(self):
        print("Login:")
        print()
        username = input("Enter your username: ")

        if username in self.users:
            password = getpass.getpass("Enter your password: ")

            if password == self.users[username]:
                self.username = username
                self.file_path = f"{self.username}_tasks.txt"
                self.load_tasks()
                print(f"Welcome, {username}!\n")
            else:
                print("Incorrect password. Please try again.\n")
                self.login()
        else:
            print("User not found. Please register.\n")
            self.main_menu()

    def load_tasks(self):
        try:
            with open(self.file_path, 'r') as file:
                self.tasks = [line.strip() for line in file]
        except FileNotFoundError:
            pass

    def main_menu(self):
        """
        Displays the menu to the user.
        """

        print(" > Please choose an option: \n ")

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
            self.add_task()

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
                    self.update_tasks()
                    self.main_menu()

                self.tasks.append(task)

            except EOFError:
                print("You have exited your Add task")
                exit()

    def update_tasks(self):
        '''Save items in task to a file'''
        with open(self.file_path, 'w') as file:
            print(self.tasks)
            for line in self.tasks:
                file.write(f"{line}\n")

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
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

        task_index = input("Enter the number of the task you want to mark as done (or type 'cancel' to go back): ")

        if task_index.lower() == 'cancel':
            return self.main_menu()

        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                self.tasks[task_index - 1] += " - Done"
                print(f"Task {task_index} marked as done.")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        self.update_tasks()
        return self.main_menu()

    def remove_task(self):
        """
        Removes a task from the list and the text file.
        """
        print("Here are your tasks:")
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. {task}")

        task_index = input("Enter the number of the task you want to remove (or type 'cancel' to go back): ")

        if task_index.lower() == 'cancel':
            return self.main_menu()

        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                print(f"Task {task_index} removed: {removed_task}")
            else:
                print("Invalid task number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

        self.update_tasks()
        return self.main_menu()

    def quit_app(self):
        """
        Quits the app.
        """
        print("Goodbye!")
        return

if __name__ == "__main__":
    todo = ToDoList()
    todo.load_users()

    while True:
        print("\nGood day! Choose an option from the menu below:")
        print("1. Register")
        print("2. Login")
        print("3. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            todo.register()
        elif choice == '2':
            todo.login()
            todo.main_menu()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

