f = open("khmerdataupdated.csv", 'r', encoding='utf-16')
lines = f.readlines()

for line in lines:
    segment = line.split('\t')
 #   print(segment)
    length = int(segment[4]) - int(segment[3])
    #find the videos that are longer than 45 seconds and print its name
    if length > 4500:
        print(segment[1])


