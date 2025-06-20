import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # use the setter to validate input

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, str):
            self._value = val
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        # Use regular expressions to split on ., ! or ?
        split_sentences = re.split(r'[.!?]', self._value)
        # Filter out any empty strings or whitespace-only strings
        valid_sentences = [s for s in split_sentences if s.strip()]
        return len(valid_sentences)
