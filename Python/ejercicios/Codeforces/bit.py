tt = input()
last_value = 0
for _ in range(int(tt)):
    statement = input()
    bits = statement.split()
    if(bits[0] == "X++" or bits[0] == "++X"):
        last_value += 1
    else: last_value -= 1
print(last_value)