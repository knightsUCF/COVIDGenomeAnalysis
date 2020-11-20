from Bio import SeqIO



database = {}

# this is the entire fasta file, 500mb+, 10 million lines of data, needs to be downloaded off the site
for record in SeqIO.parse("data/sequences.fasta", "fasta"):
    description_words = record.description.split()
    if description_words[1][1:] not in database:
        database[description_words[1][1:]] = []
    sequence = record.seq
    database[description_words[1][1:]].append(str(sequence))
    
    
 
for i in database:
    print(i, database[i])
