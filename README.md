Project Information
===============

This repository was used for the paper ["CUPiD^RT: Detecting Improper GPU Usage in Real-Time Applications"](https://www.cs.unc.edu/~tamert/papers/isorc21.pdf), presented at ISORC 2021.

Setup
===============

First, you need two enviornment variables:

* CUPIDRT_DIR should point to this repository.
* OPENCV_DIR should point to your OpenCV repository (we used version 3.4).

Running our Case Study
===============

To run CUPiD^RT to gather tracing results:

0. Run `cd CUPiD-RT`.
1. Run each of run*.sh.
2. Run `cd ../case_study`.
3. Run `python3 parse_trace.py > tracing_output.txt`.
4. Look at the middle of each list printed in tracing_output.txt
   to determine table values.

To generate the per-frame response time plot:

0. Run `cd case_study`.
1. Run `./run_hog_rt.sh 1` for values 1 to 10.
2. Run `./make_plot.sh > hog_rt/table_vals.txt` to generate the
   PDF file (this uses graph_cdf.py).
3. Find the plot at hog_rt/hog_rt.pdf.
4. Find the table values in hog_rt/table_vals.txt.

To generate the kernel launch time plots:

0. Run `cd case_study`.
1. Run `./run_hog_kernels.sh 1` for values 1 to 10.
2. Run `./make_hist.sh > hog_kernels/table_vals.txt` to generate the
   PDf files (this uses graph_hist.py).
3. Find the plots at hog_kernels/*.pdf.
4. Find the table values in hog_kernels/table_vals.txt.