f = open("khmerdata.csv", 'r', encoding='utf-16')
lines = f.readlines()
nf = open("khmerdataupdated.csv", 'w', encoding='utf-16')

for line in lines:
    segment = line.split('\t')
    length = int(segment[4]) - int(segment[3])
    #find the videos that are longer than 45 seconds, then do nothing with them! Copy only videos with less time to new document
    if length > 4500:
        continue
    else:
        nf.write(line)

f.close()
nf.close()