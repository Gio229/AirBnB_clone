# AirBnB clone - The console

![](/web_static/images/hbnb_project.png)

## Description

This AirBnB clone project (The console) is the first version of a larger web application clone project.

Here we are building a command line interpreter to easly work and interact with our data (in file storage for the moment) without the need of user interface.

![](/web_static/images/v1.png)

## Features

This command line tool (hbnb) is going to:

> - Create a new object (ex: a new User or a new Place)
> - Retrieve an object from a file, a database etc…
> - Do operations on objects (count, compute stats, etc…)
> - Update attributes of an object
> - Destroy an object

## Getting started

Open your terminal an run this following command to clone the repository:

    git clone https://github.com/Gio229/AirBnB_clone.git

Access AirBnb directory:

    cd AirBnB_clone

Run the console in interactive mode with:

    ./console.py

The output will look like this:

>$ ./console.py
>
>(hbnb) help
>
>Documented commands (type help <topic>):
>
>========================================
>
>EOF &nbsp;&nbsp; all &nbsp;&nbsp; count &nbsp;&nbsp; create  destroy &nbsp;&nbsp; help &nbsp;&nbsp; quit &nbsp;&nbsp; show &nbsp;&nbsp; update
>
>(hbnb) 
>
>(hbnb)
> 
>(hbnb) quit
>
>$

But also in non-interactive mode:

>$ echo "help" | ./console.py
>(hbnb)
>
>Documented commands (type help  <topic>):
>
>========================================
>
>EOF &nbsp;&nbsp; all &nbsp;&nbsp; count &nbsp;&nbsp; create  destroy &nbsp;&nbsp; help &nbsp;&nbsp; quit &nbsp;&nbsp; show &nbsp;&nbsp; update
>
>(hbnb) 
>
>$

## How to use commands

The `help` command here should be your best friend

>
>(hbnb) help
>
>Documented commands (type help <topic>):
>
>========================================
>
>EOF &nbsp;&nbsp; all &nbsp;&nbsp; count &nbsp;&nbsp; create  destroy &nbsp;&nbsp; help &nbsp;&nbsp; quit &nbsp;&nbsp; show &nbsp;&nbsp; update
>
>(hbnb) 
>

As you can see it display all available commands.

To know how to use a specific command just hint `help` and then the `command`.

Let's take a deep dive with this exemple below.

    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  count  create  destroy  help  quit  show  update

    (hbnb) help quit
    Command to exit the program.
            
    (hbnb) 
    (hbnb) help update
    Updates an instance based on the class name and id by adding or updating attribute
            Default syntax: update <class name> <id> <attribute name> "<attribute value>"
                !!! THIS SYNTAX CAN JUST UPDATE ONE ATTRIBUTE AT TIME
            Alternative syntax 1: <class name>.update(<id>, <attribute name>, <attribute value>)
                !!! THIS SYNTAX CAN JUST UPDATE ONE ATTRIBUTE AT TIME
            Alternative syntax 2: <class name>.update(<id>, <dictionary representation>)
            eg1: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
            eg2:  User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
            eg3: User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
            
    (hbnb) 

## Authors
[Giovanni Athaoue](https://github.com/Gio229)