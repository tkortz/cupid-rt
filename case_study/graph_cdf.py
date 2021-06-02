#!/usr/bin/python

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

plt.rcParams.update({"font.size": 16})

#plt.figure(figsize=(8,3.5))
plt.figure(figsize=(10,5))
ax = plt.gca()
title = sys.argv[1]
styles = ['-', '--',':', '-.']
colors = ['r', 'g', 'b', 'm', 'k', 'c', 'r', 'g']

data = {}
labels = []
for i in xrange(1,len(sys.argv)-2, 2):
    indx = i + 1
    fname = sys.argv[indx]
    label = sys.argv[indx+1]
    print "\nfname and label:", fname, label
    
    # Grab the data
    content = []
    f = open(fname, 'r')
    for line in f:
        if "FPS" not in line and "RT" not in line: continue
        frameIdx = int(line[4:line.find("]")])
        if frameIdx >= 500: continue
        s = line.strip().split(' ')
        content.append(float(s[2])) # ms
    f.close()

    # Group data by curve
    if label not in data:
        labels.append(label)
        data[label] = content
    else:
        data[label].extend(content)

for (i, label) in enumerate(labels):
    content = data[label]

    print "\n" + label + ":"
    print "avg: " + str(sum(content)/len(content))
    print "worst: " + str(max(content))
    print "variance: " + str(np.var(content))
    print "90th: " + str(sorted(content)[int(len(content) * 0.9)])
    print "99th: " + str(sorted(content)[int(len(content) * 0.99)])
    #print content[0:10]
    if len(np.atleast_1d(content)) < 2:
        continue
    dist = np.array(range(len(content)+1))[1:]/float(len(content))
    #print np.sort(content)
    #print labels[i]
    s = colors[i % len(colors)] + styles[i % len(styles)]# + markers[i % len(markers)]
    plt.plot(np.sort(content), dist, s, label=label.lower(),
            linewidth=2)
    #plt.plot(np.sort(content), range(len(content)+1)[1:], styles[i/2 % len(styles)], label=label)

if (len(sys.argv) % 2 == 0):
    output = 0
else:
    output = sys.argv[len(sys.argv)-1]

#plt.annotate('cudaThreadSynchronize', xy=(64000, 0.8), xytext=(45000, 0.6), arrowprops=dict(facecolor='red', width=2,
    #headwidth=2))

print "\nOutput:", output

#plt.title("CDF of Graph Time")
#plt.title(title)
plt.ylabel("Percentage (X <= x)");
#plt.xlabel("Start Time (s)")
plt.xlabel("Per-Frame Response Time (milliseconds)")
#plt.legend(loc="best")
plt.legend(loc="lower right")
#plt.xlim([0,max(500, plt.xlim()[1])])
plt.xlim([0, 60])
#plt.show()
if (output != 0):
    plt.savefig(output, bbox_inches = "tight", pad_inches = 0)
else:
    plt.show()
