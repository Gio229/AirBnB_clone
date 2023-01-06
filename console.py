#!/usr/bin/python3
"""
This module define commands console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Define all commands to manipulate data
    """
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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
