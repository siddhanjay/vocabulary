#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vocabulary import Vocabulary as vb
import unittest
import sys
try:
    import simplejson as json
except ImportError:
    import json



class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_meaning_valid_phrase(self):
        current_result = vb.meaning("humming")
        result = '[{"seq": 0, "text": "Present participle of hum."}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):  ## python 2 
            self.assertItemsEqual(current_result, expected_result)
        else:       # python 3
            """
            assertItemsEqual() was renamed to assertCountEqual() 
            Why I am not using assertEqual() here? 

            Reference: 
            - http://stackoverflow.com/a/7473137/3834059
            - https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertItemsEqual
            - https://docs.python.org/3/library/unittest.html?highlight=assertcountequal#unittest.TestCase.assertCountEqual
            """

            self.assertCountEqual(current_result, expected_result)

    def test_meaning_not_valid_phrase(self):
        current_result = vb.meaning("sxsw")
        self.assertIsNone(current_result)
        
    def test_synonym_valid_phrase(self):
        current_result = vb.synonym("repudiate")
        result = '[{"seq": 0, "text": "deny"}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_synonym_not_valid_phrase(self):
        current_result = vb.synonym("sxsw")
        self.assertIsNone(current_result)
        
    def test_antonym_valid_phrase_1(self):
        current_result = vb.antonym("love")
        result = '{"text": ["hate"]}'
        expected_result = json.loads(result)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_antonym_valid_phrase_2(self):
        current_result = vb.antonym("respect")
        result = '{"text": ["disesteem", "disrespect"]}'
        expected_result = json.loads(result)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_antonym_not_valid_phrase(self):
        current_result = vb.antonym("sxsw")
        self.assertIsNone(current_result)

    def test_partOfSpeech_valid_phrase_1(self):
        current_result = vb.part_of_speech("hello")
        result = '[{"text": "interjection", "example:": "Used to greet someone, answer the telephone, or express surprise.", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_partOfSpeech_valid_phrase_2(self):
        current_result = vb.part_of_speech("rapidly")
        result = '[{"text": "adverb", "example:": "With speed; in a rapid manner.", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_partOfSpeech_not_valid_phrase(self):
        current_result = vb.part_of_speech("sxsw")
        self.assertIsNone(current_result)

    def test_usageExamples_valid_phrase(self):
        current_result = vb.usage_example("hillock")
        result = '[{"seq": 0, "text": "I went to the to of the hillock to look around."}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_usageExamples_not_valid_phrase(self):
        current_result = vb.usage_example("lksj")
        self.assertIsNone(current_result)

    def test_pronunciation_valid_phrase(self):
        current_result = vb.pronunciation("hippopotamus")
        result = '[{"rawType": "ahd-legacy", "raw": "(hĭpˌə-pŏtˈə-məs)", "seq": 0}, {"rawType": "arpabet", "raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "seq": 0}]'
        expected_result = json.loads(result)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_pronunciation_not_valid_phrase(self):
        current_result = vb.pronunciation("lksj") # for non valid word
        self.assertIsNone(current_result)

    def test_hyphenation_valid_phrase(self):
        current_result = vb.hyphenation("hippopotamus")
        result = '[{"seq": 0, "text": "hip", "type": "secondary stress"}, {"seq": 1, "text": "po"}, {"seq": 2, "text": "pot", "type": "stress"}, {"seq": 3, "text": "a"}, {"seq": 4, "text": "mus"}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_hyphenation_not_valid_phrase(self):
        current_result = vb.hyphenation("sxsw")
        self.assertIsNone(current_result)

    def test_translate_valid_phrase(self):
        current_result = vb.translate("hummus", "en", "es")
        result = '[{"text": "hummus", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(current_result, expected_result)
        else:
            self.assertCountEqual(current_result, expected_result)

    def test_translate_not_valid_phrase(self):
        current_result = vb.translate("asldkfj", "en", "ru")
        self.assertIsNone(current_result, False)

if __name__ == "__main__":
    unittest.main()
