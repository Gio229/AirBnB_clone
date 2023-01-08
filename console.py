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

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split(' ')
        all_instances = []
        if args == ['']:
            for value in storage.all().values():
                all_instances.append(value.__str__())
            print(all_instances)
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                identifier = args[0] + "." + value.id
                if key == identifier:
                    all_instances.append(value.__str__())
            print(all_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class
        name and id by adding or updating attribute
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            identifier = args[0] + "." + args[1]
            if identifier not in storage.all():
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                attribute_type = type(eval(args[3]))
                new_value = args[3].strip('\'\"')
                setattr(storage.all()[identifier],
                        args[2], attribute_type(new_value))
                storage.all()[identifier].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
