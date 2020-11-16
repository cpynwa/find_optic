import jxmlease

def interStatus(a):
    inter_list=[]
    inter_status=[]
    with open(a,'rb') as xml:
        root = jxmlease.parse(xml)
        
    for node in root.find_nodes_with_tag('physical-interface'):
        inter_list.append(node['name'].get_cdata())
        inter_status.append(node['oper-status'].get_cdata())
    r = dict(zip(inter_list,inter_status))
    return r
