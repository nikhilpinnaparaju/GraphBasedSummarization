f = open("../wordscores.txt")

sys = f.readlines()

f.close()

for i in range(len(sys)):
    sys[i] = sys[i].replace('\n','')
    sys[i] = sys[i].split(' ')

# print(sys)

f = open("../annotated_keys.txt")

man = f.readlines()

f.close()

for i in range(len(man)):
    man[i] = man[i].replace('\n','')
    man[i] = man[i].split(' ')

# print(man)

cor = 0

for i in range(len(man)):
    for j in man[i]:
        for k in range(len(man)):
            if j==sys[k][0]:
                # print(j,sys[k][0])
                cor = cor + 1

print(cor)

flat = []

print(len(man))

for sublist in man:
    for item in sublist:
        flat.append(item)

print(len(flat))