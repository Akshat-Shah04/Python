import re

text = "You can reach me at 123-456-7890."
pattern = r"\d{3}-\d{3}-\d{4}"
pattern2 = r"\d{3}-\d{4}-\d{4}"

match = re.search(pattern, text)
match2 = re.search(pattern2,text)
if match:
    print(f"Phone number found: {match.group()}")
else:
    print("No phone number found.")

if match2:
    print(f"Phone number found: {match2.group()}")
else:
    print("No phone number found.")

'''
Phone number found: 123-456-7890
No phone number found.

'''