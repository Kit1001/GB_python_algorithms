import hashlib
import random

string = ''.join(chr(random.randint(97, 122)) for i in range(random.randint(2, 5)))
substring_set = set()
print(string)

for i in range(1, len(string)):
    for j in range(len(string)):
        substring = string[0 + j: i + j]
        substring_hash = hashlib.sha1(substring.encode()).hexdigest()
        if substring_hash not in substring_set:
            substring_set.add(substring_hash)
            print(substring, end=' ')

substring_set = substring_set if len(string) > 1 else '1'
print()
print(len(substring_set))
