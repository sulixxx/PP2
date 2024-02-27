import re

text = "You_have_finally_reached_the_top_of_the_mountain,_where_a_great_adventure_awaits."
pattern = r'[ ,.]'
replacement = ':'

new_text = re.sub(pattern, replacement, text)
print(new_text)
