
# Version 1.1

Version 1.1 adds the ability to process the entire catalog of downloaded COVID sequences from: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049

In records.py we automatically create a list which categorizes each protein variation sequence under the labeled name of the protein.

https://github.com/knightsUCF/COVIDGenomeAnalysis/blob/main/src/records.py


# Downloading All Protein Sequences


# Organizing Protein Sequences by Individual Protein


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
