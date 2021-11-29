#!/bin/bash

wget -nc "ftp://ftp.ncbi.nlm.nih.gov/pubchem/Substance/CURRENT-Full/XML/Substance_*"

# then verify md5 sums
# 
#   nohup ./splitem.pl < /dev/null > splitem.pl.out 2> splitem.pl.err &

