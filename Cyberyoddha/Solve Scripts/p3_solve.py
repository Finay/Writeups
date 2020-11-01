import base64

given = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="

given = given.encode("ascii")
given = base64.b64decode(given)

given = given.decode("ascii")
flag = []

for i in given:
    flag += [chr(ord(i) ^ 0x55)]

print("".join(flag))
