
# Version 1.1


# Downloading All Protein Sequences


# Organizing Protein Sequences by Individual Protein


# Comparing Protein Mutations


    import records
    import protein
    
    records = records.Records()
    protein = protein.Protein()
    
    
    records = Records()
    protein = Protein()

    # click: download -> download all protein sequences: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049
    # replace file path with file path of download
    
    file_path = 'sequences.fasta'
    protein_records = records.GetAllProteinSequences(file_path)

    # this can take a while
    # note: protein names are organized by how the original uploader of the record filed them
    
    protein.DetermineSimilarity(protein_records)
