"""
bv2np.py

This script reads pickled chunks containing names and Morgan fingerprints (bit vectors)
created with molobj2morganbv.py and splitmorgan.py and converts the chunked fingerprints
from bit vectors into scipy sparse matrices via numpy arrays.  Results are saved in chunked pickles.

"""

import glob
import pandas as pd
import numpy as  np
import scipy.sparse as sp

from rdkit import DataStructs

path = "/home/mheller/Python_github/dbase_prep/"
files = glob.glob("58_morgan_bv_*.pkl")

# Convert Morgan fingerprints from Bit Vector format into
# scipy sparse matrices arrays for use with Scikit-Learn

def bv_to_csr(fp):
    tmp_arr = np.zeros((0,))
    DataStructs.ConvertToNumpyArray(fp, tmp_arr)
    arr = sp.csr_matrix(tmp_arr)
    return arr
 
print("\n\n")

for f in files:
    
    # Read the chunk
    print("*** Reading {}".format(f))
    df = pd.read_pickle(f)
    
    # Convert bit vector to numpy array
    fp_col = df.columns[1]
    csr_col = fp_col.replace("fp", "csr")
    df[csr_col] = df[fp_col].map(lambda fp: bv_to_csr(fp))
    
    # Drop the bit vector column
    df.drop(fp_col, axis=1, inplace=True)
    
    # Save the converted pickle
    f_out = f.replace("_bv_", "_csr_")
    df.to_pickle(f_out)

    print("Working on {}\n".format(f_out.split("/")[-1]))
    
