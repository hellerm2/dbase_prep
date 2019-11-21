# dbase_prep

Prepare a compound database for substructure and similarity searches.

The workflow described in this repository starts with a compound database in SMILES format.  Using RDkit, fingerprints for substructure as well as similarity searches will be calculated.

# Requirements

* Compound database in SMILES format
* RDkit
* Numpy
* Pandas
* Scipy
* Glob (for chunked workflow)

# Usage

For larger compound sets (upwards of 6 M compounds), this workflow might fail due to insufficient memory, and the use of a proper database, such as the [RDkit database cartridge](https://www.rdkit.org/docs/Cartridge.html), is recommended.  I haven't had the opportunity to play with the cartridge yet, so as a workaround, calculation of  Morgan Fingerprints can be performed in chunks.

An example file with 58 compounds is provided (`58_smiles.smi`).

## Fingerprinting In One File

1. Convert SMILES into RDkit `mol` object: `python smiles2molobj.py`

   Define `smiles_name`, `pickle_name`, `failed_name` in script

2. Calculate Morgan Fingerprints as Bit Vectors: `python molobj2morganbv.py`

   Define `pickle_in`, `bv_pickle_out`, `radius` in script

3. Convert Morgan FP Bit Vectors into Scipy Sparse Matrices: `bv2csr.py`

   Define `file` in script

## Fingerprinting In Chunks

1. Convert SMILES into RDkit `mol` object: `python smiles2molobj.py`

   Define `smiles_name`, `pickle_name`, `failed_name` in script

2. Calculate Morgan Fingerprints as Bit Vectors: `python molobj2morganbv.py`

   Define `pickle_in`, `bv_pickle_out`, `radius` in script

3. Split the Morgan bv pickle into chunks: `python splitmorganbv.py`

   Define `bv_pickle_in`, `n_chunks` in script

4. Convert Morgan FP Bit Vectors into Scipy Sparse Matrices: `python bv2csr_chunks.py`

   Define `path`, `files` in script

5. Concatenate the chunks: `python concatchunks.py`

   Define `path`, `file`, `giant_pickle` in script

# To-Do

* Improve UI: move arguments from inside scripts to proper command line arguments
