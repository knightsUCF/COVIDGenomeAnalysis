# COVID Genome Analysis


![COVID GIF](GIFS/COVID.gif)

Pictured: spike proteins which are responsible for cell entry and infection.

https://jvi.asm.org/content/77/16/8801

Spike proteins are a target for vaccine and therapeutic development.

https://www.nature.com/articles/nrmicro2090


# Introduction

The COVID Genome Analysis project aims at analyzing the genomic sequence of COVID-19.


Author: Piotr (Peter) Kwiatkowski.

Contact: peterk@knights.ucf.edu


# Features

- identifying the start and stop codons for analyzing where the COVID spike protein might begin and end

- analyzing the frequency of C and G nucleotides across samples which have been shown to be linked to the rate of mutation

- analyzing "Motif X" sequences, which have been show to display mathematical properties and are significant in identifying major protein sequences

- calculating the RSCU index (weighs synonymous codons)

"Different codons that encode the same amino acid are known as synonymous codons. Even though synonymous codons encode the same amino acid, it has been shown for all organisms that the distribution of these codons in a genome is not random"

https://www.nature.com/articles/nrmicro2090


# Data

COVID genomic sequence data can be obtained from: https://www.ncbi.nlm.nih.gov/sars-cov-2/


https://www.ncbi.nlm.nih.gov/nuccore/MN908947
01 05 2020 - Shanghai Public Health Clinical Center & School of Public Health

https://www.ncbi.nlm.nih.gov/nuccore/MW228187
11 06 2020 - Laboratory Services Section, Texas

https://www.ncbi.nlm.nih.gov/nuccore/MW241329
11 10 2020 - Utah Public Health Laboratory

https://www.ncbi.nlm.nih.gov/nuccore/MW240764
11 10 2020 - Maryland Department of Health


https://www.ncbi.nlm.nih.gov/nuccore/MT483564
11 10 2020 - Division of Infectious Diseases, California


# Genome Class

The main class Genome.py can be found here: https://github.com/knightsUCF/COVIDGenomeAnalysis/blob/main/genome.py

This class provides the methods for:

- parsing genomic sequence data, extracting nulceotides, and converting to codons

- identifies start and stop codons by index in the genomic sequence

- between the start and stop codons, protein sequences can be identified which are the target for vaccines



# COVID Mutations

The rate of COVID mutation has been linked to the frequency of C and G nucleotides.

"We found that CG reduction in SARS-CoV-2 is achieved mainly through mutating C/G into A/T, and CG is the best target for mutation"

https://www.nature.com/articles/s41598-020-69342-y

We can test this by:


    import genome

    # get genome sequences
    g1 = genome.Genome('MN908947_China_01_05_2020.txt')
    g2 = genome.Genome('MT483564_California_11_10_2020.txt')

    print('China 01 05 2020 C nucleotide frequency: ', g1.GetCFrequency())
    print('China 01 05 2020 G nucleotide frequency: ', g1.GetGFrequency())

    print('California 11 10 2020 C nucleotide frequency: ', g2.GetCFrequency())
    print('California 11 05 2020 G nucleotide frequency: ', g2.GetGFrequency())
    
    
    # output:
    China 01 05 2020 C nucleotide frequency:  18.37
    China 01 05 2020 G nucleotide frequency:  19.61
    California 11 10 2020 C nucleotide frequency:  18.16
    California 11 05 2020 G nucleotide frequency:  19.39
    
    

The results confirm the study, where the C and G nucleotides have decreased in frequency from the January sample to the November sample, indicating the virus has mutated since.

Further possible research areas could include analyzing data sets by geolocation and time, and analyzing the rate of mutation.


# RSCU Index

A codon in the form of a trinucleotide base such as "ATG" can code for the amino acid, "methionine". MEthionine is an an important amino acid being the most common start codon. In this case only one amino acid "ATG", codes for methionine, so methionine does not have any synonymous codons. However other amino acids do have multiple codons which can code for the same amino acid being termed as "synonymous".  The RSCU index weighs the appearance of various synynomous codons in the genomic sequence to analyze their importance. 

Here is a table of amino acids, and their synonymous codons:

    synonymous_codons = {
                "CYS": ["TGT", "TGC"],
                "ASP": ["GAT", "GAC"],
                "SER": ["TCT", "TCG", "TCA", "TCC", "AGC", "AGT"],
                "GLN": ["CAA", "CAG"],
                "MET": ["ATG"],
                "ASN": ["AAC", "AAT"],
                "PRO": ["CCT", "CCG", "CCA", "CCC"],
                "LYS": ["AAG", "AAA"],
                "TERM": ["TAG", "TGA", "TAA"],
                "THR": ["ACC", "ACA", "ACG", "ACT"],
                "PHE": ["TTT", "TTC"],
                "ALA": ["GCA", "GCC", "GCG", "GCT"],
                "GLY": ["GGT", "GGG", "GGA", "GGC"],
                "ILE": ["ATC", "ATA", "ATT"],
                "LEU": ["TTA", "TTG", "CTC", "CTT", "CTG", "CTA"],
                "HIS": ["CAT", "CAC"],
                "ARG": ["CGA", "CGC", "CGG", "CGT", "AGG", "AGA"],
                "TRP": ["TGG"],
                "VAL": ["GTA", "GTC", "GTG", "GTT"],
                "GLU": ["GAG", "GAA"],
                "TYR": ["TAT", "TAC"],
            }



https://en.wikipedia.org/wiki/Start_codon

"Different codons that encode the same amino acid are known as synonymous codons. Even though synonymous codons encode the same amino acid, it has been shown for all organisms that the distribution of these codons in a genome is not random"

https://www.nature.com/articles/nrmicro2090

