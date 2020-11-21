
# Version 1.1


(add mutation chart here of significant proteins)

Version 1.1 adds the ability to:

- process the entire catalog of downloaded COVID protein sequences from: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049

- in records.py we automatically create an organized list which categorizes each protein variation sequence under the labeled name of the protein


- we can get all available labeled protein names from the database: `protein.GetAllLabeledProteinNames(protein_records)`


- we can get protein similiarities (mutations) by name, since this can save us a lot of time instead of processing all protein mutations `protein.GetAllLabeledProteinNames(protein_records)`


# Downloading All Protein Sequences


Later we will add separate methods for downloading nucleotides versus records.


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


# Organizing Protein Sequences by Individual Protein


# Get All Labeled Protein Names from Records


    import records
    import protein
    
    
    records = records.Records()
    protein = protein.Protein()


    file_path = 'sequences.fasta'
    
    protein_records = records.GetAllProteinSequences(file_path)

    protein.GetAllLabeledProteinNames(protein_records)

    
    '''
    output
    
    Categorizing protein sequences...
    
    leader
    nsp2
    nsp3
    nsp4
    3C-like
    nsp6
    nsp7
    nsp8
    nsp9
    nsp10
    ORF7b
    ORF1a
    RNA-dependent
    helicase
    3'-to-5'
    endoRNAse
    2'-O-ribose
    nsp11
    ORF10
    ORF1ab
    surface
    ORF3a
    envelope
    membrane
    ORF6
    ORF7a
    ORF8
    nucleocapsid
    ORf6
    N
    ORF7b,
    truncated
    Chain
    E
    ORF7a/ORF7b
    ORF1ap
    orf1ab
    orf3a
    orf6
    orf7a
    orf8
    orf10
    orf1a
    RecName:
    S
    M
    ORF3a,
    spike
    nonstructural
    structural
    matrix
    ORF3
    ORF7
    '''

# Determining Protein Similarity (Mutation) by Protein Name

Determining protein similarities for all proteins and all records can take a long time. Once we run:

    protein.GetAllLabeledProteinNames(protein_records)
    



We can then select a similarity analysis by protein name: ORF3a


"The greatest reduction in virus growth was noted following ORF3a deletion."

https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1287583/


ORF3a mutations:

https://github.com/knightsUCF/COVIDGenomeAnalysis/blob/main/results/ORF3a_mutations.txt




    import records
    import protein
    
    
    records = records.Records()
    protein = protein.Protein()


    file_path = 'sequences.fasta'
    
    protein_records = records.GetAllProteinSequences(file_path)
    
    protein_name = 'ORF3a'
    
    protein.DetermineSimilarityByProtein(protein_records, protein_name)



    '''
    output:
    
    ORF3a mutations:
    
    https://github.com/knightsUCF/COVIDGenomeAnalysis/blob/main/results/ORF3a_mutations.txt
    
    (comparing to the first protein instance)
    # todo: specify custom protein sequence,
    # or compare to the most common found one
    
    1.0 = 100% similar
    

    1.0
    0.20363636363636364
    0.20363636363636364
    0.20363636363636364
    0.20363636363636364
    0.20363636363636364
    0.02909090909090909
    0.7890909090909091
    0.20363636363636364
    0.20363636363636364
    0.92
    1.0
    0.20363636363636364
    1.0
    
    ...
    '''






# Comparing Protein Mutations


    import records
    import protein
    
    records = records.Records()
    protein = protein.Protein()
    
    

    # click: download -> download all protein sequences: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049
    # replace file path with file path of download
    
    file_path = 'sequences.fasta'
    protein_records = records.GetAllProteinSequences(file_path)

    # this can take a while
    # note: protein names are organized by how the original uploader of the record filed them
    
    protein.DetermineSimilarity(protein_records)


# TODO:

- get all labeled protein names

- do similarity analysis for specific proteins

- graph mutations
