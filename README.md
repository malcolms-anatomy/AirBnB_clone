# AirBnB Clone - The Console

## Description
Welcome to the AirBnB clone project! This is the first step towards building your first full web application: the AirBnB clone. This initial phase focuses on creating a command interpreter to manage AirBnB objects, which will be used in subsequent projects like HTML/CSS templating, database storage, API development, and front-end integration.

## Command Interpreter

The command interpreter allows you to manage various AirBnB objects such as users, places, cities, etc. It can create, retrieve, update, and delete objects. This interpreter functions similarly to a shell but is specific to AirBnB's use case.

### How to Start the Command Interpreter

You can start the command interpreter in interactive mode by running:

```sh
$ ./console.py

Here are some examples of using the command interpreter:

(hbnb) create User
(e3c01326-6d87-4e5a-b7b4-09361ecf373d)
(hbnb) show User e3c01326-6d87-4e5a-b7b4-09361ecf373d
[User] (e3c01326-6d87-4e5a-b7b4-09361ecf373d) {'id': 'e3c01326-6d87-4e5a-b7b4-09361ecf373d', 'created_at': '2023-06-28T20:18:33.084650', 'updated_at': '2023-06-28T20:18:33.084650'}
(hbnb) update User e3c01326-6d87-4e5a-b7b4-09361ecf373d name "John Doe"
(hbnb) show User e3c01326-6d87-4e5a-b7b4-09361ecf373d
[User] (e3c01326-6d87-4e5a-b7b4-09361ecf373d) {'id': 'e3c01326-6d87-4e5a-b7b4-09361ecf373d', 'created_at': '2023-06-28T20:18:33.084650', 'updated_at': '2023-06-28T20:19:33.084650', 'name': 'John Doe'}
(hbnb) all User
[[User] (e3c01326-6d87-4e5a-b7b4-09361ecf373d) {'id': 'e3c01326-6d87-4e5a-b7b4-09361ecf373d', 'created_at': '2023-06-28T20:18:33.084650', 'updated_at': '2023-06-28T20:19:33.084650', 'name': 'John Doe'}]
(hbnb) destroy User e3c01326-6d87-4e5a-b7b4-09361ecf373d
(hbnb) all User
[]
(hbnb) quit

