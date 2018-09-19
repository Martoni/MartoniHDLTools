#! /usr/bin/python3
# -*- coding: utf-8 -*-
#-----------------------------------------------------------------------------
# Author:   Fabien Marteau <fabien.marteau@armadeus.com>
# Created:  19/09/2018
#-----------------------------------------------------------------------------
#  Copyright (2018)  Armadeus Systems
#-----------------------------------------------------------------------------
""" extract_graph
"""

import getopt
import sys

def usage():
    """ print usages """
    print("Usage :")
    print("$ python3 extract_graph.py [options]")
    print("-h, --help              this usage message") 
    print("-v, --verilog=filename  verilog filename")

class extract_graph(object):
    """
    """

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hv:",
                                   ["help", "verilog="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(1)

    filesource = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-v", "--verilog"):
            filesource = arg

    if filesource is None:
        raise Exception("Please give a HDL source file")

    with open(filesource, "r") as fhdl:
        graph = False
        for line in fhdl:
            if line[:5] == '//END':
                sys.exit()
            if graph:
                print("{}".format(line[2:]), end="")
            if line[:10] == '//GRAPHVIZ':
                graph = True


