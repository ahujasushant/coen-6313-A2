#!/usr/bin/env python3
import sys
import ast
import statistics

def reducer():
    output_dict = {}
    for line in sys.stdin:

        line = line.strip()
        try:
           key = line.split('\t')

           if key[0] in output_dict.keys():
              output_dict[key[0]].append(float(key[1]))
           else:
              output_dict[key[0]] = [float(key[1])]
        except: continue

    for key, v in output_dict.items():
        if len(v) == 0: continue
        sorted_list = sorted(v)
        key = key.strip()
        print({'Range '+key: {'Number of Samples': len(sorted_list), 'Maximum': max(sorted_list), 'Minimum': min(sorted_list),
                     'Median': statistics.median(sorted_list), 'Standard Deviation': statistics.stdev(sorted_list)}})


reducer()