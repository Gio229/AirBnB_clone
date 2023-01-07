#!/usr/bin/python3
"""
This module define commands console
"""
import cmd

from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    Define all commands to manipulate data
    """

    __available_classes = ["BaseModel",
                           "User",
                           "City",
                           "Amenity",
                           "State",
                           "Place",
                           "Review"]

    # Change the prompt name
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """ Command to exit the program.
        """
        return True

    def emptyline(self):
        """Eempty lines + ENTER don't execute anything.
        """
        pass

    def do_create(self, arg):
        """
        Create instance of class
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(args[0])()
            storage.new(new_instance)
            storage.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[0] + "." + args[1]
            if instance_id not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance_id])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[0] + "." + args[1]
            if instance_id not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[instance_id]
                storage.save()





if __name__ == '__main__':
    HBNBCommand().cmdloop()
