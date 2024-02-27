import re

camel_case_str = "TheEnderDragonIsTheFinalBossInMinecraftAndCanBeFoundInTheEndDimension."
snake_case_str = re.sub(r'(?<!^)(?=[A-Z])', '_', camel_case_str).lower()
print(snake_case_str)
