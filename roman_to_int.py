ip = input().split(', ')
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
res = 0
for j in range(len(ip)):
    res = 0
    rm = ip[j]
    i = 0
    while i < len(rm) - 1:
        if rm[i] not in set(d.keys()):
            print(f"Invalid input {i} so ignored and moved forward")
        else:
            if d.get(rm[i + 1]) > d.get(rm[i]):
                res += (d.get(rm[i + 1]) - d.get(rm[i]))
                i += 2
            else:
                res += d.get(rm[i])
                i += 1

    if i<len(rm):
        res+=d.get(rm[-1])
    print(f"{ip[j]}->{res}")
