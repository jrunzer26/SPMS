
def hash1(x):
    return x*x + 3

def hash2 (x):
    return 7 * x + 9

def hash3 (x):
    return 2* x * x - 3* x -5


list =  [12,15,19,11,5,9,14]
h1 = []
h2 = []
h3 = []
h = []



for e in list:
    h1.append(hash1(e))
    h2.append(hash2(e))
    h3.append(hash3(e))

for i in range(0,len(list)):
    h.append((h1[i] + h2[i] *h3[i]) % 5)

print list
print h1
print h2
print h3
print h






