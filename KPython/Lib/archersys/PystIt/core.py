note = " "
while True:
    try:
        line = input()
    except EOFError:
        break
    if not line:
        break
    note = note + " " + line
print(note)
