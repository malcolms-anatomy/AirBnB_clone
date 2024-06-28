#!/usr/bin/python3
# Importing libraries
import os
import sys
from datetime import datetime


# Constants
MAX_RETRIES = 5


# Class definition
class MyClass:
    """A class to demonstrate code style."""

    def __init__(self, name):
        """Initialize with name."""
        self.name = name

    def greet(self):
        """Greet the user."""
        print(f"Hello, {self.name}!")

    def perform_task(self, task_name):
        """Perform a task."""
        if task_name == 'cleanup':
            self._cleanup()
        elif task_name == 'validate':
            self._validate()
        else:
            raise ValueError(f"Unknown task: {task_name}")

    def _cleanup(self):
        """Perform cleanup."""
        print("Performing cleanup...")

    def _validate(self):
        """Perform validation."""
        print("Performing validation...")


# Function definition
def main():
    """Main function to demonstrate usage."""
    name = input("Enter your name: ")
    obj = MyClass(name)
    obj.greet()
    obj.perform_task('cleanup')


if __name__ == "__main__":
    main()
