text="hello World"
print(text.upper()) # Convert to uppercase
print(text.lower()) # Convert to lowercase 
print(text.capitalize()) # Capitalize the first letter
print(text.title()) # Capitalize the first letter of each word
print(text.count('l')) # Count occurrences of 'l'
print(text.find('W')) # Find the index of 'W'
print(text.center(20,'|')) # Center the text with '|' padding
print("hello\nworld") # new line
print("hello\tworld") # tab space
teXt="hello\tworld1"
string=" "
print(teXt.expandtabs(100)) # Expand tabs to 100 spaces
print(text.isalnum()) # Check if all characters are alphanumeric but if text have space it will return False
print(text.isdigit()) # Check if all characters are digits but if text have space it will return False
print(text.islower()) # Check if all characters are lowercase but if text have space it will
print(text.isupper()) # Check if all characters are uppercase but if text have space it will return False
print(string.isspace()) # Check if all characters are whitespace but if text have space it will return False
print(text.startswith('hello')) # Check if text starts with 'hello'
print(text.endswith('World')) # Check if text ends with 'World'
print(text.isalpha()) # Check if all characters are alphabetic but if text have space it will return False
print(text.split()) # Split the text into a list of words
print(text.partition('l')) # Split the text by 'l' but only at first occurrence 