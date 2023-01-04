# AirBnB clone - The console

![](/web_static/images/hbnb_project.png)

## Description

This AirBnB clone project (The console) is the first version of a larger clone project.

Here we are building a command line interpreter to easly work and interact with our data without the need of user interface.

## Features

This command line tool (hbnb) is going to:

> - Create a new object (ex: a new User or a new Place)
> - Retrieve an object from a file, a database etc…
> - Do operations on objects (count, compute stats, etc…)
> - Update attributes of an object
> - Destroy an object

## Getting started

Open your terminal an run this following command to clone the repository:

    git clone "https://github.com/Gio229/AirBnB_clone.git"

Access AirBnb directory:

    cd AirBnB_clone

Run the console in interactive mode with:

    ./console.py

The output will look like this:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit

    (hbnb) 
    (hbnb) 
    (hbnb) quit
    $

But also in non-interactive mode:

    $ echo "help" | ./console.py
    (hbnb)

    Documented commands (type help  <topic>):
    ========================================
    EOF  help  quit
    (hbnb) 
    $