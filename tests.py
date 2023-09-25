from helpers import remove_letter_templates
import json

with open('./data/test.json') as file:
    data = json.load(file)


def test_remove_letter_templates():
    request = {
        "description": "Hello [START]World[END]",
        "law": {
            "letter_start": "[START]",
            "letter_end": "[END]"
        }
    }
    expected_output = "Hello World"
    assert remove_letter_templates(request) == expected_output
    assert  isinstance(remove_letter_templates(data), str)
    # Add more test cases here
