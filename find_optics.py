import re
import jxmlease


def useCheck(a):
    interface_L = []
    description_L = []
    with open(a,'rb') as xml:
        root = jxmlease.parse(xml)
    for node in root.find_nodes_with_tag('chassis-module'):
        name = node['name'].get_cdata()
        for snode in node.find_nodes_with_tag('chassis-sub-module'):
            sname = snode['name'].get_cdata()
            for ssnode in snode.find_nodes_with_tag('chassis-sub-sub-module'):
                ssname = ssnode['name'].get_cdata()
                ssdescription = ssnode['description'].get_cdata()
                iname = str(int(re.findall('\d+', name)[0]))
                isname = str(int(re.findall('\d+', sname)[0]))
                issname = str(int(re.findall('\d+', ssname)[0]))
                if ssdescription == "SFP+-10G-SR" or ssdescription == "SFP+-10G-LR":
                    interface="xe-"+iname+"/"+isname+"/"+issname
                    interface_L.append(interface)
                    description_L.append(ssnode['description'].get_cdata())
                elif ssdescription == "XFP-10G-SR" or ssdescription == "XFP-10G-LR":
                    interface="xe-"+iname+"/"+isname+"/"+issname
                    interface_L.append(interface)
                    description_L.append(ssnode['description'].get_cdata())
                elif ssdescription == "SFP-SX" or ssdescription == "SFP-LX10":
                    interface="ge-"+iname+"/"+isname+"/"+issname
                    interface_L.append(interface)
                    description_L.append(ssnode['description'].get_cdata())
                else:
                    #print('please check interface type')
                    interface=iname+"/"+isname+"/"+issname
                    interface_L.append(interface)
                    description_L.append(ssnode['description'].get_cdata())
    r = dict(zip(interface_L,description_L))
    return r
