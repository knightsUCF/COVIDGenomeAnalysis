from difflib import SequenceMatcher
from numba import jit



class Protein():

    '''
    records = Records()
    file_path = 'sequences.fasta'
    protein_records = records.GetAllProteinSequences(file_path)

    DetermineSimilarity(protein_records)
    '''

    # warning: this can crash if computer specs are not enough to process 10 million lines in the complete record
    # @jit(nopython=True)
    def DetermineSimilarity(self, protein_records):
        for protein in protein_records:
            compare_to = protein_records[protein][0] # compare everything to the first protein record, can also compare to a selected sequence
            print('Starting similarity analysis for protein: ', protein)
            for record in protein_records[protein]:
                how_similar = SequenceMatcher(None, compare_to, record).ratio()
                print(how_similar)


'''
records = Records()
protein = Protein()


file_path = 'sequences.fasta'
protein_records = records.GetAllProteinSequences(file_path)

protein.DetermineSimilarity(protein_records)
'''
