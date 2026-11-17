# Version 2: Student Information Formatter using string methods

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
section = input("Enter section: ")
favorite_subject = input("Enter favorite subject: ")

raw_full_name = first_name.strip() + " " + last_name.strip()

formatted_name = raw_full_name.title()
name_code = raw_full_name.upper()
formatted_section = section.strip().upper()
formatted_subject = favorite_subject.strip().title()
character_count = len(formatted_name)

print("\nFormatted Output:")
print("Name:", formatted_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Favorite Subject:", formatted_subject)
print("Character Count:", character_count)
