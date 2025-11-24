# Python CLI To-Do List Manager

## Overview
A lightweight, command-line interface (CLI) application designed to help users manage their daily tasks efficiently. This project implements a persistent to-do list using Python, allowing users to add, view, and remove tasks with data saved automatically to a local text file.

## Features
- **Task Management**: Add new tasks and remove completed ones.
- **Persistent Storage**: Automatically saves tasks to `my_todo_list.txt`, ensuring data is not lost when the program closes.
- **User-Friendly Interface**: Simple numbered menu for easy navigation.
- **Error Handling**: Validates user input to prevent crashes during task deletion.

## Technologies Used
- **Language**: Python 3.x
- **Modules**: `os` (Standard Library)
- **Storage**: Flat text file (`.txt`)

## Installation & Execution
1. **Prerequisites**: Ensure Python 3 is installed on your system.
2. **Download**: Clone this repository or download `To-do-list-manager.py`.
3. **Run**:
   Open your terminal or command prompt and navigate to the project directory:

## Usage Instructions
1. Launch the application.
2. Select **Option 2** to add a new task.
3. Select **Option 1** to view your current list.
4. Select **Option 3** to remove a task by its number.
5. Select **Option 4** to save and exit.

## Testing
- Try adding a task "Study Python" and restarting the app to verify it saves.
- Try removing a task with an invalid number to test error handling.