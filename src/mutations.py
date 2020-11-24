import genome

# get genome sequences
g1 = genome.Genome('MN908947_China_01_05_2020.txt')
g2 = genome.Genome('MT483564_California_11_10_2020.txt')

print('China 01 05 2020 C frequency: ', g1.get_c_frequency())
print('China 01 05 2020 G frequency: ', g1.get_g_frequency())

print('California 11 10 2020 C frequency: ', g2.get_c_frequency())
print('California 11 05 2020 G frequency: ', g2.get_g_frequency())
