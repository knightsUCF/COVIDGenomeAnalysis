from difflib import SequenceMatcher




class Protein():

    def DetermineSimilarity(self, protein_records):
        for protein in protein_records:
            compare_to = protein_records[protein][0] # compare everything to the first protein record, can also compare to a selected sequence
            print('Starting similarity analysis for protein: ', protein)
            for record in protein_records[protein]:
                how_similar = SequenceMatcher(None, compare_to, record).ratio()
                print(how_similar)
                
              
    def DetermineSimilarityByProtein(self, protein_records, protein_name):
        compare_to = protein_records[protein_name][0] # compare everything to the first protein record, can also compare to a selected sequence
        for record in protein_records[protein_name]:
            how_similar = SequenceMatcher(None, compare_to, record).ratio()
            print(how_similar)
                
                
    def GetAllLabeledProteinNames(self, protein_records):
        protein_names = []
        for protein in protein_records:
            protein_names.append(protein)
        return protein_names

                
