
# only meant for comparing 1 custom set of data, not meant to be reusable 

'''
Code X: [AAC, AAT, ACC, ATC, ATT, CAG, CTC, CTG, GAA, GAC, GAG, GAT, GCC, GGC, GGT, GTA, GTC, GTT, TAC, TTC]
Sequence,Start,End,Length,Frame,UniqueTri
'''



data = {}


def read_file(file):
    global data

    f = open(file, 'r')
    lines = f.readlines()
    # contents = f.read()

    results = []


    for i in lines:
        results.append(i)



    for i in range(len(results)):
        # print(results[i])
        separated_data_point = results[i].split(',')
        # print(separate_data_point)
        # separated_data_point = list[results[i]].split(',')
        motif_x_length = separated_data_point[3]
        start_location = separated_data_point[1]
        data[start_location] = int(motif_x_length) / 3


    print(data)

    '''
    print(separated_data_point)

    # get motif x which is the nth index element - 3

    motif_x_length = separated_data_point[3]
    start_location = separated_data_point[1]

    print(motif_x_length)
    print(start_location)


    data[start_location] = int(motif_x_length) / 3

    print(data)
    '''


    '''
    for i in contents:
        if i.isalpha():
            self.nucleotides.append(i)

    return self.nucleotides
    '''


read_file('results.txt')



import graph







title = 'Motif X Sequences'

x_label = 'Genome Location'
y_label = 'Length'

x_start = 0
x_end = 30000

y_start = 0
y_end = 10

graph = graph.Graph(title, x_label, y_label, x_start, x_end, y_start, y_end)


# AddData(self, x, y, radius, plot, r, g, b, color)

x_set_1 = []
y_set_1 = []

for i in data:
    x_set_1.append(i)
    y_set_1.append(data[i])
    # print(i)
    # print(data[i])

print(x_set_1)
print(y_set_1)




import genome
import motifx

g = genome.Genome('MN908947_China_01_05_2020.txt')
mx = motifx.MotifX()


data_2 = mx.GetSegments(g.GetCodons())

x_set_2 = []
y_set_2 = []

for i in data_2:
    x_set_2.append(i * 3)
    y_set_2.append(data_2[i])

print(x_set_2)
print(y_set_2)

graph.add_data(x_set_1, y_set_1, 0.000000000000000001, 'green')
graph.add_data(x_set_2, y_set_2, 0.000000000000000001, 'purple')


graph.show()
