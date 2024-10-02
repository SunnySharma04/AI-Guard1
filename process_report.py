import re

# Function to clean the uploaded audit report
def clean_report(report):
    # Basic text cleaning (remove unwanted characters, headers, etc.)
    cleaned = re.sub(r'\s+', ' ', report)  # Replace multiple whitespaces with a single space
    cleaned = re.sub(r'(\n|\r)', ' ', cleaned)  # Remove newline characters
    cleaned = re.sub(r'[^a-zA-Z0-9\s.,;?!-]', '', cleaned)  # Remove special characters except basic punctuation
    return cleaned
