import re

#work in progress
def contains(items, value):
    for i in items:
        #print(i, i[0][1], value)
        if len(i) > 0 and i[0][1] == value:
            #print(True)
            return True
    return False

with open('input.txt', 'r') as f:
    lines = f.readlines()

pattern = re.compile("([0-9]+) ([a-z]+ [a-z]+)")
bags = {}
for line in lines:
    line = line.replace(" bags", "").replace(" bag", "").replace(".\n", "")
    outer, inner = line.split(' contain ')

    inner = inner.split(', ')
    inner = [pattern.findall(x) for x in inner]
    print(outer, inner)
    bags[outer]=inner

print(bags)
targets = set()
targets.add('shiny gold')
result = set()

while len(targets)>0:
    current = targets.pop()
    for k, v in bags.items():
        if contains(v, current):
            result.add(k)
            targets.add(k)

print(len(result), result)


