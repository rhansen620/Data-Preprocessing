import sox
import os

# assign directory
directory = '1296_chunks'

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    n_samples = sox.file_info.num_samples(f)
    print(n_samples)
    #if no samples, print name of file
    if n_samples == None:
        print(f)