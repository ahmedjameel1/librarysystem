from django.core.exceptions import ValidationError


def validate_alpha(value):
    #validate that the name of the author or one of it's chars is not a number.
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError('Only alphabetic characters and spaces are allowed.')


def validate_isbn13(value):
    """
        Validate the format and checksum of an ISBN-13 number.

        Parameters:
        value (str): The ISBN-13 number to validate.

        Raises:
        ValidationError: If the ISBN-13 number does not meet the specified criteria.

    """
    if len(value) != 13:
        raise ValidationError('ISBN must be 13 digits long.')
    
    if not value.startswith('978') and not value.startswith('979'):
        raise ValidationError('ISBN must start with 978 or 979.')
    
    try:
        #make sure all numbers no chars
        digits = [int(d) for d in value]
    except ValueError:
        raise ValidationError('ISBN must contain only digits.')

    #here we sum all numbers after multiplying each odd number by 1 and even number by 3 
    total = sum(int(digit) * (1 if i % 2 == 0 else 3) for i, digit in enumerate(digits[:-1]))
    #get the remainder
    check_digit = (10 - (total % 10)) % 10
    #compare with the last digit so it's a valid isbn or not.
    if check_digit != digits[-1]:
        raise ValidationError('Invalid ISBN check digit.')
