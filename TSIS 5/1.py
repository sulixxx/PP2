import re

text = "In Minecraft, you can craft various items, like a block of wood or a bucket of lava, or even an abundance of diamonds!"
pattern = r'ab*'

matches = re.findall(pattern, text)
print(matches)
