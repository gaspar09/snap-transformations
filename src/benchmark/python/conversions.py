import sys
import snap
import time
from my_cfg import NW

def t():
    return time.time()

def reportTime(t0, msg):
    print "%s: %f" % (msg,t()-t0) 
    return t()

def tungraphToBinary():
    t0=t()
    G = snap.LoadEdgeList(snap.PUNGraph, NW.twitter, 0, 1)
    t1=reportTime(t0, "TUNGRAPH")
    FOut = snap.TFOut(NW.twitter_binary)
    G.Save(FOut)
    FOut.Flush()
    t2=reportTime(t1, "TUNGRAPH save binary")
    FIn = snap.TFIn(NW.twitter_binary)
    G2 = snap.TUNGraph.Load(FIn)
    reportTime(t2, "TUNGRAPH load binary")

def ttableToTmmnet():
    
    # load table
    t0=t()
    context = snap.TTableContext()

    schema = snap.Schema()
    schema.Add(snap.TStrTAttrPr("srcID", snap.atInt))
    schema.Add(snap.TStrTAttrPr("dstID", snap.atInt))


    edge_table = snap.TTable.LoadSS(schema, NW.small, context, "\t", snap.TBool(False))
    t1 = reportTime(t0, "TTABLE")

    # convert table to TMMNet
    mmnet = snap.TMMNet.New()
    edgeattrv = snap.TStrV()
    edgeattrv.Add("edgeattr1")

    CrossG = snap.LoadCrossNetToNet(mmnet, "Mode1", "Mode2", "Cross1", edge_table, "srcID", "dstID", edgeattrv)
    
    reportTime(t1, "convert TTABLE to CrossNet")
    

def tuntoall():
    FIn = snap.TFIn(NW.twitter_binary)
    G = snap.TUNGraph.Load(FIn)

    t0=t()
    # convert undirected graph to directed
    GOut = snap.ConvertGraph(snap.PNGraph, G)
    t1=reportTime(t0, "convert TUNGRAPH to TNGRAPH")

    # convert directed graph to a network
    GOut = snap.ConvertGraph(snap.PNEANet, G)
    reportTime(t1,"convert TUNGRAPH to TNEANet")

def main(opt):
    if opt == 1:
        tuntoall()
    if opt == 2:
        ttableToTmmnet()

if __name__=="__main__":
    main(int(sys.argv[1]))
