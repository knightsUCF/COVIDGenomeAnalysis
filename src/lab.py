import genome
import motifx

g = genome.Genome('MN908947_China_01_05_2020.txt')
mx = motifx.MotifX()


print(mx.get_segments_by_rank(g.get_codons()))

