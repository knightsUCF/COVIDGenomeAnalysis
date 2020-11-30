import pprint
import numpy as np
import collections




class MotifX():

    def __init__(self):
        self.motif_x = [
            'AAC',
            'AAT',
            'ACC',
            'ATC',
            'ATT',
            'CAG',
            'CTC',
            'CTG',
            'GAA',
            'GAC',
            'GAG',
            'GAT',
            'GCC',
            'GGC',
            'GGT',
            'GTA',
            'GTC',
            'GTT',
            'TAC',
            'TTC'
        ]


    def is_valid(self, sequence):
        contains_at_least_3_codons_flag = False
        contains_at_least_2_unique_codons_flag = False
        in_motif_x_list_flag = True
        x_unique = np.array(sequence)
        unique_data_points = np.unique(x_unique)

        # check whether the sequence contains at least 3 codons
        if len(sequence) > 2:
            contains_at_least_3_codons_flag = True

        # check that there are more than or equal to 2 unique codons
        if len(unique_data_points) > 1:
            contains_at_least_2_unique_codons_flag = True

        # check if the items of the sequence list are found in the motif x list
        for i in sequence:
            if i in self.motif_x:
                pass
            else:
                in_motif_x_list_flag = False

        return contains_at_least_3_codons_flag and contains_at_least_2_unique_codons_flag and in_motif_x_list_flag


    def get_segments(self, nucleotides):
        # returns a dictionary with the location (index in the genome) and length of each segment

        motif_x_sequence_lengths = {}

        i = 0
        while i < len(nucleotides):
            start = i
            end = start + 3
            if self.is_valid(nucleotides[start:end]):
                while end < len(nucleotides) and \
                        self.is_valid(nucleotides[start:end + 1]):
                    end += 1
                motif_x_sequence_lengths[start] = end - start
                i = end
            else:
                i += 1

        return motif_x_sequence_lengths


    def get_segments_by_rank(self, nucleotides):
        segments = self.GetSegments(nucleotides)
        ranked_by_index = collections.OrderedDict(sorted(segments.items(), key=lambda kv: kv[1]))

        output = pprint.PrettyPrinter(indent=4)
        output.pprint(ranked_by_index)

        return ranked_by_index



    def calculate_motif_x_percent_magnitude(self, motif_x_segment_length, total_length):
        return motif_x_segment_length / total_length * 100




