import unittest
import os.path

from initialize_database import Create_databases

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        Create_databases().create_user_database()



    def test_user_database_file_exists(self):

        
        self.assertEqual(os.path.exists("/src/users.db"))
