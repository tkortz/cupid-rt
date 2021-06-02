#!/bin/bash

outdir="hog_rt/hog_rt_$1"
mkdir -p $outdir

video="${OPENCV_DIR}/samples/data/vtest.avi"

exec="${OPENCV_DIR}/build/bin/example_gpu_hog"
$exec --video $video > $outdir/hog_rt_orig_inst0.txt
$exec --video $video --use_threads true --num_inst 1 > $outdir/hog_rt_orig_inst1.txt
$exec --video $video --use_threads true --num_inst 2 > $outdir/hog_rt_orig_inst2.txt
$exec --video $video --use_threads true --num_inst 3 > $outdir/hog_rt_orig_inst3.txt
$exec --video $video --use_threads true --num_inst 4 > $outdir/hog_rt_orig_inst4.txt

exec="${OPENCV_DIR}/build/bin/example_gpu_hog_mod"
$exec --video $video > $outdir/hog_rt_mod_noNULL_inst0.txt
$exec --video $video --use_threads true --num_inst 1 > $outdir/hog_rt_mod_noNULL_inst1.txt
$exec --video $video --use_threads true --num_inst 2 > $outdir/hog_rt_mod_noNULL_inst2.txt
$exec --video $video --use_threads true --num_inst 3 > $outdir/hog_rt_mod_noNULL_inst3.txt
$exec --video $video --use_threads true --num_inst 4 > $outdir/hog_rt_mod_noNULL_inst4.txt
