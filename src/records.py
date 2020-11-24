from Bio import SeqIO


# download from: https://www.ncbi.nlm.nih.gov/sars-cov-2/ (protein)


class Records():

    def get_all_protein_sequences(self, file_path):
        print('Categorizing protein sequences...\n')
        proteins = {}
        for record in SeqIO.parse(file_path, "fasta"):
            labels = record.description.split()
            if labels[1][1:] not in proteins:
                proteins[labels[1][1:]] = []
            sequence = record.seq
            proteins[labels[1][1:]].append(str(sequence))
        return proteins
