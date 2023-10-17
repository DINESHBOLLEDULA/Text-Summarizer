import re

def preprocess_text(text):
    # Use a regular expression to find and remove text within square brackets.
    cleaned_text = re.sub(r'\[.*?\]', '', text)

    return cleaned_text
