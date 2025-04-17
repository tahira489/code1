file = open('sample.txt','r')
file3 = open('sample1.txt','w')

for line in file1.readlines():
    if not (line.startswith("study")):
        print(line)
        file3.write(line)

file.close()
file3.close()
