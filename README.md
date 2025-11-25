# To-Do List Manager – README

A simple command-line To-Do List Manager written in Python that allows users to view, add, and remove tasks stored in a text file on the local system.  The project is designed as a small but complete CLI application demonstrating basic file handling, modular design, and interactive menus in Python.

## Overview

This project provides a minimal task management system that runs entirely in the terminal.  Users interact with a numbered menu to perform operations on their to‑do list, which is persisted in a plain text file so that tasks remain available between sessions.  The codebase is intentionally simple to serve as a starting point for students learning Python programming concepts such as functions, loops, conditionals, and basic error handling.

Key capabilities include:
- Loading existing tasks from a text file at startup.
- Displaying the current list of tasks with index numbers.
- Adding new tasks entered by the user.
- Removing tasks by selecting their index from the displayed list.

## Features

The core features implemented in this project are:

- Persistent storage:
  - Tasks are stored in a file named `mytodolist.txt` in the working directory.
  - On startup, the program checks if this file exists and loads all existing tasks line by line.

- Interactive menu-driven CLI:
  - A simple text menu offers options to view tasks, add tasks, remove tasks, or exit the application.
  - User input is read from standard input using the `input()` function and handled in a loop until the user chooses to exit.

- Task viewing:
  - Tasks are printed with serial numbers starting from 1 for easy selection and reference.
  - A header and footer are displayed around the list to separate it from other console output.

- Task addition:
  - The user enters a short text description for each new task.
  - The new task is appended to the in-memory list and then written back to the file for persistence.

- Task removal:
  - The application first displays the current list of tasks with indices.
  - The user is prompted to enter the number corresponding to the task to delete, and the entry is removed from the list and saved to the file.

- Basic error handling:
  - If the user enters an invalid index when removing a task, an error message is displayed instead of crashing.
  - If the data file does not exist when the program starts, an empty list is used and a new file is created on write.

## Project Structure

The project has a very simple structure suitable for an introductory Python CLI project.

- `To-do-list-manager.py`  
  Main Python script that contains:
  - Global configuration for the data file name.
  - Functions for reading from and writing to the task file.
  - A function to display the current list of tasks.
  - The `main()` function implementing the menu loop and user interaction.

- `mytodolist.txt` (auto-created)  
  - Plain text file storing one task per line.
  - Created automatically when the user adds the first task if it does not already exist.

This simple structure matches typical patterns for small command-line utilities, where a single script coordinates reading data, updating it, and printing results to the console.

## Installation

The application only requires Python and the standard library, making it easy to set up on any system with Python installed.

Steps:

1) Install Python (if not already installed):
- Ensure Python 3.x is installed on your machine.
- On most systems, `python --version` or `python3 --version` in a terminal will show the installed version.

2) Download project files:
- Place `To-do-list-manager.py` into a folder of your choice.
- You do not need to create `mytodolist.txt` manually; the script will create it when writing tasks.

3) (Optional) Create a virtual environment:
- For a clean environment, you can create and activate a virtual environment using the standard `venv` module.
- This is optional because the script only uses the Python standard library and does not require external packages.

## Usage

The application is run from the command line and interacts with the user through prompts.

1) Open a terminal or command prompt.
2) Navigate to the folder containing `To-do-list-manager.py`.
3) Run the script:
- On many systems: `python To-do-list-manager.py`  
- On some systems: `python3 To-do-list-manager.py`

After starting, the program will:
- Load existing tasks (if any) from `mytodolist.txt`.
- Display a menu with numbered options like:
  - View
  - Add
  - Remove
  - Exit

Typical workflow:
- To see current tasks, choose the “View” option; the program will print each task with an index.
- To add a task, choose the “Add” option and type the task description when prompted; the task is saved to the file.
- To remove a task, choose the “Remove” option, check the task numbers in the displayed list, and input the number of the task to delete.
- To quit the application, select the “Exit” option; the main loop ends and the program terminates.

