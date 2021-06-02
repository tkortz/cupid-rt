#!/usr/bin/python

import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

plt.rcParams.update({"font.size": 16})

#plt.figure(figsize=(8,3.5))
styles = ['-', '--','-.',':']

def parseData():
    origData = {}
    modData = {}
    for i in range(1,len(sys.argv)-2, 2):
        indx = i + 1
        fname = sys.argv[indx]
        label = sys.argv[indx+1]
        data = origData if "orig" in fname else modData
        print("\nfname and label:", fname, label)
        
        # Grab the data
        f = open(fname, 'r')
        num_at_500 = 0
        for line in f:
            if " us" not in line: continue
            if line.startswith("RT ["):
                frameIdx = int(line[4:line.find("]")])
                if frameIdx == 500:
                    num_at_500 += 1
            if num_at_500 >= 4: break
            s = line.strip().split(' ')
            kernel_name = s[0][:-1] # skip the :
            if kernel_name not in data:
                data[kernel_name] = []
            data[kernel_name].append(float(s[1]))
        f.close()
    return origData, modData

def plotData(data):
    kernel_abbrevs = {"resize":          "Kernel A",
                      "compute_grads":   "Kernel B",
                      "compute_hists":   "Kernel C",
                      "normalize_hists": "Kernel D",
                      "classify_hists":  "Kernel E"}
    kernel_names = sorted(data.keys(), key=lambda x: kernel_abbrevs[x])

    for kernel_name in kernel_names:
        content = data[kernel_name]
        print("\n" + kernel_name)
        print("avg: " + str(sum(content)/len(content)))
        sorted_content = sorted(content)
        print("50th:", sorted_content[int(len(content) * 0.50)])
        print("90th:", sorted_content[int(len(content) * 0.90)])
        print("95th:", sorted_content[int(len(content) * 0.95)])
        print("99th:", sorted_content[int(len(content) * 0.99)])
        print("max: " + str(max(content)))
        print("variance: " + str(np.var(content)))
        if len(np.atleast_1d(content)) < 2:
            continue
        r = max(content) - min(content)
        nbins = int(r)#5000
        #plt.hist(content, nbins, histtype="step", stacked=True, fill=False, normed=True, label=kernel_abbrevs[kernel_name])
        plt.hist(content, nbins, histtype="step", fill=False, normed=True, label=kernel_abbrevs[kernel_name])

def plotSubfigData(data, title):
    # Plot the data
    plotData(data)

    # Customize the subplot
    plt.title(title)
    plt.xlabel("Kernel launch time (microseconds)")
    if "Original" in title:
        plt.ylabel("Density")
    plt.xlim([0,150])
    plt.ylim([0,0.3])
    if "Original" not in title:
        plt.legend(loc="best")

def plotOneFigData(data):
    plt.figure(figsize=(10,5))
    ax = plt.gca()

    # Plot the data
    plotData(data)

    # Customize the plot
    plt.xlabel("Kernel launch time (microseconds)")
    plt.ylabel("Density")
    plt.xlim([0,350])
    plt.ylim([0,0.025])
    plt.legend(loc="best")

# Parse the data
origData, modData = parseData()

# Make some output
if (len(sys.argv) % 2 == 0):
    output_dir = 0
else:
    output_dir = sys.argv[len(sys.argv)-1]
    print("\nOutput:", output_dir)

# Plot it!
if len(origData) > 0 and len(modData) > 0:
    plt.figure(figsize=(10,5))
    ax = plt.gca()

    plt.subplot(121)
    plotSubfigData(origData, "Original HOG")

    plt.subplot(122)
    plotSubfigData(modData, "HOG with issues fixed")

    if output_dir != 0:
        plt.savefig(output_dir + "/hog_kernel_full.pdf", bbox_inches="tight", pad_inches=0)

if len(origData) > 0:
    plotOneFigData(origData)
    if output_dir != 0:
        plt.savefig(output_dir + "/hog_kernel_zoomed_orig.pdf", bbox_inches="tight", pad_inches=0)
if len(modData) > 0:
    plotOneFigData(modData)
    if output_dir != 0:
        plt.savefig(output_dir + "/hog_kernel_zoomed_mod.pdf", bbox_inches="tight", pad_inches=0)


#plt.annotate('cudaThreadSynchronize', xy=(64000, 0.8), xytext=(45000, 0.6), arrowprops=dict(facecolor='red', width=2,
    #headwidth=2))

plt.show()
