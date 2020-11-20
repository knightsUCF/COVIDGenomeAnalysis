from Bio import SeqIO


# download from: https://www.ncbi.nlm.nih.gov/sars-cov-2/


class Records():

    def GetAllProteinSequences(self, file_path):
        print('Categorizing protein sequences...\n')
        database = {}
        for record in SeqIO.parse(file_path, "fasta"):
            description_words = record.description.split()
            if description_words[1][1:] not in database:
                database[description_words[1][1:]] = []
            sequence = record.seq
            database[description_words[1][1:]].append(str(sequence))
        return database
