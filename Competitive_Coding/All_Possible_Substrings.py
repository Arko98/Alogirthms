# Method 1 
from itertools import combinations
all_substrings = [s[x:y] for x,y in combinations(range(len(s)+1),r=2)]

# Method 2
all_substrings = []
for length in range(1, len(s)+1):
    for start in range(len(s) - length + 1):
        end = start + length - 1
        all_substrings.append(s[start:end+1])