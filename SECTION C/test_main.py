from unittest import TestCase
from main import num_to_word

# Test class to ensure that the program is still displaying the correct input.
class Test(TestCase):
    def test_num_to_word(self):

        stringTest1 = num_to_word(90376000010012)
        stringTest2 = num_to_word(11)
        stringTest3 = num_to_word(10000)

        # Test Assertions
        self.assertEqual(stringTest1, "ninety trillion, three hundred and seventy-six billion, ten thousand and twelve")
        self.assertEqual(stringTest2, "eleven")
        self.assertEqual(stringTest3, "ten thousand")
