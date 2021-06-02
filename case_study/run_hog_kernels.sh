#!/bin/bash

outdir="hog_kernels/hog_kernels_$1"
mkdir -p $outdir

video="${OPENCV_DIR}/samples/data/vtest.avi"

exec="${OPENCV_DIR}/build/bin/example_gpu_hog"
$exec --video $video --use_threads true --num_inst 4 > $outdir/hog_rt_orig_inst4.txt

exec="${OPENCV_DIR}/build/bin/example_gpu_hog_mod"
$exec --video $video --use_threads true --num_inst 4 > $outdir/hog_rt_mod_noNULL_inst4.txt
