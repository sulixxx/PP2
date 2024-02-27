import re

text = "HerobrineWasHereDestroyingBlocksAndCausingChaosInTheWorld."
words = re.findall('[A-Z][^A-Z]*', text)
print(words)
