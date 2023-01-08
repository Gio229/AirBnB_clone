

#!/usr/bin/python3
"""Unit test for the file storage class
"""
from io import StringIO
import unittest
from unittest.mock import patch

from console import HBNBCommand


class TestConsoleClass(unittest.TestCase):
    """
    This class define count tests for Console
    """

    def test_help(self):
        """ test help output
        """
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help")
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_val.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_val:
            HBNBCommand().onecmd("help count")
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

    def test_destroy(self):
        """ test destroy output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_count(self):
        """ test count output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('count BaseModel')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_update(self):
        """ test update output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(val.getvalue() == "** instance id missing **\n")

    def test_count_base_model_method(self):
        """ test count BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_review_method(self):
        """ test count Review method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Review')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Review.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_user_method(self):
        """ test count User method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_state_method(self):
        """ test count State method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create State')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('State.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_city_method(self):
        """ test count City method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_amenity_method(self):
        """ test count Amenity method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Amenity')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Amenity.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_place_method(self):
        """ test count Place method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Place')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Place.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    # -------------------------------

    def test_count_base_model_method(self):
        """ test count BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('BaseModel.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_review_method(self):
        """ test count Review method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Review')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Review.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_user_method(self):
        """ test count User method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('User.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_state_method(self):
        """ test count State method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create State')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('State.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_city_method(self):
        """ test count City method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_amenity_method(self):
        """ test count Amenity method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Amenity')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Amenity.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_count_place_method(self):
        """ test count Place method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Place')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Place.count()')
            self.assertTrue(len(val.getvalue()) > 0)

    # -------------------------------

    def test_all_base_model_method(self):
        """ test all BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('BaseModel.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_review_method(self):
        """ test all Review method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Review')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Review.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_user_method(self):
        """ test all User method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create User')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('User.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_state_method(self):
        """ test all State method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create State')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('State.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_city_method(self):
        """ test all City method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_amenity_method(self):
        """ test all Amenity method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Amenity')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Amenity.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    def test_all_place_method(self):
        """ test all Place method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Place')
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Place.all()')
            self.assertTrue(len(val.getvalue()) > 0)

    # -------------------------------

    def test_show_base_model_method(self):
        """ test show BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('BaseModel.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_review_method(self):
        """ test show Review method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Review')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Review.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_user_method(self):
        """ test show User method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create User')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('User.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_state_method(self):
        """ test show State method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create State')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('State.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_city_method(self):
        """ test show City method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_amenity_method(self):
        """ test show Amenity method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Amenity')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Amenity.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_show_place_method(self):
        """ test show Place method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Place')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Place.show("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    # -------------------------------

    def test_destroy_base_model_method(self):
        """ test destroy BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create BaseModel')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('BaseModel.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_review_method(self):
        """ test destroy Review method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Review')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Review.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_user_method(self):
        """ test destroy User method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create User')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('User.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_state_method(self):
        """ test destroy State method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create State')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('State.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_city_method(self):
        """ test destroy City method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_amenity_method(self):
        """ test destroy Amenity method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Amenity')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Amenity.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    def test_destroy_place_method(self):
        """ test destroy Place method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create Place')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('Place.destroy("{}")'.format(instance_created_id))
            self.assertTrue(len(val.getvalue()) > 0)

    # -------------------------------

    def test_update_base_model_method_first_alternative(self):
        """ test update BaseModel method output """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('create City')
            instance_created_id = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.show("{}")'.format(instance_created_id))
            result1 = val.getvalue()
        with patch('sys.stdout', new=StringIO()) as val:
            arguments = "'name', 'John'"
            HBNBCommand().onecmd('City.update("{}", {})'.format(instance_created_id, arguments))
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd('City.show("{}")'.format(instance_created_id))
            result2 = val.getvalue()
            self.assertTrue(result1 != result2)
    #---------------------

