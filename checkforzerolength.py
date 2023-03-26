f = open("khmerdata.csv", 'r', encoding='utf-16')
lines = f.readlines()

for line in lines:
    segment = line.split('\t')
    length = int(segment[4]) - int(segment[3])
  #  if length == 0:
    #    print(segment[1])
    if length <= 1000:
        print(segment[1])
        print (length)