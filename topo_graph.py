import pygraphviz as pgv
import sys
import matplotlib.pyplot as plt
import re
#===============================================================================

_node_attrs = {
        #### topo start
        # layout options for topo plot:
        "node":[],
        "label": {},
        "graph_layout": "neato",
        "shape":"circle",
        # node shape options are provided in NodeShapeList.txt file, default is circle
        "color":"black",
        # node color options are provided in ColorList.txt file, default is white with black border
        "fixedsize":"true", 
        "fontsize":8,
        "fontcolor":"black", 
	# node font size default is 8
        "style":"filled",
        "fillcolor":"white"
        }
_edge_attrs = {
        "edge":[],
        "label":[],
        "color":'blue',
        "style":'solid',
        #style options are solid, dashed, dotted, bold
        # edge color options are provided in ColorList.txt file, default is set to black
        "penwidth":1.0,
        "dir":"forward",  
        # edge line thickness
        "headlabel":"",
        "taillabel":"",
        #"edge_label_pos": [0.5] #0.3?
        "arrowhead":"none",
        # default is set as normal, list of available options are provided in "ArrowType.txt"
        "arrowtail":"none",
        # default is set as none, list of available options are provided in "ArrowType.txt"
        "arrow_dir":"forward",
        # arrow direction options are "forward", "back","both","none". Default is set as "forward". 
        #### topo end
        }


class topo_graph():

    def __init__(self, node_attrs, edge_attrs, outputfile):
        attrs0 = dict(_node_attrs) #new dict
        attrs1 = dict(_edge_attrs)
        attrs0.update(node_attrs)
        attrs1.update(edge_attrs)
        self.node_attrs = attrs0
        self.edge_attrs = attrs1
        self.outfile = outputfile

    def add_node_attr(self, attr_type, tgraph):
        if type(self.node_attrs[attr_type]) is str or type(self.node_attrs[attr_type]) is int:
            tgraph.node_attr[attr_type]=self.node_attrs[attr_type] 
        elif isinstance(self.node_attrs[attr_type], dict):
            for k, v in self.node_attrs[attr_type].items():
                nnode = tgraph.get_node(k)
                nnode.attr[attr_type]=v
        else:         
            print "incorrect type"+str(attr_type)+" parameters provided."
        return tgraph

    def add_edge_attr(self, attr_type, tgraph):
        if type(self.edge_attrs[attr_type]) is str or type(self.edge_attrs[attr_type]) is int:
            tgraph.edge_attr[attr_type]=self.edge_attrs[attr_type] 
        elif isinstance(self.edge_attrs[attr_type], dict):
            for k, v in self.edge_attrs[attr_type].items():
                nnode = tgraph.get_edge(k)
                nnode.attr[attr_type]=v
        return tgraph

    def add_node_defaults(self, topo):
        topo.node_attr['style']='filled'
        topo.node_attr['shape']='circle'
        topo.node_attr['fixedsize']='false'
        topo.node_attr['fontcolor']='black'
        topo.node_attr['fillcolor']='white' 
        return topo

 
    
    def add_nodes(self, topo):
        for index, node in enumerate(self.node_attrs['node']):
            topo.add_node(node)
        return topo
    
    def add_node_attrs(self, topo):
        topo = self.add_node_attr('color',topo)
        topo = self.add_node_attr('style',topo)
        topo = self.add_node_attr('fillcolor',topo)
        topo = self.add_node_attr('fixedsize',topo)
        topo = self.add_node_attr('fontsize',topo)
        topo = self.add_node_attr('shape',topo)
        topo = self.add_node_attr('label',topo)            
        return topo

    def add_edge_attrs(self, topo):
        topo = self.add_edge_attr('color',topo)
        topo = self.add_edge_attr('style',topo)
        topo = self.add_edge_attr('penwidth',topo)
        topo = self.add_edge_attr('dir',topo)
        topo = self.add_edge_attr('arrowhead',topo)
        topo = self.add_edge_attr('arrowtail',topo)
        topo = self.add_edge_attr('arrow_dir',topo)            
        return topo    

    def add_edges(self, topo):
        for index, edge in enumerate(self.edge_attrs['edge']):
            topo.add_edge(edge)
        return topo
            
    def draw_topo(self):
        A=pgv.AGraph()
        A = self.add_nodes(A)
        #A = self.add_node_defaults(A)
        A = self.add_node_attrs(A)
        #A = self.add_edge_defaults(A)
        A = self.add_edges(A)
        A = self.add_edge_attrs(A)
        
        A.layout(prog='neato',args='-Goverlap=scale -Gsplines=true')
        A.draw(self.outfile)
        #print("Wrote "+nodeattrib['outputfile'])    


def main():
    nodes = {}
    links = {}
    trytopo =  topo_graph(nodes, links, 'topopy.svg')
    drawtopo = trytopo.draw_topo()
if __name__ == '__main__':
	main()
