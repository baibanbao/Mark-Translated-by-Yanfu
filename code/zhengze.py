import re

def remove_line_numbers(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()
        pattern = r'\d+:\d+\s'
        new_text = re.sub(pattern, '', text)
    return new_text

input_file = 'input_text.txt'
output_text = remove_line_numbers(input_file)

print(output_text)
