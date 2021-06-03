file_name = input("input file: ")

#f = open("data/test.csv")
f = open(file_name)

data = f.readlines()

for line in data:
    print(line)
