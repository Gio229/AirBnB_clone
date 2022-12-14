#!/usr/bin/python3
"""
This module define commands console
"""
import cmd
import json

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

    __available_utilities = ["show",
                             "count",
                             "all",
                             "update",
                             "destroy"]

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
        Syntax: create <class name>
        eg: create BaseModel
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
        """Prints the string representation of an instance based on the class name and id
        Default syntax: show <class name> <id>
        Alternative syntax: <class name>.show(<id>)
        eg: show BaseModel 1234-1234-123
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[0] + "." + args[1].strip('" ')
            if instance_id not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[instance_id])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        Default syntax: destroy <class name> <id>
        Alternative syntax: <class name>.destroy(<id>)
        eg1: destroy BaseModel 1234-1234-123
        eg2: BaseModel.destroy(1234-1234-123)
        """
        args = arg.split(' ')
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in self.__available_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance_id = args[0] + "." + args[1].strip('" ')
            if instance_id not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[instance_id]
                storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances based or not on the class name
        Default syntax: all [<class name>]
        Alternative syntax: <class name>.all()
        eg1: all BaseModel
        eg2: BaseModel.all()
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
        """ Updates an instance based on the class name and id by adding or updating attribute
        Default syntax: update <class name> <id> <attribute name> "<attribute value>"
            !!! THIS SYNTAX CAN JUST UPDATE ONE ATTRIBUTE AT TIME
        Alternative syntax 1: <class name>.update(<id>, <attribute name>, <attribute value>)
            !!! THIS SYNTAX CAN JUST UPDATE ONE ATTRIBUTE AT TIME
        Alternative syntax 2: <class name>.update(<id>, <dictionary representation>)
        eg1: update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        eg2:  User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", "age", 89)
        eg3: User.update("38f22813-2753-4d42-b37c-57a17f1e4f88", {'first_name': "John", "age": 89})
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

    def do_count(self, arg):
        """Retrieve the number of instances of a specified class
        Default syntax: count [<class name>]
        Alternative syntax: <class name>.count()
        eg1: count BaseModel
        eg2: BaseModel.count()
        """
        if arg not in self.__available_classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in storage.all().keys():
                if arg in key:
                    count += 1
            print(count)

    def default(self, line: str):
        """Main goal is to handle util method
        """
        if "(" in line or ")" in line:
            args = line.split('.')
        else:
            args = line.split(' ')[0].split('.')
        class_name = args[0]
        if len(args) < 2:
            print("** Unknown syntax: {} **".format(line))
        elif class_name not in self.__available_classes:
            print("** class doesn't exist **")
        else:
            util_method, argument_passed = self.which_util_func(args[1])
            if util_method not in self.__available_utilities:
                print("[{}] is not available as method".format(util_method))
            elif util_method == "all":
                self.do_all(class_name)
            elif util_method == "count":
                self.do_count(class_name)
            elif util_method == "show":
                self.do_show("{} \"{}\"".format(class_name, argument_passed))
            elif util_method == "destroy":
                self.do_destroy("{} \"{}\"".format(
                    class_name, argument_passed))
            elif util_method == "update":
                if "{" not in argument_passed and "}" not in argument_passed:
                    argument_passed = argument_passed.replace("\"", "")
                    argument_passed = argument_passed.replace("'", "")
                    list_argument_passed = argument_passed.split(", ")
                    try:
                        if type(eval(str(list_argument_passed[2]))) is not str:
                            self.do_update("{} {} {} {} ".format(class_name,
                                                                 list_argument_passed[0], list_argument_passed[1], list_argument_passed[2]))
                    except NameError:
                        self.do_update("{} {} {} \"{}\"".format(class_name,
                                                                list_argument_passed[0], list_argument_passed[1], list_argument_passed[2]))

                else:
                    list_argument_passed = argument_passed.split(", ", 1)
                    argument_id = list_argument_passed[0]
                    list_argument_passed[1] = list_argument_passed[1].replace(
                        "'", "\"")
                    argument_dict = json.loads(list_argument_passed[1])

                    for key, value in argument_dict.items():
                        try:
                            if type(eval(str(value))) is not str:
                                to_update = "{} {} {} {}".format(
                                    class_name, argument_id, key, value)
                        except NameError:
                            to_update = "{} {} {} \"{}\"".format(
                                class_name, argument_id, key, value)
                        self.do_update(to_update)

    def which_util_func(self, to_evaluate: str):
        """ Analyze a given string and return the
        util function as string and param if exist
        """
        args = to_evaluate.split('(')
        if len(args) > 1:
            args[1] = args[1].strip('\')"')
            return (args[0], args[1])
        return (args[0], 'invalid')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
