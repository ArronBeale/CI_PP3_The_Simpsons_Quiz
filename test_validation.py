import unittest
import validation as val


class Test_emails(unittest.TestCase):
    """
    test validation of emails
    """

    def test_validate_email(self):
        self.assertTrue(val.validate_email('test@test.com'), True)


class Test_stats(unittest.TestCase):
    """
    Thsi will test the stats functions of total players and
    total score and total svore average
    """

    def test_total_player(self):
        self.assertTrue(val.total_players(), True)

    def test_total_score(self):
        self.assertNotEqual(val.total_score(), 0)


if __name__ == '__main__':
    unittest.main()
