# AirBnB clone - The console

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230104T073653Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3fa0af102eb0fc64310d1c9ad06953a114e2367be1ad3638a5e3dd52315af4fb)

## Description

This AirBnB clone project (The console) is the first version of a larger clone project.
Here we are building a commandline interpreter to easly work with

## Features

This commandline tool (hbnb) is going to:

> - Create a new object (ex: a new User or a new Place)
> - Retrieve an object from a >file, a database etc…
> - Do operations on objects (count, compute stats, etc…)
> - Update attributes of an object
> - Destroy an object

## Getting started

Open your terminal an run this following command to clone the repository:

    git clone "https://github.com/Gio229/AirBnB_clone"

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