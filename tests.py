import unittest
from unittest import TestCase
import os.path

from simple_import import import_item, from_x_import_y

class FromXImportYTests(TestCase):
	def test_single(self):
		self.assertEqual(from_x_import_y('os', 'path'), os.path)
	def test_multiple(self):
		self.assertEqual(from_x_import_y('os.path', 'relpath'), os.path.relpath)

class ImportItemTests(TestCase):
	def test_single(self):
		self.assertEqual(import_item('unittest.TestCase'), TestCase)
	def test_multiple(self):
		self.assertEqual(import_item('os.path.relpath'), os.path.relpath)

if __name__ == '__main__':
	unittest.main()
