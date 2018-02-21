import fileinput

data = fileinput.input()

print [line for line in data]
