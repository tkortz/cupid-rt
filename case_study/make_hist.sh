#!/bin/bash

indir="hog_kernels"
outdir="hog_kernels"

python3 graph_hist.py "Kernel Launch Durations of HOG" \
    $indir/hog_kernels_1/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_2/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_3/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_4/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_5/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_6/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_7/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_8/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_9/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_10/hog_rt_orig_inst4.txt "" \
    $indir/hog_kernels_1/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_2/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_3/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_4/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_5/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_6/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_7/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_8/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_9/hog_rt_mod_noNULL_inst4.txt "" \
    $indir/hog_kernels_10/hog_rt_mod_noNULL_inst4.txt "" \
    $outdir
