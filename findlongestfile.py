f = open("khmerdata.csv", 'r', encoding='utf-16')
lines = f.readlines()

longest = 0
for line in lines:
    segment = line.split('\t')    
    length = int(segment[4]) - int(segment[3])
    if length > longest:
        longest = length
    else:
        continue
print(longest)
