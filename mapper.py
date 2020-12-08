#!/usr/bin/env python3
import sys


def mapper():
    output_dict = {}
    start = 0
    end = 100
    for i in range(start, end, 10):
        if i == 0:
            output_dict[(i, i + 10)] = []
        else:
            output_dict[(i+1, i+10)] = []
    for row in sys.stdin:
        try:
            row = row.strip()
            row = row.split(",")
            for (key, value) in output_dict.items():
                if float(key[0]) <= float(row[0]) <= float(key[1]):
                    output_dict[key] = row[3]
                    print((key[0], key[1]), '\t', output_dict[key])
        except: continue


mapper()