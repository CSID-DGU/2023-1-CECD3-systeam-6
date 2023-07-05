from rdkit import Chem

sdf_file = "BindingDB_ChEMBL_2D.sdf"

with open(sdf_file, "r") as f:
    block_started = False
    mol_block = ""
    for line in f:
        if line.startswith("$$$$"):
            if block_started:
                break
            block_started = True
            mol = Chem.MolFromMolBlock(mol_block, sanitize=False)
            if mol is not None:
                smiles = Chem.MolToSmiles(mol)

        elif line.startswith("> <BindingDB Target Chain Sequence>"):
            protein_sequence = next(f).strip()
        mol_block += line

# 결과 출력
print("Ligand SMILES:", smiles)
print("Protein Sequence:", protein_sequence)
