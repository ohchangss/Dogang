import unittest
import tempfile
import os
import sys
import yaml
class TestYaml(unittest.TestCase):
    def setUp(self) -> None:
        with open('rec/test_rec/test.yaml') as f:
            self.yaml = yaml.load(f, Loader=yaml.FullLoader)

    def test_read_yaml(self):
        self.assertEqual(type(self.yaml), dict)
        self.assertEqual(self.yaml['ID'], '1test1')
        self.assertEqual(self.yaml['NAME'], 'ohchangss')
        self.assertEqual(self.yaml['DATANAME'], 'iris.csv')

