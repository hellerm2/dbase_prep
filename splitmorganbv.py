"""
splitmorganbv.py

This script reads a pickle containing names and Morgan fingerprints (bit vectors)
created with molobj2morganbv.py and splits it into pickle chunks to prevent
memory issues when working with large compound databases.

"""

# Name of the pickle file containing fingerprints as bit vectors
bv_pickle_in = "58_morgan_bv.pkl"

# How many chunks do you want?
n_chunks = 10

import pandas as pd
import numpy as np

# Read pickle from pickle_in
print("\n\n")
print("*** Unpickling %s ..." % bv_pickle_in)

dfrm = pd.read_pickle(bv_pickle_in)

print("")
print("*** Splitting dataframe with {} rows into {} chunks ...\n".format(dfrm.shape[0], n_chunks))

# Define a function that splits the big df
def split(dfrm, chunk_size):
    def index_marks(nrows, chunk_size):
        return range(1 * chunk_size, (nrows // chunk_size + 1) * chunk_size, chunk_size)
    indices = index_marks(dfrm.shape[0], chunk_size)
    return np.split(dfrm, indices)


# Calculate the chunk size (we need to round up!)
chunk_size = int(np.ceil(dfrm.shape[0] / n_chunks))

# Split the big df and save chunks as pickles
chunks = split(dfrm, chunk_size)
i = 0

for c in chunks:
    i += 1
    pickle_name = bv_pickle_in.replace(".pkl", "_" + str(i) + ".pkl")
    c.to_pickle(pickle_name)
    print("Pickling: {}".format(pickle_name))
    
print("")
print("*** Done.\n\n")
