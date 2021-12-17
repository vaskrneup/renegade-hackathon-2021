from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

import phonenumbers


def validate_phone(number: str):
    """
    Validates given phone number, If invalid then raise django.core.exceptions.ValidationError

    :param number: Phone Number in any format
    :return: None
    """
    _number = phonenumbers.parse(number, "NP")
    if not phonenumbers.is_valid_number(_number):
        raise ValidationError(
            _(f"`{number}` is not a Valid Number."),
        )


def validate_name(name: str):
    """
    Validates the given name, If invalid then raise django.core.exceptions.ValidationError
    :param name: Name to validate
    :return: None
    """

    for letter in name:
        if letter and not letter.isalnum():
            raise ValidationError(
                _(f"`{name}` is not a valid name, Numbers can only contain Alphabets.")
            )
