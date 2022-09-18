import unittest
import re
from password_generator import make_one_special_char
from password_generator import make_one_uppercase_letter
from password_generator import make_one_lowercase_letter
from password_generator import make_one_number
from password_generator import make_password

class TestPasswordGenerator(unittest.TestCase):
  
  def test_make_one_special_char_multiple_ranges(self):
    regex = re.compile(r'^[ -\/:-@\[-`{-~]$')
    
    for i in range(100):
      with self.subTest(i=1):
        self.assertRegex(make_one_special_char(), regex)

  def test_make_one_uppercase_letter_range_65_90(self):
    regex = re.compile(r'^[A-Z]$')
    
    for i in range(100):
      with self.subTest(i=1):
        self.assertRegex(make_one_uppercase_letter(), regex)
  
  def test_make_one_lowercase_letter_range_97_122(self):
    ord_range = list(range(97, 123))
    
    for i in range(100):
      with self.subTest(i=1):
        self.assertIn(ord(make_one_lowercase_letter()), ord_range)

  def test_make_one_number_range_48_58(self):
    ord_range = list(range(48, 58))
    
    for i in range(100):
      with self.subTest(i=1):
        self.assertIn(ord(make_one_number()), ord_range)
     
    
  def test_make_password_length(self):
    with self.assertRaises(AssertionError):
      make_password(length=1)
      
    with self.assertRaises(AssertionError):
      make_password(length='a')

    for i in range(4, 100):
      with self.subTest(i=1):
        self.assertTrue(len(make_password(length=i)) == i)
    
  def test_make_password_all_params_true(self):
    regex = re.compile(
      r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@\[-`{-~]).+$'
    )
    
    self.assertRegex(make_password(), regex)
    
  def test_make_password_all_params_false(self):
    with self.assertRaises(AssertionError):
      make_password(numbers=False, upper=False, lower=False, chars=False)
  
  def test_make_password_no_upper(self):
    regex = re.compile(r'^[^A-Z]+$')
    
    for i in range(4, 100):
      with self.subTest(i=1):
        self.assertRegex(make_password(length=i, upper=False), regex)

  def test_make_password_no_numbers(self):
    regex = re.compile(r'^\D+$')
    
    for i in range(4, 100):
      with self.subTest(i=1):
        self.assertRegex(make_password(length=i, numbers=False), regex)
  
  def test_make_password_no_lower(self):
    regex = re.compile(r'^[^a-z]+$')
    
    for i in range(4, 100):
      with self.subTest(i=1):
        self.assertRegex(make_password(length=i, lower=False), regex)
  
  def test_make_password_no_chars(self):
    regex = re.compile(r'^[^ -\/:-@\[-`{-~]+$')
    
    for i in range(4, 100):
      with self.subTest(i=1):
        self.assertRegex(make_password(length=i, chars=False), regex)
  
  def test_make_password_sequence_not_allowed(self):
    regex = re.compile(r'^(?:[ -\/:-@\[-`{-~][a-z][A-Z][0-9])+$')
    
    for i in range(4, 10000):
      with self.subTest(i=i):
        self.assertNotRegex(make_password(length=i), regex)
  
if __name__ == '__main__':
  unittest.main(verbosity=2)