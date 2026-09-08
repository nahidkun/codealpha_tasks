import os
import re

def extract_emails_from_file(file_path):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return []
    with open(file_path, 'r') as file:
        content = file.read()
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, content) 
    return emails

def save_emails_to_file(emails, output_file):
    with open(output_file, 'w') as file:
        for email in emails: 
            file.write(email + '\n')

path = 'C:\\Users\\nahid\\OneDrive\\Ambiente de Trabalho\\codealpha tasks\\automation\\emails.txt'
emails = extract_emails_from_file(path)
save_emails_to_file(emails, 'extracted_emails.txt')





