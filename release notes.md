
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


    file_path = 'sequences.fasta'
    protein_records = records.GetAllProteinSequences(file_path)

    # this can take a while
    protein.DetermineSimilarity(protein_records)
