import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import networkx.drawing.nx_pylab

G = nx.Graph()

df = pd.read_csv('small-gephiready.tsv', sep='\t')

for index, row in df.iterrows():
    G.add_edge(row['Source'], row['Target'], relation=row['Type'])

print(G)

G = nx.petersen_graph()
subax1 = plt.subplot(121)
nx.draw(G, with_labels=True, font_weight='bold')
subax2 = plt.subplot(122)
nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')

plt.show()