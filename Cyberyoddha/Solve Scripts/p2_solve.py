given = "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"

flag = ["A" for i in range(47)]

for i in range(0, 9):
    flag[i] = given[i]
for i in range(9, 24):
    flag[i] = given[32 - i]
for i in range(24, 47, 2):
    flag[i] = given[70 - i]
for i in range(45, 25, -2):
    flag[i] = given[i]

print("".join(flag))
