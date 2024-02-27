import re

text = "Alex grabbed his sword and shield, ready to face the challenges ahead in the dangerous wilderness of Minecraft."
pattern = r'a.*?b$'

match = re.search(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match found.")
