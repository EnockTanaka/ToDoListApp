# TODO List Terminal App

## Overview

This is a simple command-line based **TODO list application** that allows users to manage their tasks.
The application supports user authentication through a basic **login and logout system**, and stores 
all user information and tasks in text files.

## Features

- **User Authentication:**
  - Users can log in and log out.
  - User credentials are stored in text files.
- **Task Management:**
  - Users can add, view, edit, and delete tasks.
  - Tasks are stored in text files specific to each user.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```
    git clone git@github.com:EnockTanaka/ToDoListApp.git
    ```

2. Navigate to the project directory:

    ```
    cd todo-list-terminal-app
    ```

### Usage

1. Run the application:

    ```
    python todo.py
    ```

2. Follow the on-screen prompts to log in or create a new user.
3. After logging in, you can add, view, edit, and delete tasks using the menu options.

### Example

  ```
  $ python todo.py
  Welcome to the TODO List App!
  1. Log in
  2. Create a new user
  3. Exit
  Enter your choice: 1
  
  Username: Tanaka
  Password: ****
  
  Welcome, Tanaka!
  1. Add a new task
  2. View all tasks
  3. Edit a task
  4. Delete a task
  5. Log out
  Enter your choice: 1
  
  Enter the task description: Buy groceries
  Task added successfully!
  ```

## Future Improvements

- **Encryption:** Securely store user credentials and task data using encryption.
- **Improved Task Management:**
  - Add due dates and priorities to tasks.
  - Implement categories or tags for better task organization.
  - Allow users to set reminders for tasks.
- **User Interface Enhancements:**
  - Develop a graphical user interface (GUI) for a more user-friendly experience.
  - Improve the command-line interface with better formatting and color coding.
- **Data Management:**
  - Implement a database (e.g., SQLite, PostgreSQL) for more efficient data storage and retrieval.
  - Allow data import/export in different formats (e.g., CSV, JSON).
- **Collaboration Features:**
  - Enable sharing of task lists between users.
  - Implement collaborative task editing and tracking.
- **Cross-Platform Compatibility:**
  - Develop mobile and web versions of the app.
- **Integration with Other Services:**
  - Sync tasks with calendar applications (e.g., Google Calendar).
  - Integrate with productivity tools (e.g., Trello, Asana).

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## Contact

For questions or issues, please open an issue in this repository or contact [mukwindidza04@gmail.com].


