import matplotlib.pyplot as plt
import numpy as np
import sys, os, json

plt.style.use('seaborn-whitegrid')
fontSize=16

files = [
"2305-2335lux.json",
"1705-1737lux.json",
"1400-1413lux.json",
"812-836lux.json"
]

color_list = ["#66a61e" , '#e7298a', '#7570b3', '#d95f02', '#1b9e77']
f = plt.figure(figsize=(8,4))

# plt.tick_params(axis='x', pad=15, bottom=False)


for i in range(len(files)):
    file = "../../data/bursty_events/470uf/"+files[i]
    print(file)
    with open(file, "r") as read_file:
        data = json.load(read_file)

    medianprops = {'color':color_list[i], 'linewidth': 2}
    boxprops = {'color': color_list[i], 'linestyle': '-'}
    whiskerprops = {'color': color_list[i], 'linestyle': '-'}
    capprops = {'color': color_list[i], 'linestyle': '-'}
    # flierprops = {'color': color_list[i], 'marker': 'x'}
    
    bw=0.2
    gap=0.2
    plt.boxplot(data[::-1], positions=np.arange(4)+i*0.2, widths=0.2, showfliers=False, \
    medianprops=medianprops, boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops) #, flierprops=flierprops)
plt.xlabel("Light intensity (lux)", fontsize = fontSize)
plt.ylabel("Detection events", fontsize = fontSize)
plt.xticks(np.arange(4)+0.4,(800,1400,1700,2300),fontsize=fontSize-2)
plt.yticks(range(0,10,2),range(0,10,2),fontsize=fontSize-2)
plt.xlim([-0.11,3.71])
plt.ylim([-0.8,8.2])

for group_idx in range(4):

    for bar_idx in range(4):
        plt.text( group_idx+bar_idx*bw-0.05 , -0.3 , bar_idx+1 , color='r' ,fontsize=11, verticalalignment='top')


plt.tight_layout()
f.savefig("../../paper/figures/events_burst_problem.pdf", bbox_inches='tight')
plt.show()