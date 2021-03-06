from django.core.exceptions import ValidationError


def validate_nums(value):
    """Проверка, что время приготовления больше-равно 1."""

    if value < 1:
        raise ValidationError(f'время приготовления {value}, должно быть => 1')


def ingred_nums(value):
    """Проверка, что ингредиентов больше-равно 1."""

    if value < 1:
        raise ValidationError(f'ингредиентов {value}, должно быть => 1')
