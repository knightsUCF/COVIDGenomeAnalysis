# COVID GENOME ANALYSIS


![COVID GIF](GIFS/COVID.gif)


# Introduction

The COVID Genome Analysis project aims at analyzing the genomic sequence of COVID-19.

Author: Piotr (Peter) Kwiatkowski.

Contact: peterk@knights.ucf.edu


# Data

COVID genomic sequence data can be obtained from here: https://www.ncbi.nlm.nih.gov/sars-cov-2/

Here are some of the samples:

First record: https://www.ncbi.nlm.nih.gov/nuccore/MN908947
01 05 2020 Shanghai Public Health Clinical Center & School of Public Health


https://www.ncbi.nlm.nih.gov/nuccore/MW241329
11 10 2020 - Utah Public Health Laboratory


https://www.ncbi.nlm.nih.gov/nuccore/MW228187
11 06 2020 - Laboratory Services Section, Texas


https://www.ncbi.nlm.nih.gov/nuccore/MW240764
11 10 2020 Maryland Department of Health


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

We can test with the code by:







