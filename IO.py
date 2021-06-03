file_name = input("input file: ")

#f = open("data/test.csv")
f = open(file_name)

text = f.readlines()

for line in text:
    print("text:",line)