## Functional Requirements

Even though this is a small project, it aligns with standard functional requirement specifications used in academic project evaluation.

Main functional requirements covered:

- FR1: Task persistence
  - The system shall store the list of tasks in a text file such that tasks remain available across multiple runs of the program.

- FR2: Task viewing
  - The system shall allow the user to view all current tasks in a numbered list.

- FR3: Task addition
  - The system shall allow the user to add a new task by entering its description, and shall append it to the stored list.

- FR4: Task removal
  - The system shall allow the user to remove an existing task by selecting its index from the displayed list.

- FR5: Menu navigation
  - The system shall present a menu of operations and process user choices in a loop until the user chooses to exit.

These functional requirements map directly to the menu options and core operations implemented in the script.

## Non-Functional Requirements

The project also demonstrates several non-functional requirements that are typically expected in course projects.

- Performance:
  - For typical list sizes, operations such as viewing, adding, and removing tasks complete almost instantly because they operate on simple lists and a small text file.

- Usability:
  - The menu and prompts use clear, simple text instructions so that users with basic command-line familiarity can operate the application.
  - Error messages for invalid indexes help users recover from common mistakes without crashing the program.

- Reliability:
  - The application checks for file existence before reading, preventing crashes if the list file is missing on first run.
  - Basic exception handling around removal input ensures that non‑numeric or out‑of‑range values are handled gracefully.

- Maintainability:
  - Core operations are separated into functions such as reading, writing, displaying, and the main loop, making the code easier to read and extend.
  - The use of a single configuration variable for the file name makes it straightforward to change the storage file path in the future.

These properties together help show that even a simple program can be structured in a way that supports extension and reuse.

## Design and Architecture

The design follows a straightforward procedural architecture that is suitable for a small Python script.

Key elements:

- File handling abstraction:
  - `readfile()` encapsulates the logic for loading tasks from disk, including checking whether the file exists.
  - `writefile(items)` encapsulates saving the list of tasks back to the file, ensuring a single place manages disk writes.

- Presentation and interaction:
  - `displayitems()` is responsible for printing the header, body, and footer of the current task list in a consistent format.
  - The main loop in `main()` handles user interaction, menu display, and dispatching to the appropriate functionality for each option.

- Control flow:
  - The program uses a `while True` loop to repeatedly show the menu and process user choices until the exit option is selected.
  - `if-elif-else` blocks map numeric menu choices to functions such as viewing, adding, and removing tasks.

Although simple, this architecture respects the separation of concerns between data persistence, output formatting, and user interaction, which is an important principle in software design.[14][13]

## Example Scenarios

The following example scenarios illustrate how a user might interact with the application in practice.

- First-time use:
  - Run the script, choose “View”; the list may be empty if `mytodolist.txt` does not exist yet.
  - Choose “Add”, enter a task such as “Complete project documentation”, and see confirmation that it has been saved.

- Managing multiple tasks:
  - Add several tasks using the “Add” option, then use “View” to verify that they are all listed with correct indices.
  - Use “Remove” to delete a task that is no longer needed by entering its number from the displayed list.

These scenarios demonstrate the complete cycle of adding, viewing, and removing tasks using only the terminal interface.

## Future Enhancements

There are many ways this project could be extended to meet more advanced academic or practical requirements.

Possible enhancements:

- Additional features:
  - Support for marking tasks as completed instead of only deleting them.
  - Adding due dates or priorities to tasks and sorting the list accordingly.

- Improved storage:
  - Migrating from a plain text file to structured storage such as JSON or a lightweight database to support richer task metadata.

- User experience:
  - Colorized terminal output or improved formatting to distinguish completed and pending tasks.
  - Command-line arguments for quick operations without navigating a menu, such as directly adding a task from the command invocation.

- Software engineering practices:
  - Splitting the code into multiple modules for storage, UI, and core logic.
  - Adding basic unit tests for file operations and menu logic to improve reliability.