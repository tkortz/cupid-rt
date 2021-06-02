#!/bin/bash

indir="hog_rt"
outdir="hog_rt"

for output in "hog_rt.pdf"
do
    python graph_cdf.py "Per-Frame Response Time of HOG" \
           $indir/hog_rt_1/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_1/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_1/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_1/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_1/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_1/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_1/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_1/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_2/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_2/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_2/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_2/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_2/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_2/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_2/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_2/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_3/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_3/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_3/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_3/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_3/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_3/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_3/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_3/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_4/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_4/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_4/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_4/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_4/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_4/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_4/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_4/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_5/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_5/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_5/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_5/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_5/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_5/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_5/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_5/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_6/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_6/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_6/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_6/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_6/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_6/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_6/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_6/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_7/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_7/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_7/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_7/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_7/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_7/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_7/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_7/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_8/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_8/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_8/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_8/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_8/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_8/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_8/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_8/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_9/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_9/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_9/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_9/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_9/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_9/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_9/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_9/hog_rt_orig_inst4.txt "Original x4" \
           $indir/hog_rt_10/hog_rt_mod_noNULL_inst1.txt "Modified x1" \
           $indir/hog_rt_10/hog_rt_mod_noNULL_inst2.txt "Modified x2" \
           $indir/hog_rt_10/hog_rt_mod_noNULL_inst3.txt "Modified x3" \
           $indir/hog_rt_10/hog_rt_mod_noNULL_inst4.txt "Modified x4" \
           $indir/hog_rt_10/hog_rt_orig_inst1.txt "Original x1" \
           $indir/hog_rt_10/hog_rt_orig_inst2.txt "Original x2" \
           $indir/hog_rt_10/hog_rt_orig_inst3.txt "Original x3" \
           $indir/hog_rt_10/hog_rt_orig_inst4.txt "Original x4" \
           $outdir/$output
done