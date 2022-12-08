#!/usr/bin/python3
''' Test suite for the console'''


import sys
import models
import unittest
from models import State
from models import storage
from models.engine.db_storage import DBStorage
from console import HBNBCommand
from IO import StringIO
from os import getenv
from unittest.mock import create_autospec


db = getenv("HBNB_TYPE_STORAGE", "fs")



class test_console(unittest.TestCase):
    ''' Test the console module'''
    def setUp(self):
        '''Setup Tests module for console'''
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        '''Teardown test module'''
        sys.stdout = self.backup

    def create(self):
        '''Test creation an instance of the HBNBCommand class'''
        return HBNBCommand()

    def test_quit(self):
        ''' Test quit exists'''
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        ''' Test EOF exists'''
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        ''' Test all method exists'''
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show(self):
        '''
            Testing that show exists
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_class_name(self):
        '''
            Testing the error messages for class name missing.
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.apt_out.getvalue())
        sys.stdout = self.backup
        self.assetEqual("** class name missing **\n", x)

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_no_instance_found(self):
        '''
            Test show message error for id missing
        '''
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.sdout = self.capt_out
       	console.onecmd("show User " + "1234567")
	x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assetEqual("** no instance found **\n", x)
