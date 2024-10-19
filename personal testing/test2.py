import pytest
from src.tested2 import check_number, check_prime, check_palindrome

def test_check_number():
    assert check_number(5) == 'The number is positive.'
    assert check_number(-3) == "The number is negative."
    assert check_number(0) == "The number is zero."

def test_check_prime():
    assert check_prime(7) == True
    assert check_prime(10) == False
    assert check_prime(1) == False

def test_check_palindrome():
    assert check_palindrome(121) == True
    assert check_palindrome(123) == False
    assert check_palindrome(12321) == True