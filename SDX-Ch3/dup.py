import sys
import os
from hashlib import sha256

def find_groups(filenames):
    groups = {}
    output = open("output.txt", 'w')
    for fn in filenames:
        data = open(fn, "rb").read()
        hash_code = sha256(data).hexdigest()

        output.write(str(hash_code) + "\n")
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)

    for fn in filenames:
        if fn in open("output.txt").read():
            print("duplicate found!")

    return groups
        
    
if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))

