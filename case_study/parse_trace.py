def isCudaMalloc(s):
    return s == '"cudaMalloc"' or s == '"cudaMallocPitch"' or \
           s == '"cudaMallocHost"' or s == '"cudaMallocArray"' or \
           s == '"cudaMalloc3D"' or s == '"cudaMalloc3DArray"' or \
           s == '"cudaMallocManaged"' or s == '"cudaMallocMipmappedArray"'

def isCudaFree(s):
    return s == '"cudaFree"' or s == '"cudaFreeHost"' or \
           s == '"cudaFreeArray"' or s == '"cudaFreeMipmappedArray"'

def isKernel(lineVals):
    return len(lineVals[2]) > 0

def isNullStream(lineVals):
    return lineVals[17] == '"7"'

def isAsync(lineVals):
    return len(lineVals) > 17 and \
           "Async" in lineVals[-2] and \
           not isKernel(lineVals)

def isNullAsync(lineVals):
    return len(lineVals) > 17 and \
           (lineVals[17] == '"7"' or lineVals[17] == "") and \
           "Async" in lineVals[-2] and \
           not isKernel(lineVals)

def parseFile(filepath):
    mallocCountsA = []
    freeCountsA = []
    kernelCountsA = [0]
    nullKernelCountsA = [0]
    nullAsyncCountsA = [0]
    otherNullCountsA = [0]

    mallocCountsB = []
    freeCountsB = []
    kernelCountsB = [0]
    nullKernelCountsB = [0]
    nullAsyncCountsB = [0]
    otherNullCountsB = [0]

    mallocCountsC = []
    freeCountsC = []
    kernelCountsC = [0]
    nullKernelCountsC = [0]
    nullAsyncCountsC = [0]
    otherNullCountsC = [0]

    mallocCountsD = []
    freeCountsD = []
    kernelCountsD = [0]
    nullKernelCountsD = [0]
    nullAsyncCountsD = [0]
    otherNullCountsD = [0]

    mallocCounts = []
    freeCounts = []
    kernelCounts = [0]
    nullKernelCounts = [0]
    nullAsyncCounts = [0]
    otherNullCounts = [0]

    asyncCorrIds = set()
    allCorrIds = {}

    f = open(filepath, 'r')

    # Ignore the first three lines
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    tracing = False
    tracingA = False
    tracingB = False
    tracingC = False
    tracingD = False
    for line in f:
        line = line.strip()
        if line == "": continue

        vals = line.split(',')
        if len(vals) < 19: continue
        
        if vals[-1] != "":
            try:
                corrId = int(vals[-1])
                if corrId not in allCorrIds:
                    allCorrIds[corrId] = vals[-2]
            except ValueError:
                pass

        if "[Marker] TRACE_START" in line:
            if "TRACE_START_A" in line:
                tracingA = True
                mallocCountsA.append(0)
                freeCountsA.append(0)
                kernelCountsA.append(0)
                nullKernelCountsA.append(0)
                nullAsyncCountsA.append(0)
                otherNullCountsA.append(0)
            elif "TRACE_START_B" in line:
                tracingB = True
                mallocCountsB.append(0)
                freeCountsB.append(0)
                kernelCountsB.append(0)
                nullKernelCountsB.append(0)
                nullAsyncCountsB.append(0)
                otherNullCountsB.append(0)
            elif "TRACE_START_C" in line:
                tracingC = True
                mallocCountsC.append(0)
                freeCountsC.append(0)
                kernelCountsC.append(0)
                nullKernelCountsC.append(0)
                nullAsyncCountsC.append(0)
                otherNullCountsC.append(0)
            elif "TRACE_START_D" in line:
                tracingD = True
                mallocCountsD.append(0)
                freeCountsD.append(0)
                kernelCountsD.append(0)
                nullKernelCountsD.append(0)
                nullAsyncCountsD.append(0)
                otherNullCountsD.append(0)
            else:
                tracing = True
                mallocCounts.append(0)
                freeCounts.append(0)
                kernelCounts.append(0)
                nullKernelCounts.append(0)
                nullAsyncCounts.append(0)
                otherNullCounts.append(0)
        elif "[Marker] TRACE_END" in line:
            tracingA = False
            tracingB = False
            tracingC = False
            tracingD = False
            tracing = False

        if isCudaMalloc(vals[-2]):
            if tracingA:
                mallocCountsA[-1] += 1
            if tracingB:
                mallocCountsB[-1] += 1
            if tracingC:
                mallocCountsC[-1] += 1
            if tracingD:
                mallocCountsD[-1] += 1
            if tracing:
                mallocCounts[-1] += 1
        if isCudaFree(vals[-2]):
            if tracingA:
                freeCountsA[-1] += 1
            if tracingB:
                freeCountsB[-1] += 1
            if tracingC:
                freeCountsC[-1] += 1
            if tracingD:
                freeCountsD[-1] += 1
            if tracing:
                freeCounts[-1] += 1

        if isKernel(vals):
            if tracingA:
                kernelCountsA[-1] += 1
            if tracingB:
                kernelCountsB[-1] += 1
            if tracingC:
                kernelCountsC[-1] += 1
            if tracingD:
                kernelCountsD[-1] += 1
            if tracing:
                kernelCounts[-1] += 1
            if isNullStream(vals):
                if tracingA:
                    nullKernelCountsA[-1] += 1
                if tracingB:
                    nullKernelCountsB[-1] += 1
                if tracingC:
                    nullKernelCountsC[-1] += 1
                if tracingD:
                    nullKernelCountsD[-1] += 1
                if tracing:
                    nullKernelCounts[-1] += 1

        if isAsync(vals):
            asyncCorrIds.add(int(vals[-1]))
        if vals[-1] != "" and not isKernel(vals) and int(vals[-1]) in asyncCorrIds:
            if isNullStream(vals):
                if tracingA:
                    nullAsyncCountsA[-1] += 1
                if tracingB:
                    nullAsyncCountsB[-1] += 1
                if tracingC:
                    nullAsyncCountsC[-1] += 1
                if tracingD:
                    nullAsyncCountsD[-1] += 1
                if tracing:
                    nullAsyncCounts[-1] += 1

        if not isAsync(vals) and not isKernel(vals) and isNullStream(vals) and \
           vals[-1] != "" and int(vals[-1]) in allCorrIds:
            if tracingA:
                otherNullCountsA[-1] += 1
            if tracingB:
                otherNullCountsB[-1] += 1
            if tracingC:
                otherNullCountsC[-1] += 1
            if tracingD:
                otherNullCountsD[-1] += 1
            if tracing:
                otherNullCounts[-1] += 1

    f.close()

    if "morphology.csv" in filename:
        print("// Open/close:")
        print("Mallocs:", mallocCountsA)
        print("Frees:", freeCountsA)

        print("\nKernels:", kernelCountsA)
        print("NULL-stream kernels:", nullKernelCountsA)

        print("\nNULL-stream async calls:", nullAsyncCountsA)
        
        print("\nOther NULL-stream calls:", otherNullCountsA)

        print("\n// Erode/dilate:")
        print("Mallocs:", mallocCountsB)
        print("Frees:", freeCountsB)

        print("\nKernels:", kernelCountsB)
        print("NULL-stream kernels:", nullKernelCountsB)

        print("\nNULL-stream async calls:", nullAsyncCountsB)
        
        print("\nOther NULL-stream calls:", otherNullCountsB)
    elif "trace_optical_flow.csv" in filename:
        print("// Brox:")
        print("Mallocs:", mallocCountsA)
        print("Frees:", freeCountsA)

        print("\nKernels:", kernelCountsA)
        print("NULL-stream kernels:", nullKernelCountsA)

        print("\nNULL-stream async calls:", nullAsyncCountsA)
        
        print("\nOther NULL-stream calls:", otherNullCountsA)

        print("\n// DensePyrLK:")
        print("Mallocs:", mallocCountsB)
        print("Frees:", freeCountsB)

        print("\nKernels:", kernelCountsB)
        print("NULL-stream kernels:", nullKernelCountsB)

        print("\nNULL-stream async calls:", nullAsyncCountsB)
        
        print("\nOther NULL-stream calls:", otherNullCountsB)

        print("\n// Farneback:")
        print("Mallocs:", mallocCountsC)
        print("Frees:", freeCountsC)

        print("\nKernels:", kernelCountsC)
        print("NULL-stream kernels:", nullKernelCountsC)

        print("\nNULL-stream async calls:", nullAsyncCountsC)
        
        print("\nOther NULL-stream calls:", otherNullCountsC)

        print("\n// Dual_TVL1:")
        print("Mallocs:", mallocCountsD)
        print("Frees:", freeCountsD)

        print("\nKernels:", kernelCountsD)
        print("NULL-stream kernels:", nullKernelCountsD)

        print("\nNULL-stream async calls:", nullAsyncCountsD)
        
        print("\nOther NULL-stream calls:", otherNullCountsD)
    else:
        print("Mallocs:", mallocCounts)
        print("Frees:", freeCounts)

        print("\nKernels:", kernelCounts)
        print("NULL-stream kernels:", nullKernelCounts)

        print("\nNULL-stream async calls:", nullAsyncCounts)
        
        print("\nOther NULL-stream calls:", otherNullCounts)

if __name__ == "__main__":
    import os
    CUPIDT_DIR = os.environ["CUPIDRT_DIR"]

    for filename in ["trace_bgfg_segm.csv",
                     "trace_farneback_optical_flow.csv",
                     "trace_generalized_hough.csv",
                     "trace_hog.csv",
                     "trace_hog_mod.csv",
                     "trace_houghlines.csv",
                     "trace_morphology.csv",
                     "trace_optical_flow.csv",
                     "trace_optical_flow_mod.csv",
                     "trace_pyrlk_optical_flow.csv",
                     "trace_stereo_match.csv",
                     "trace_super_resolution.csv"]:
        filepath = CUPIDT_DIR + "/trace_logs/" + filename

        print("\n\n==== Parsing file:", filename)

        parseFile(filepath)
