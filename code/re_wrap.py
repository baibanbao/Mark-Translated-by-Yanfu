import re

def remove_newlines(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        pattern = r'\n'
        new_text = re.sub(pattern, '', text).strip()
    return new_text

input_file = 'input_text.txt'
output_text = remove_newlines(input_file)

print(output_text)
