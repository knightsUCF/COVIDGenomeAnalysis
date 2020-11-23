from difflib import SequenceMatcher




class Protein():

    def DetermineSimilarity(self, protein_records):
        for protein in protein_records:
            compare_to = protein_records[protein][0] # compare everything to the first protein record, can also compare to a selected sequence
            print('Starting similarity (mutation) analysis for protein: ', protein)
            for record in protein_records[protein]:
                how_similar = SequenceMatcher(None, compare_to, record).ratio()
                print(how_similar)
                
              
    def DetermineSimilarityByProtein(self, protein_records, protein_name):
        compare_to = protein_records[protein_name][0] # compare everything to the first protein record, can also compare to a selected sequence
        for record in protein_records[protein_name]:
            how_similar = SequenceMatcher(None, compare_to, record).ratio()
            print(how_similar, ' - ', record)
                
                
    def GetAllLabeledProteinNames(self, protein_records):
        protein_names = []
        for protein in protein_records:
            protein_names.append(protein)
        return protein_names


    def DetermineFrequentProteinFormulas(self, protein_records, protein_name):
        common_protein_formulas = {}
        for record in protein_records[protein_name]:
            if record not in common_protein_formulas:
                common_protein_formulas[record] = 1
            else:
                common_protein_formulas[record] += 1
        common_protein_formulas =  dict(sorted(common_protein_formulas.items(), key=lambda item: item[1]))
        return common_protein_formulas



            







                
