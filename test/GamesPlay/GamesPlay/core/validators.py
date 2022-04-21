from django.core.exceptions import ValidationError


def rating_validator(value):
    if value > 5 or value < 0.1:
        raise ValidationError('Rating cannot be greater than 5 or below 0.1!')


def age_validator(value):
    if value < 12:
        raise ValidationError('Age cannot be less than 12!')


def max_level_validator(value):
    if value < 1:
        raise ValidationError('level cannot be less than 1')
