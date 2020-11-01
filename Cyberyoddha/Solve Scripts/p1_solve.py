with open("/root/Documents/CTFs/CyberYoddha/password1.py") as red:
    lines = red.readlines()[5:48]

final = range(len(lines))

for line in lines:
    p1 = int(line.split("[")[1].split("]")[0])
    p2 = line.split("'")[1]
    final[p1] = p2

print("".join(final))
