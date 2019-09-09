s = "bozgbobbiyobobooboobobbobbobobbobbpfoboboobob"
count = 0
length = int(len(s))
while length > 2:
    for x in s:
        if length <= 2:
            break
        elif x == "b":
            word = "b"
            length -= 1
            break
        else:
            s = s[1:]


    for x in s:
        if length <= 2:
            break
        elif s[1] == "o":
            word += "o"
            length -= 1
            break
        else:
            s = s[1:]
            length -= 1
            word = " "
            break
    for x in s:
        if length <= 2:
            break
        elif s[2] == "b":
            word += "b"
            break
        else:
            s = s[1:]
            length -= 1
            word = " "
            break
    if word == "bob":
         if length <= 2:
             break
         count += 1
         s = s[2:]

    if length <= 2:
        break

print("Number of times bob occurs is: " + str(count))
