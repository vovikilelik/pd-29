from datetime import date

from rest_framework import serializers


class AgeAllowValidator:

    def __init__(self, age: int):
        self._age = age

    def __call__(self, value):
        today = date.today()
        if date(today.year - self._age, today.month, today.day) < value:
            raise serializers.ValidationError(f'{value} not allowed. You must older {self._age} years')


class ValueEnumValidator:

    def __init__(self, *values, deny=False):
        self._values = values
        self._deny = deny

    def __call__(self, value):
        for v in self._values:
            if (v == value) == self._deny:
                raise serializers.ValidationError(
                    f'{value} not allowed in this case. {self._values} is {"deny" if self._deny else "required" }'
                )


def rambler_ban_validator(email):
    if 'rambler.ru' in email:
        raise serializers.ValidationError(f'rambler.ru not allowed')
