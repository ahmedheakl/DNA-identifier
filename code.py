#importing libraries
from sys import argv, exit
import csv

if len(argv) != 3:
    print("Entry error")
    
    
def find_max(s, sub):
    ans = [0] * len(s) 
    for i in range(len(s) - len(sub), -1, -1):
        if s[i: i + len(sub)] == sub:
            if i + len(sub) > len(s) - 1:
                ans[i] = 1
            else:    
                ans[i] = 1 + ans[i + len(sub)]
    return max(ans)
    
    
def print_match(csvv, actual):
    for row in csvv:
        # print(row[1:])
        if row[1:] == actual:
            print(row[0])
            exit(0)
    print("No match")
    exit(0)
    
    
csv_domain = argv[1]
text_domain = argv[2]
with open(csv_domain, "r") as csvv:
    csvvreader = csv.reader(csvv)
    all_seq = next(csvvreader)[1:]
    with open(text_domain, "r") as text:
        textreader = text.read()
        actual = []
        for seq in all_seq:
            actual.append(f'{find_max(textreader, seq)}')
    print_match(csvvreader, actual) 
