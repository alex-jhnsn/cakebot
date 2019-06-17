import unittest
import json
from src import UsersHandler

class UsersTest(unittest.TestCase):

    def WhenAddingAUserWithNoUserId_BadRequestShouldBeReturned(self):
        event = {}
        result = UsersHandler.handle(event, None)

        expected = {
            'statusCode': 400,
            'body': 'Missing user'
        }

        self.assertEqual(expected, result)

    def WhenAddingAUserWithAUserId_OKShouldBeReturned(self):
        event = {}
        result = UsersHandler.handle(event, None)

        expected = {
            'statusCode': 200,
            'body': '@lilal is now a baker!'
        }

        self.assertEqual(expected, result)

    def WhenDeletingAUserWithNoUserId_BadRequestShouldBeReturned(self):
        event = {}
        result = UsersHandler.handle(event, None)

        expected = {
            'statusCode': 400,
            'body': 'Missing user'
        }

        self.assertEqual(expected, result)

    def WhenDeletingAUserWithAUserId_OKShouldBeReturned(self):
        event = {}
        result = UsersHandler.handle(event, None)

        expected = {
            'statusCode': 200,
            'body': '@lilal is no longer a baker.'
        }

        self.assertEqual(expected, result)


