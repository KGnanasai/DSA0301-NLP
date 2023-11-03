import re

# Sample text to search for patterns
text = "Hello, my email is john.doe@example.com and my phone number is 123-456-7890."

# Define a regular expression pattern for email addresses
email_pattern = r'\b[\w\.-]+@[\w\.-]+\.\w+\b'

# Define a regular expression pattern for phone numbers
phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'

# Use the re.search() function to find the first match of the email pattern
email_match = re.search(email_pattern, text)
if email_match:
    print("Email found:", email_match.group())

# Use the re.findall() function to find all matches of the phone number pattern
phone_matches = re.findall(phone_pattern, text)
if phone_matches:
    print("Phone numbers found:", phone_matches)
