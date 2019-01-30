import unittest

from CreditCard_Validator import Validate_Card


class CC_Tests(unittest.TestCase):

    """Tests for Validate_Card."""

    def test_check_cc(self):
        #16 Digits
        self.assertTrue(Validate_Card("4123456789123456"))
        #16 Digits with hyphen
        self.assertTrue(Validate_Card("5123-4567-8912-3456"))
        #Bad Formatting
        self.assertFalse(Validate_Card("61234-567-8912-3456"))
        #16 digits
        self.assertTrue(Validate_Card("4123356789123456"))
        #Repeated Digits:
        self.assertFalse(Validate_Card("5133-3367-8912-3456"))
        #Spaces Included
        self.assertFalse(Validate_Card("5123 - 3567 - 8912 - 3456"))


if __name__ == "__main__":
    unittest.main()
