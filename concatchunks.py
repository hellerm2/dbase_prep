"""
concatchunks.py

This script reads pickled chunks containing names and Morgan fingerprints (numpy arrays)
created with bv2np.py and concats the chunks into one giant dataframe.
Results are saved as a pickle.

"""

import glob
import pandas as pd

path = "/home/mheller/Python_github/dbase_prep/"
files = glob.glob("58_morgan_csr_*.pkl")

print("\n\n")

# Name of the giant pickle
giant_pickle = path + "58_morgan_csr.pkl"

print("Concatenating small pickles ...\n")

giant_df = pd.concat([pd.read_pickle(fp) for fp in files], ignore_index=True)

print("Writing giant pickle to {}\n\n".format(giant_pickle))

giant_df.to_pickle(giant_pickle)
