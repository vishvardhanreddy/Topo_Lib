import pygraphviz as pgv
import sys
import matplotlib.pyplot as plt
import re
from topo_graph import topo_graph
#===============================================================================
def read_CSV(filename,header_row=1):
  try:
    inFile = open(filename,'r')
  except IOError:
    return {}

  row = 0
  array = {}
  for line in inFile:
    row += 1
    line = re.sub('[\n\r]','',line)     # Remove newline & linefeed
    flds = re.split(',', line)

    if row == header_row:
      array['HEADER'] = flds
    elif not re.search(r'^$',line) and not re.search(r'^#',line):
      array[line] = flds

  inFile.close()
  return array

      
# draw example

nodefile = "00.NODES.csv"     
tmp_nodes = read_CSV(nodefile, header_row=0)
linkfile = "02.NE-IPMAP.csv"
tmp_links = read_CSV(linkfile, header_row=0)


all_nodes = {}
for i in tmp_nodes:
  all_nodes[tmp_nodes[i][0]] = tmp_nodes[i][1]
 
nodes = []
links = []
for i in tmp_links:
  if tmp_links[i][0] in all_nodes and tmp_links[i][3] in all_nodes:
    edgeOne = str(tmp_links[i][0])+':'+str(tmp_links[i][1])
    edgeTwo = str(tmp_links[i][3])+':'+str(tmp_links[i][4])
    links.append((edgeOne, edgeTwo))
    nodes.append(edgeOne)
    nodes.append(edgeTwo)
nodes = set(nodes)
_node_attrs = {
        #### topo start
        # layout options for topo plot:
        "node":nodes,
        "graph_layout": "neato",
        "shape":"oval",
        # node shape options are provided in NodeShapeList.txt file, default is circle
        # node color options are provided in ColorList.txt file, default is white with black border
        "fixedsize":"false", 
        "fontsize":8,
        "fontcolor":"black", 
	# node font size default is 8
        "style":"filled",
        }
_edge_attrs = {
        "edge":links,
        "color":'blue',
        "style":'dashed',
        #style options are solid, dashed, dotted, bold
        # edge color options are provided in ColorList.txt file, default is set to black
        "penwidth":1.0,
        "dir":"forward",  
        # edge line thickness
        #"edge_label_pos": [0.5] #0.3?
        "arrowhead":"normal",
        # default is set as normal, list of available options are provided in "ArrowType.txt"
        "arrowtail":"none",
        # default is set as none, list of available options are provided in "ArrowType.txt"
        "arrow_dir":"forward",
        # arrow direction options are "forward", "back","both","none". Default is set as "forward". 
        #### topo end
        }

trytopo =  topo_graph(_node_attrs, _edge_attrs, 'node_attrib.svg')
trytopo.draw_topo()
#draw_node(set(nodes), links, node_attrib)
