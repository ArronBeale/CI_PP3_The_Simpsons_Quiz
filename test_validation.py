import unittest
import validation as val


class Test_emails(unittest.TestCase):
    """
    This will test the validation of the email format
    """

    def test_validate_email(self):
        self.assertTrue(val.validate_email('test@test.com'), True)


class Test_total_players(unittest.TestCase):
    """
    This will test the stats function of total players
    """

    def test_total_players(self):
        self.assertTrue(val.total_players(), True)


class Test_total_score(unittest.TestCase):
    """
    This will test the stats function of total score
    """

    def test_total_score(self):
        self.assertNotEqual(val.total_score(), 0)


class Test_average_score(unittest.TestCase):
    """
    This will test the stats function of average score
    """

    def test_average_score(self):
        self.assertNotEqual(val.total_score(), 0)


if __name__ == '__main__':
    unittest.main()
