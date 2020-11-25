#!/bin/sh
pip freeze > freeze-output.txt
for i in common.txt depends.txt dev.txt prod.txt test-libs.txt; do perl -i.bak -lne 'BEGIN { open FH, "freeze-output.txt"; while(<FH>) { chomp; if(/^([^=]+)/) { $M{$1}=$_; }}} if (/^([^=]+)/) {print $M{$1}}' $i; done
