from prompt_toolkit.validation import Validator, ValidationError

template = ['Please enter a valid range number',
            'Please enter valid number',
            'Sorry... u can\'t scrape zero or negative',
            'Uppss... Out of limit. My API can be banned :(']


def returnValidation(document, custom_message):
    return ValidationError(
        message=custom_message,
        cursor_position=len(document.text))


class RangeScrapeValidator(Validator):
    def validate(self, document):

        _ok = document.text.isnumeric()
        if _ok:
            numeric = int(document.text)
            inRange = 1 <= numeric <= 7

            if not inRange:
                raise returnValidation(document, template[0])
        else:
            raise returnValidation(document, template[1])


class RangeTweetsValidator(Validator):

    def validate(self, document):

        _ok = document.text.isnumeric()
        if _ok:
            numeric = int(document.text)
            lowerOutRange = numeric <= 0
            upperOutRange = numeric > 10000

            if lowerOutRange:
                raise returnValidation(document, template[2])
            elif upperOutRange:
                raise returnValidation(document, template[3])
        else:
            raise returnValidation(document, template[1])
