
# Version 1.1

Version 1.1 adds the ability to process the entire catalog of downloaded COVID sequences from: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049

In records.py we automatically create a list which categorizes each protein variation sequence under the labeled name of the protein.

https://github.com/knightsUCF/COVIDGenomeAnalysis/blob/main/src/records.py


# Downloading All Protein Sequences


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
