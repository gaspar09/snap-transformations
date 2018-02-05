import sys
import snap
import time
from my_cfg import NW

def t():
    return time.time()

def reportTime(t0, msg):
    print "%s: %f" % (msg,t()-t0) 

def tungraph():
    t0=t()
    G = snap.LoadEdgeList(snap.PUNGraph, NW.twitter, 0, 1)
    reportTime(t0, "TUNGRAPH")

def ttable():
    t0=t()
    context = snap.TTableContext()
    
    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("Col1", snap.atInt))
    schema.Add(snap.TStrTAttrPr("Col2", snap.atInt))

    table = snap.TTable.LoadSS(schema, NW.twitter, context, "\t", snap.TBool(False))
    reportTime(t0, "TTABLE")


def tneanet():
    t0=t()
    G = snap.LoadEdgeList(snap.PNEANet, NW.twitter, 0, 1)
    reportTime(t0, "TNEANET")

def tmmnet():
    t0=t()
    G = snap.LoadEdgeList(snap.PUNGraph, NW.small, 0, 1)
    reportTime(t0, "TMMNET")

def main(opt):
    if opt == 1:
        tungraph()
    elif opt == 2:
        ttable()
    elif opt == 3:
        tneanet()
    elif opt == 4:
        tmmnet()

if __name__=="__main__":
    main(int(sys.argv[1]))
