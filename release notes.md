
# Version 1.1


(add mutation chart here of significant proteins)

Features:

- process the entire catalog of downloaded COVID protein sequences from: https://www.ncbi.nlm.nih.gov/labs/virus/vssi/#/virus?SeqType_s=Nucleotide&VirusLineage_ss=SARS-CoV-2,%20taxid:2697049

- in records.py we automatically create an organized list which categorizes each protein variation sequence under the labeled name of the protein


- we can get all available labeled protein names from the database: `protein.GetAllLabeledProteinNames(protein_records)`


- we can get protein similiarities (mutations) by name, since this can save us a lot of time instead of processing all protein mutations `protein.GetAllLabeledProteinNames(protein_records)`


<h3> Downloading All Available Protein Sequences (10 million lines) </h3>


Later we will add separate methods for downloading nucleotides versus protein.

```python
from Bio import SeqIO


# download from: https://www.ncbi.nlm.nih.gov/sars-cov-2/


class Records():

    def GetAllProteinSequences(self, file_path):
        print('Categorizing protein sequences...\n')
        proteins = {}
        for record in SeqIO.parse(file_path, "fasta"):
            labels = record.description.split()
            if labels[1][1:] not in proteins:
                proteins[labels[1][1:]] = []
            sequence = record.seq
            proteins[labels[1][1:]].append(str(sequence))
        return proteins
 ```


<h3> Organizing Protein Sequences by Individual Protein </h3>


<h3> Get All Labeled Protein Names from Records </h3>


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

<h3> Determining Protein Similarity (Mutation) by Protein Name </h3>

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






<h3> Comparing Protein Mutations </h3>


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



# Rank Frequency of Protein Formulas by Selected Protein

    ```python
    import records
    import protein


    records = records.Records()
    protein = protein.Protein()


    file_path = 'sequences.fasta'

    protein_records = records.GetAllProteinSequences(file_path)

    protein_name = 'ORF3a'


    frequent_protein_sequences = protein.DetermineFrequentProteinFormulas(protein_records, protein_name)

    # get and rank frequent protein formulas by selected protein out of all available records

    for key, value in frequent_protein_sequences.items():
        print(key, ' - ', value, '\n')
        
    '''
    output
    
    ...
    
    
    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFHSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYHIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL  -  93 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFQSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESVVKDCVVLHSYFTSDYYQLYSTQLSTDTCVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL  -  96 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFQSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVSPVMEPIYDEPTTTTSVPL  -  310 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFQSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDVSSGVVNPVMEPIYDEPTTTTSVPL  -  374 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFHSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSVDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL  -  530 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFHSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL  -  11495 

    MDLFMRIFTIGTVTLKQGEIKDATPSDFVRATATIPIQASLPFGWLIVGVALLAVFQSASKIITLKKRWQLALSKGVHFVCNLLLLFVTVYSHLLLVAAGLEAPFLYLYALVYFLQSINFVRIIMRLWLCWKCRSKNPLLYDANYFLCWHTNCYDYCIPYNSVTSSIVITSGDGTTSPISEHDYQIGGYTEKWESGVKDCVVLHSYFTSDYYQLYSTQLSTDTGVEHVTFFIYNKIVDEPEEHVQIHTIDGSSGVVNPVMEPIYDEPTTTTSVPL  -  19805 
    
    
    
    '''
    
    
    
    
    ```

    




# TODO:

- get all labeled protein names

- do similarity analysis for specific proteins

- graph mutations
