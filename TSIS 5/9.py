import re

text = "NotchWasTheCreatorOfMinecraftAndTheFirstToEnterTheWorldOfBlocks."
new_text = re.sub(r'(?<!^)(?=[A-Z])', ' ', text)
print(new_text)
