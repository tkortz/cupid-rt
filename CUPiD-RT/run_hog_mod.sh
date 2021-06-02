#!/bin/bash

prog="hog_mod"

mkdir -p ${CUPIDRT_DIR}/CUPiD-RT/trace_logs

dir=`pwd`

cd ${OPENCV_DIR}/build/bin/run_here

nvprof --csv -u us --print-api-trace --print-gpu-trace \
       --log-file ${CUPIDRT_DIR}/CUPiD-RT/trace_logs/trace_$prog.csv \
       ${OPENCV_DIR}/build/bin/example_gpu_$prog \
       --video ${OPENCV_DIR}/samples/data/vtest.avi

cd $dir
