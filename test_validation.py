import unittest
import validation as val


class Test_emails(unittest.TestCase):
    """
    test validation of emails
    """
    def test_validate_email(self):
        self.assertTrue(val.validate_email('test@test.com'), True)



class Test_player_names(unittest.TestCase):
    def test_retrieve_name(self):
        name = 'Test'
        email = 'test@test.com'
        result = val.retrieve_player_name(email)
        self.assertEqual(result, 'Test')


if __name__ == '__main__':
    unittest.main()
