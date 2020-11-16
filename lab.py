import genome
import motifx

g = genome.Genome('MN908947_China_01_05_2020.txt')
mx = motifx.MotifX()


print(mx.GetSegmentsByRank(g.GetCodons()))

