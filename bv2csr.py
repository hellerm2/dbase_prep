"""
bv2np.py

This script reads a pickle containing names and Morgan fingerprints (bit vectors)
created with molobj2morganbv.py and converts the fingerprints from bit vectors
into scipy sparse matrices via numpy arrays.  Results are saved in a pickle.

"""

import pandas as pd
import numpy as np
import scipy.sparse as sp

from rdkit import DataStructs

file = "58_morgan_bv.pkl"

# Convert Morgan fingerprints from Bit Vector format into
# scipy sparse matrices arrays for use with Scikit-Learn

def bv_to_csr(fp):
    tmp_arr = np.zeros((0,))
    DataStructs.ConvertToNumpyArray(fp, tmp_arr)
    arr = sp.csr_matrix(tmp_arr)
    return arr
 
# Read the bit vector pickle
print("\n\n")
print("*** Reading {}\n".format(file))
df = pd.read_pickle(file)
    
# Convert bit vector to numpy array
fp_col = df.columns[1]
csr_col = fp_col.replace("fp", "csr")
df[csr_col] = df[fp_col].map(lambda fp: bv_to_csr(fp))
    
# Drop the bit vector column
df.drop(fp_col, axis=1, inplace=True)
    
# Save the converted pickle
file_out = file.replace("_bv", "_csr")

print("Saving pickle {}".format(file_out.split("/")[-1]))
print("\n\n")

df.to_pickle(file_out)
