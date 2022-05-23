import unittest
import validation as val


class TestValidate(unittest.TestCase):
    """
    test validation of email
    """
    def test_validate_email(self):
        self.assertTrue(val.validate_email('test@test.com'), True)


if __name__ == '__main__':
    unittest.main()
