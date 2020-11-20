import genome

# get genome sequences
g1 = genome.Genome('MN908947_China_01_05_2020.txt')
g2 = genome.Genome('MT483564_California_11_10_2020.txt')

print('China 01 05 2020 C frequency: ', g1.GetCFrequency())
print('China 01 05 2020 G frequency: ', g1.GetGFrequency())

print('California 11 10 2020 C frequency: ', g2.GetCFrequency())
print('California 11 05 2020 G frequency: ', g2.GetGFrequency())
