import io

with io.open("input9-1.txt", "r") as f:
    dt = f.read()

s = []
m = [v for v in dt.split("\n") if len(v) > 0]
for j, r in enumerate(m):
    for i, c in enumerate(r):
        #print(j, i, c) # check up, down, left, right (skipping edge cases)
        if not j == 0: # UP
            u = int(m[j-1][i])
            if u < int(c):
                continue
        
        if not j == len(m) - 1: # DOWN
            b = int(m[j+1][i])
            if b < int(c):
                continue

        if not i == 0: #LEFT
            l = int(m[j][i-1])
            if l < int(c):
                continue
        
        if not i == len(r) - 1: # RIGHT
            rt = int(m[j][i+1])
            if rt < int(c):
                continue
        
        s.append(int(c) + 1) # NOTE: unclear if I need + 1 but it doesn't work?

print("Res 1=", sum(s))