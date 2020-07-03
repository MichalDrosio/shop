from django.core.exceptions import ValidationError



def number_selphone(value):
    number = str(value)
    if len(number) != 9:
        raise ValidationError('Podaj 9 cyfrowy numer')
    try:
       value = int(value)
    except ValueError:
            raise ValidationError(f'Wpisz tylko cyfry w podanym numerze {value}')


