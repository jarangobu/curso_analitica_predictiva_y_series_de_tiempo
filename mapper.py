#! /usr/bin/env python

import sys, re
import pandas as pd

if __name__ == "__main__": 
    
    for line in sys.stdin:
        line = re.findall(r'\s*"((?:[^"]*(?:"")?)+)",?|\s*([^,]*),?',line)
        line = ["".join(i) for i in line[:-1]]
        line = ";".join([line[17], line[18]])
        sys.stdout.write("{}\t1\n".format(line))
        
        