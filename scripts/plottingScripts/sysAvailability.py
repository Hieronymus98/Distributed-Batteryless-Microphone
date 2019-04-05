import numpy as np
import matplotlib.pyplot as plt
import json

plt.style.use('seaborn-whitegrid')

# Load Data 
path = '../processed_data/availability680.json'
data=[]
with open(path) as f:
    for l in f:
        data.append(json.loads(l))

# Plotting
## Figure, Axes setup
fig = plt.figure(figsize=(8,4))
ax = plt.axes()
ax.grid(linestyle=":")

## Plotting parameters 
plotPatterns = ['-*', '-^', '-+','-o']
fontSize = 16 

dataIndices = np.arange(len(data[0][1]))+1 

## Data plotting
for idx, d in enumerate(data):
    #print(d[0])
    print(d[1]) 
    ax.plot(dataIndices, np.array(d[1])*10,plotPatterns[idx], label=d[0])

## axes formatting 
ylabels = ["{:4d}%".format(x*10) for x in dataIndices-1]
ax.set_yticks(dataIndices-1)
ax.set_yticklabels(ylabels, fontsize=fontSize)
ax.set_xticklabels(dataIndices, fontsize=fontSize)
ax.set_xticks(dataIndices)

## Plotting output
ax.legend(frameon=False, fontsize=fontSize)
plt.tight_layout()
plt.savefig('../../paper/figures/sysAvailability.eps')
plt.show()
