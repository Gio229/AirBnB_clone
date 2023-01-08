

#!/usr/bin/python3
"""Unit test for the file storage class
"""
from io import StringIO
import unittest
from unittest.mock import patch

from console import HBNBCommand


class TestConsoleClass(unittest.TestCase):
    """
    This class define all tests for Console
    """

    def test_help(self):
        """ test help output """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help quit")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help EOF")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help count")
            self.assertTrue(len(help_val.getvalue()) > 0)

    def test_quit(self):
        """ test quit output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("quit")
            self.assertTrue(val.getvalue() == "")
    
    def test_EOF(self):
        """ test EOF output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("EOF")
            self.assertTrue(val.getvalue() == "")
    
    def test_empty_line(self):
        """ test EOF output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("")
            self.assertTrue(val.getvalue() == "")
    
    def test_create(self):
        """ Test the create command """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(val.getvalue()) > 0)
    
    def test_show(self):
        """ test show command"""
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            basemodel_id = val.getvalue()
            self.assertTrue(len(basemodel_id) > 0)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel ')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('show BaseModel ' + basemodel_id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
