import re

text = "The Creeper sneaked silently through the dense forest, its eyes glowing in the darkness."
pattern = r'[A-Z][a-z]+'

matches = re.findall(pattern, text)
print(matches)
