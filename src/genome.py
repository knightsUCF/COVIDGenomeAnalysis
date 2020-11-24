import pprint
import collections





class Genome():

    def __init__(self, file):
        self.file = file
        self.extract_nucleotides()


    def extract_nucleotides(self):
        self.nucleotides = []
        f = open(self.file, 'r')
        contents = f.read()
        for i in contents:
            if i.isalpha():
                self.nucleotides.append(i)
        return self.nucleotides


    def get_nucleotides(self):
        return self.nucleotides


    def get_codons(self):
        codons = []
        for i in range(0, len(self.nucleotides), 3):
            try:
                codon = self.nucleotides[i].upper() + self.nucleotides[i + 1].upper() + self.nucleotides[i + 2].upper()
                print(codon)
                codons.append(codon)
            except:
                pass
        return codons


    def get_nucleotide_with_index(self, index):
        return self.nucleotides[index]


    def get_amino_acid_with_index(self, index):
        amino_acid = self.nucleotides[index] + self.nucleotides[index + 1] + self.nucleotides[index + 2]
        return amino_acid


    def get_character_count(self, character):
        with open(self.file, 'r') as f:
            data_string = f.read().replace('\n', '')
        count = 0
        for i in data_string:
            if i == character:
                count += 1
        return count


    def get_total_character_count(self):
        with open(self.file) as infile:
            lines = 0
            words = 0
            characters = 0
            for line in infile:
                wordslist = line.split()
                lines += 1
                words = words + len(wordslist)
                characters += sum(len(word) for word in wordslist)
            return characters


    def get_percent_frequency_of_nucleotide_bases(self):
        total_nucleotides_count = len(self.nucleotides)
        a_nucleotide_count = self.nucleotides.count('a')
        a_nucleotide_percent_frequency = round(a_nucleotide_count / total_nucleotides_count * 100, 2)
        c_nucleotide_count = self.nucleotides.count('c')
        c_nucleotide_percent_frequency = round(c_nucleotide_count / total_nucleotides_count * 100, 2)
        g_nucleotide_count = self.nucleotides.count('g')
        g_nucleotide_percent_frequency = round(g_nucleotide_count / total_nucleotides_count * 100, 2)
        t_nucleotide_count = self.nucleotides.count('t')
        t_nucleotide_percent_frequency = round(t_nucleotide_count / total_nucleotides_count * 100, 2)
        self.a_frequency = a_nucleotide_percent_frequency
        self.c_frequency = c_nucleotide_percent_frequency
        self.g_frequency = g_nucleotide_percent_frequency
        self.t_frequency = t_nucleotide_percent_frequency


    def get_a_frequency(self):
        self.get_percent_frequency_of_nucleotide_bases()
        return self.a_frequency


    def get_c_frequency(self):
        self.get_percent_frequency_of_nucleotide_bases()
        return self.c_frequency


    def get_g_frequency(self):
        self.get_percent_frequency_of_nucleotide_bases()
        return self.g_frequency


    def get_t_frequency(self):
        self.get_percent_frequency_of_nucleotide_bases()
        return self.t_frequency


    def output_all_nucleotide_frequency_percents(self):
        self.get_percent_frequency_of_nucleotide_bases()
        print('A nucleotide frequency: ', self.a_frequency)
        print('C nucleotide frequency: ', self.c_frequency)
        print('G nucleotide frequency: ', self.g_frequency)
        print('T nucleotide frequency: ', self.t_frequency)


    def translate_to_protein_sequence(self, amino_acids):
        # todo
        pass


    def convert_nucleotides_to_amino_acid(self, nucleotides):
        # https://www.bx.psu.edu/~ross/workmg/GeneticCodeCh13.htm#:~:text=The%20nucleotides%20triplet%20that%20encodes,acid%2C%20in%20most%20cases).
        # of the total of 64 codons, 61 encode amino acids and 3 specify termination of translation

        # 1 ######################################################

        # U - U

        if nucleotides == 'UUU' or nucleotides == 'TTT':
            return 'Phe'
        if nucleotides == 'UUC' or nucleotides == 'TTC':
            return 'Phe'
        if nucleotides == 'UUA' or nucleotides == 'TTA':
            return 'Leu'
        if nucleotides == 'UUG' or nucleotides == 'TTG':
            return 'Leu'

        # U - C

        if nucleotides == 'CUU' or nucleotides == 'CTT':
            return 'Leu'
        if nucleotides == 'CUC' or nucleotides == 'CTC':
            return 'Leu'
        if nucleotides == 'CUA' or nucleotides == 'CTA':
            return 'Leu'
        if nucleotides == 'CUG' or nucleotides == 'CTG':
            return 'Leu'

        # U - A

        if nucleotides == 'AUU' or nucleotides == 'ATT':
            return 'Ile'
        if nucleotides == 'AUC' or nucleotides == 'ATC':
            return 'Ile'
        if nucleotides == 'AUA' or nucleotides == 'ATA':
            return 'Ile'
        if nucleotides == 'AUG' or nucleotides == 'ATG':
            return 'Met'

        # U - G

        if nucleotides == 'GUU' or nucleotides == 'GTT':
            return 'Val'
        if nucleotides == 'GUC' or nucleotides == 'GTC':
            return 'Val'
        if nucleotides == 'GUA' or nucleotides == 'GTA':
            return 'Val'
        if nucleotides == 'GUG' or nucleotides == 'GTG':
            return 'Val'

        # 2 ######################################################

        # C - U

        if nucleotides == 'UCU' or nucleotides == 'TCT':
            return 'Ser'
        if nucleotides == 'UCC' or nucleotides == 'TCC':
            return 'Ser'
        if nucleotides == 'UCA' or nucleotides == 'TCA':
            return 'Ser'
        if nucleotides == 'UCG' or nucleotides == 'TCG':
            return 'Ser'

        # C - C

        if nucleotides == 'CCU' or nucleotides == 'CCT':
            return 'Pro'
        if nucleotides == 'CCC':
            return 'Pro'
        if nucleotides == 'CCA':
            return 'Pro'
        if nucleotides == 'CCG':
            return 'Pro'

        # C - A

        if nucleotides == 'ACU' or nucleotides == 'ACT':
            return 'Thr'
        if nucleotides == 'ACC':
            return 'Thr'
        if nucleotides == 'ACA':
            return 'Thr'
        if nucleotides == 'ACG':
            return 'Thr'

        # C - G

        if nucleotides == 'GCU' or nucleotides == 'GCT':
            return 'Thr'
        if nucleotides == 'GCC':
            return 'Thr'
        if nucleotides == 'GCA':
            return 'Thr'
        if nucleotides == 'GCG':
            return 'Thr'

        # 3 ######################################################

        # A - U

        if nucleotides == 'UAU' or nucleotides == 'TAT':
            return 'Tyr'
        if nucleotides == 'UAC' or nucleotides == 'TAC':
            return 'Tyr'
        if nucleotides == 'UAA' or nucleotides == 'TAA':
            return 'Term'
        if nucleotides == 'UAG':
            return 'Term'

        # A - C

        if nucleotides == 'CAU' or nucleotides == 'CAT':
            return 'His'
        if nucleotides == 'CAC':
            return 'His'
        if nucleotides == 'CAA':
            return 'Gln'
        if nucleotides == 'CAG':
            return 'Gln'

        # A - A

        if nucleotides == 'AAU' or nucleotides == 'AAT':
            return 'Asn'
        if nucleotides == 'AAC':
            return 'Asn'
        if nucleotides == 'AAA':
            return 'Lys'
        if nucleotides == 'AAG':
            return 'Lys'

        # A - G

        if nucleotides == 'GAU' or nucleotides == 'GAT':
            return 'Asp'
        if nucleotides == 'GAC':
            return 'Asp'
        if nucleotides == 'GAA':
            return 'Glu'
        if nucleotides == 'GAG':
            return 'Glu'

        # 4 ######################################################

        # G - U

        if nucleotides == 'UGU' or nucleotides == 'TGT':
            return 'Cys'
        if nucleotides == 'UGC' or nucleotides == 'TGC':
            return 'Cys'
        if nucleotides == 'UGA':
            return 'Term'
        if nucleotides == 'UGG':
            return 'Trp'

        # G - C

        if nucleotides == 'CGU' or nucleotides == 'CGT':
            return 'Arg'
        if nucleotides == 'CGC':
            return 'Arg'
        if nucleotides == 'CGA':
            return 'Arg'
        if nucleotides == 'CGG':
            return 'Arg'

        # G - A

        if nucleotides == 'AGU' or nucleotides == 'AGT':
            return 'Ser'
        if nucleotides == 'AGC':
            return 'Ser'
        if nucleotides == 'AGA':
            return 'Arg'
        if nucleotides == 'AGG':
            return 'Arg'

        # G - A

        if nucleotides == 'AGU' or nucleotides == 'AGT':
            return 'Ser'
        if nucleotides == 'AGC':
            return 'Ser'
        if nucleotides == 'AGA':
            return 'Arg'
        if nucleotides == 'AGG':
            return 'Arg'

        # G - G

        if nucleotides == 'GGU' or nucleotides == 'GGT':
            return 'Gly'
        if nucleotides == 'GGC':
            return 'Gly'
        if nucleotides == 'GGA':
            return 'Gly'
        if nucleotides == 'GGG':
            return 'Gly'

        else:
            return -1


    def is_valid_start_codon(self, amino_acid):
        # todo: insert more valid start codons, but for now the 'AUG' start codon is 80% occurring and what the current research focuses on
        amino_acid_upper_case = amino_acid.upper()
        if amino_acid_upper_case == 'AUG' or amino_acid_upper_case == 'ATG':
            return True
        else:
            return False


    def is_valid_stop_codon(self, amino_acid):
        amino_acid_upper_case = amino_acid.upper()

        # an amino acid of "Term" is designated for stop codons

        if amino_acid_upper_case == 'TERM':
            return True
        if amino_acid_upper_case == 'UAA' or amino_acid_upper_case == 'UAG' or amino_acid_upper_case == 'UGA':
            return True
        if amino_acid_upper_case == 'TAA' or amino_acid_upper_case == 'TAG' or amino_acid_upper_case == 'TGA':
            return True
        else:
            return False


    def get_start_codon_indexes(self):
        start_codons_count = 0
        start_codon_index = -1
        start_codon_indexes = []
        for i in range(len(self.nucleotides)):
            # prevent negative index errors
            if i < 2:
                continue
            if self.nucleotides[i] == 'g' and self.nucleotides[i - 1] == 'u' and self.nucleotides[i - 2] == 'a':
                start_codon_index = i - 2
                start_codon_indexes.append(start_codon_index)
                start_codons_count += 1
            if self.nucleotides[i] == 'g' and self.nucleotides[i - 1] == 't' and self.nucleotides[i - 2] == 'a':
                start_codon_index = i - 2
                start_codon_indexes.append(start_codon_index)
                start_codons_count += 1
        return start_codon_indexes


    def get_stop_codon_indexes(self):
        stop_codons_count = 0
        stop_codon_index = -1
        stop_codon_indexes = []
        for i in range(len(self.nucleotides)):
            # prevent negative index errors
            if i < 2:
                continue
            # Major stop codons: UAA, UAG, UGA
            # we will have 6 sets here, since we also need to test for T which is equivalent with U
            # they need to be input backwards here, since we are iterating backwards

            # UAA - AAU

            if self.nucleotides[i] == 'a' and self.nucleotides[i - 1] == 'a' and self.nucleotides[i - 2] == 'u':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

            # UAG - GAU

            if self.nucleotides[i] == 'g' and self.nucleotides[i - 1] == 'a' and self.nucleotides[i - 2] == 'u':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

            # UGA - AGU

            if self.nucleotides[i] == 'a' and self.nucleotides[i - 1] == 'g' and self.nucleotides[i - 2] == 'u':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

            # substituting t for u

            # TAA - AAT

            if self.nucleotides[i] == 'a' and self.nucleotides[i - 1] == 'a' and self.nucleotides[i - 2] == 't':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

            # TAG - GAT

            if self.nucleotides[i] == 'g' and self.nucleotides[i - 1] == 'a' and self.nucleotides[i - 2] == 't':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

            # TGA - AGT

            if self.nucleotides[i] == 'a' and self.nucleotides[i - 1] == 'g' and self.nucleotides[i - 2] == 't':
                stop_codon_index = i - 2
                stop_codon_indexes.append(stop_codon_index)
                stop_codons_count += 1

        return stop_codon_indexes


    def extract_spike_protein(self):
        pass


    def generate_rscu(self):
        # "AKA GenerateCodonUsageIndex()"

        self.codon_count = {}
        self.index = {}

        codons_count = {}
        codons_list = []

        # based on: https://github.com/biopython/biopython/blob/master/Bio/SeqUtils/CodonUsage.py

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

        # populate the codons_count dictionary with the frequency of specific codons occurring

        for i in range(0, len(self.nucleotides), 3):
            try:
                codon = self.nucleotides[i].upper() + self.nucleotides[i + 1].upper() + self.nucleotides[i + 2].upper()
                codons_list.append(codon)
                if codon not in codons_count:
                    codons_count[codon] = 1
                if codon in codons_list:
                    codons_count[codon] += 1
            except:
                pass

        # print(codons_list)
        # print(codons_count)

        # now to calculate the index we first need to sum the number of times
        # synonymous codons were used all together.

        for i in synonymous_codons:
            total = 0.0
            # RCSU values are CodonCount/((1/num of synonymous codons) * sum of all synonymous codons)
            rcsu = []
            codons = synonymous_codons[i]
            for codon in codons:
                total += codons_count[codon]
            # calculate the RSCU value for each of the codons
            for codon in codons:
                denominator = float(total) / len(codons)
                rcsu.append(codons_count[codon] / denominator)
            # now generate the index W=RCSUi/RCSUmax:
            rcsu_max = max(rcsu)
            for codon_index, codon in enumerate(codons):
                self.index[codon] = rcsu[codon_index] / rcsu_max
        ranked_by_index = collections.OrderedDict(sorted(self.index.items(), key=lambda kv: kv[1]))
        output = pprint.PrettyPrinter(indent = 4)
        output.pprint(ranked_by_index)
        return ranked_by_index



