snake_case_str = "the_ender_dragon_soared_high_above_the_end_island,_its_massive_wings_casting_a_dark_shadow_over_the_land."
camel_case_str = ''.join(word.capitalize() for word in snake_case_str.split('_'))
camel_case_str = camel_case_str[0].lower() + camel_case_str[1:]  # Lowercase the first character
print(camel_case_str)
