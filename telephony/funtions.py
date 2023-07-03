import phonenumbers
from phonenumbers.phonenumberutil import NumberParseException

def is_valid_phone(phone_number):
    """
    Checks if phone number is valid or not, if valid returns True else False
    """
    try:
        parsed_phone_num = phonenumbers.parse(phone_number, None)
        return phonenumbers.is_valid_number(parsed_phone_num)
    except NumberParseException:
        return False
