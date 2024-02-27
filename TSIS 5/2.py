import re

text = "The rabbit hopped across the grassy plains, nibbling on a carrot and digging a burrow with its powerful hind legs."
pattern = r'ab{2,3}'

matches = re.findall(pattern, text)
print(matches)
