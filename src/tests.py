import unittest
from io import StringIO
import sys

from app import process_commands
from directories import FileSystem

# Assume the FileSystem and Directory classes have been defined as above

class TestFileSystem(unittest.TestCase):

    def setUp(self):
        self.fs = FileSystem()

    def test_create_directory(self):
        """Test creating a directory that does not exist."""
        self.fs.create('fruits')
        self.assertIn('fruits', self.fs.root.children)
        self.assertEqual(self.fs.root.children['fruits'].name, 'fruits')

    def test_create_directory_with_missing_parent(self):
        """Test creating a directory when the parent directory does not exist."""
        captured_output = StringIO()
        sys.stdout = captured_output
        self.fs.create('fruits/apples')
        sys.stdout = sys.__stdout__
        expected_error = "Cannot create fruits/apples - fruits does not exist\n"
        self.assertIn(expected_error, captured_output.getvalue())

    def test_create_existing_directory(self):
        """Test creating a directory that already exists."""
        self.fs.create('fruits')
        captured_output = StringIO()
        sys.stdout = captured_output
        self.fs.create('fruits')
        sys.stdout = sys.__stdout__
        expected_error = "Cannot create fruits - fruits already exists\n"
        self.assertIn(expected_error, captured_output.getvalue())

    def test_delete_directory(self):
        """Test deleting an existing directory."""
        self.fs.create('fruits')
        self.fs.delete('fruits')
        self.assertNotIn('fruits', self.fs.root.children)


class TestFileSystemIntegration(unittest.TestCase):

    def test_full_command_sequence(self):
        """Test processing a sequence of commands and verifying the overall output."""
        commands = """
CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
DELETE fruits/apples
DELETE foods/fruits/apples
LIST
"""

        expected_output = """CREATE fruits
CREATE vegetables
CREATE grains
CREATE fruits/apples
CREATE fruits/apples/fuji
LIST
fruits
  apples
    fuji
grains
vegetables
CREATE grains/squash
MOVE grains/squash vegetables
CREATE foods
MOVE grains foods
MOVE fruits foods
MOVE vegetables foods
LIST
foods
  fruits
    apples
      fuji
  grains
  vegetables
    squash
DELETE fruits/apples
Cannot delete fruits/apples - fruits does not exist
DELETE foods/fruits/apples
LIST
foods
  fruits
  grains
  vegetables
    squash"""

        # Capture the output of the process_commands function
        captured_output = StringIO()
        sys.stdout = captured_output

        process_commands(commands)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue().strip()
        self.assertEqual(output, expected_output.strip())
        
if __name__ == '__main__':
    unittest.main()