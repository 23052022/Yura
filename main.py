file = open("result.txt", "w+")
while True:
    s=input("Enter:")
    if not s:
        break
    file.write(s+"\n")
file.close
