#!/usr/bin/env python

#************
# LIBRARIES *
#************

import sys
from optparse import OptionParser


#*****************
# OPTION PARSING *
#*****************

parser = OptionParser()
parser.add_option("-i", "--input", dest="input", help="Input file path (gene.starts.tsv)")
parser.add_option("-s", "--start", dest="start", type="int", help="5' coordinate of a regulatory element")
(options, args) = parser.parse_args()

# Check if both input file and start position are provided
if not options.input or not options.start:
    parser.error("Both --input and --start options are required.")

open_input = open(options.input)
enhancer_start = options.start


#********
# BEGIN *
#********

min_distance = float('inf')  # Set initial minimum distance to infinity
closest_gene = None  # Initialize the closest gene as None

for line in open_input:  # for each line in the input file
    gene, start_str = line.strip().split('\t')  # split the line into two columns based on a tab
    start = int(start_str)
    distance = abs(start - enhancer_start)  # compute the absolute value of the difference between start and enhancer_start

    if distance < min_distance:  # if this distance is less than the current minimum distance
        min_distance = distance  # update the minimum distance
        closest_gene = (gene, start)  # update the closest gene and its start position

# Output the closest gene, its start position, and the distance from the enhancer start position
if closest_gene:
    gene, start = closest_gene
    print("{gene}\t{start}\t{min_distance}".format(gene=gene, start=start, min_distance=min_distance))
else:
    print("No genes found in the input file.")

