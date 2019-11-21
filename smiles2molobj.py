"""
smiles2molobj.py

This script reads a SMILES file and converts the SMILES to RDkit mol objects.
Pattern fingerprints for substructure searches are included in the mol objects.
Molecules that fail sanitization will be saved in a CSV file.

A pandas dataframe containing the SMILES, names, and mol objects will be saved as a pickle.
"""

# Name of the MolPort SMILES file
smiles_name = "58_smiles.smi"

# Name of the pickle file
pickle_name = "58_molobj.pkl"

# Name of the failed molecules file
failed_name = "58_failed.csv"

import pandas as pd
from rdkit.Chem import PandasTools
from rdkit.Chem import rdDepictor
rdDepictor.SetPreferCoordGen(True)

# Load MolPort db into a dataframe from SMILES file
print("\n\n")
print("*** Reading SMILES")

molport_df = pd.read_csv(smiles_name,
			 delim_whitespace=True,
			 header=None,
			 names=['smiles', 'molport_id'])

print("*** Done.")						

# Add RDkit mol objects including pattern fingerprint for substructure searches

print("")
print("*** Creating Molecule Objects from SMILES")
PandasTools.AddMoleculeColumnToFrame(molport_df, 'smiles', 'mol', includeFingerprints=True)
print("*** Done.")

# Extract rows where SMILES could not be converted into
# molecules.  Save them in a file for analysis.

print("")
print("*** Extracting missing Mol objects")

# First, we create a Boolean mask for all rows
# where 'mol' is None
failed_mol = molport_df.mol.isnull()

# Now filter the dataframe using the mask
failed_molport_df = molport_df[failed_mol]
print("*** Done.") 

# Now clean the dataframe: get rid of all rows
# where SMILES could not be converted into molecules
print("")
print("*** Cleaning dataframe")

molport_df = molport_df.dropna()

print("*** Done.")

# Finally, save the molport dataframe as pickle ...
print("")
print("*** Saving %i molecules in a pickled dataframe as %s." % (molport_df.shape[0], pickle_name))
molport_df.to_pickle(pickle_name)
print("*** Done.")

# ... and save the failed molecules in a CSV file
print("")
print("*** Saving %i failed molecules in SMILES format as %s." % (failed_molport_df.shape[0], failed_name))
cols = ['smiles', 'molport_id']
failed_molport_df.to_csv(failed_name, columns=cols, header=False, index=False, sep=" ")
print("*** Done.\n\n")
