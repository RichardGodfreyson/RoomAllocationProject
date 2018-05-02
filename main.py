import evaluation as ev
from collections import Counter

nationalityDiversity = ev.diversity(Counter(ev.inputNationality()))
print(nationalityDiversity) 