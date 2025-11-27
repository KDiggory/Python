
#given rna string s 
#return protein encoded

import pandas as pd

column_names = ["codon", "amino_acid"]
codon_data = pd.read_csv('rnacodon.csv', names=column_names)

rna = "AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"

def to_protein(codon_data, rna):
    protein = []
    for i in range(3, len(rna) +1,3):
        #loop through codons to match it
        for j in range(len(codon_data)):
            if rna[i-3:i] == codon_data.codon[j]:
                protein.append(codon_data.amino_acid[j])
    protein = ''.join(protein)
    return()

to_protein(codon_data, rna)


    