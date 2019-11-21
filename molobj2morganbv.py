"""
molobj2morgan.py

This script reads a pickle containing SMILES, names, and mol objects created with
smiles2molobj.py and calculates Morgan Fingerprints as bit vectors.

"""

# Name of the MolPort SMILES file
pickle_in = "58_molobj.pkl"

# Name of the pickle file containing fingerprints as bit vectors
bv_pickle_out = "58_morgan_bv.pkl"

# Radius of Morgan fingerprints
# Morgan2 ~= ECFP4; Morgan3 ~= ECFP6
radius = 3

import pandas as pd
from rdkit.Chem import AllChem
from rdkit.Chem import rdDepictor
rdDepictor.SetPreferCoordGen(True)


# Read pickle from pickle_in
print("\n\n")
print("*** Reading pickle from %s" % pickle_in)

molport_df = pd.read_pickle(pickle_in)

# Add Morgan Fingerprints with radius = 2 and 3
# Morgan2 ~= ECFP4; Morgan3 ~= ECFP6
print("")
print("*** Calculating Morgan Fingerprints with Radius = %i" % radius)

fp_colname = "fp_mrgn" + str(radius)

molport_df[fp_colname] = molport_df['mol'].map(
						lambda mol: AllChem.GetMorganFingerprintAsBitVect(mol, radius)
						)
print("*** Done.")

# Fingerprints are calculated; smiles and mol objects not needed anymore.

print("")
print("Dropping SMILES and Mol Object column")

molport_df.drop(['smiles', 'mol'], axis=1, inplace=True)
						
print("")
print("Saving Dataframe with bit vector fingerprints as %s" % bv_pickle_out)

molport_df.to_pickle(bv_pickle_out)

print("*** Done.")
print("\n\n")
