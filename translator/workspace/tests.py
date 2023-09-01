#write a unit test for the function TranslatorModel.translate, where if input is "Hello" and language is "French", the output is "Bonjour".
#write a unit test for the function TranslatorModel.translate, where if input is "Hello" and language is "Spanish", the output is "Hola".

# Path: gpt-engineer/projects/translator2/workspace/translator_controller.py
# Compare this snippet from gpt-engineer/projects/translator2/workspace/translator_view.py:

import unittest
from translator_model import TranslatorModel

class TestTranslatorModel(unittest.TestCase):
    def test_translate_hello_to_french(self):
        model = TranslatorModel()
        self.assertEqual(model.translate_text('Hello', language='French'), 'Bonjour')

    def test_translate_hello_to_spanish(self):
        model = TranslatorModel()
        self.assertEqual(model.translate_text('Hello', language='Spanish'), 'Hola')

