from difflib import SequenceMatcher
import operator
import blosum


blosum = blosum.Blosum('blosum.txt')


class Protein:

    def determine_similarity(self, protein_records):
        for protein in protein_records:
            compare_to = protein_records[protein][0] # compare everything to the first protein record, can also compare to a selected sequence
            print('Starting similarity (mutation) analysis for protein: ', protein)
            for record in protein_records[protein]:
                how_similar = SequenceMatcher(None, compare_to, record).ratio()
                print(how_similar)
                
              
    def determine_similarity_by_protein(self, protein_records, protein_name):
        compare_to = protein_records[protein_name][0]
        for record in protein_records[protein_name]:
            how_similar = SequenceMatcher(None, compare_to, record).ratio()
            print(how_similar, ' - ', record)
                
                
    def get_all_labeled_protein_names(self, protein_records):
        protein_names = []
        for protein in protein_records:
            protein_names.append(protein)
        return protein_names


    def determine_frequent_protein_formulas(self, protein_records, protein_name):
        common_protein_formulas = {}
        for record in protein_records[protein_name]:
            if record not in common_protein_formulas:
                common_protein_formulas[record] = 1
            else:
                common_protein_formulas[record] += 1
        common_protein_formulas = dict(sorted(common_protein_formulas.items(), key=operator.itemgetter(1),reverse=True))
        return common_protein_formulas


    # for getting the key with the highest occuring frequency as the baseline to assess mutations from
    # input: protein.DetermineFrequentProteinFormulas(protein_records, protein_name)
    def get_key_with_highest_value(self, dictionary):
        return max(dictionary, key=dictionary.get)


    def calculate_blosum_matrix_on_sequences(self, baseline_sequence, sequences):
        print('Running blosum matrix')
        total_blosum_score = 0
        current_sequence_id = 0
        for current_key, value in sequences.items():
            current_sequence_id += 1
            # skip the first record which we are comparing to, since this is the most frequent
            if current_sequence_id == 1:
                continue
            # only compare sequences of the same length
            if len(baseline_sequence) != len(current_key):
                continue
            # only test the most common frequencies
            if current_sequence_id > 10:
                break
            try:
                for i in range(len(current_key)):
                    # throw out sequences with unknown 'X'
                    if 'X' in current_key:
                        continue
                    if current_key[i] == baseline_sequence[i]:
                        pass
                    else:
                        # ignore missing 'X' data for both the baseline key and match
                        if current_key[i] != 'X' and baseline_sequence[i] != 'X':
                            # print('no match: ', current_key[i], baseline_sequence[i])
                            total_blosum_score += float(blosum.lookup(current_key[i], baseline_sequence[i]))
                print('\nanalysis complete for sequence ID: ', current_sequence_id)
                print('sequence: ', current_key)
                print('sequence frequency out of all records: ', value)
                print('blosum matrix score: ', total_blosum_score, '\n')
                # reset
                total_blosum_score = 0
            except Exception as e:
                print(e)



            







                
