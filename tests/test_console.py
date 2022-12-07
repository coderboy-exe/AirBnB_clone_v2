#!/usr/bin/python3
''' Test suite for the console'''


import sys
import models
import unittest
from models import storage
from console import HBNBCommand


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
