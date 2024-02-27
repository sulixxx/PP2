import re

text = "Steve_mined_diamonds_with_his_trusty_pickaxe_and_explored_dark_caves_in_search_of_rare_resources."
pattern = r'[a-z]+_[a-z]+'

matches = re.findall(pattern, text)
print(matches)
