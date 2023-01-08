# AirBnB clone - The console

![](/web_static/images/hbnb_project.png)

## Description

This AirBnB clone project (The console) is the first version of a larger web application clone project.

Here we are building a command line interpreter to easly work and interact with our data (in file storage for the moment) without the need of user interface.

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/815046647d23428a14ca.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20230108%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20230108T222955Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=11d8bcf9bd79fc4b1e0f0e16b575775313a97faf380823a7e76950a9144102eb)

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
>EOF &nbsp;&nbsp; help &nbsp;&nbsp; quit
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
>EOF &nbsp;&nbsp; help &nbsp;&nbsp; quit
>
>(hbnb) 
>
>$