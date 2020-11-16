import sys
import jxmlease
import glob

class FileList:
    def file_list(self, path):
        file_list = glob.glob(path)
        file_list_1 = [file for file in file_list if file.endswith(".xml")]
        return file_list_1

class Serch:
    def interStatus(self, a):
        inter_list = []
        inter_status = []
        with open(a, 'rb') as xml:
            root = jxmlease.parse(xml)
            for node in root.find_nodes_with_tag('physical-interface'):
                inter_list.append(node['name'].get_cdata())
                inter_status.append(node['oper-status'].get_cdata())
            r = dict(zip(inter_list, inter_status))
            return r

    def useCheck(self, a):
        with open(a, 'rb') as xml:
            interface_L = []
            description_L = []
            root = jxmlease.parse(xml)
            for fpc in root.find_nodes_with_tag('chassis-module'):
                fpc_num = fpc['name'].get_cdata()
                for pic in fpc.find_nodes_with_tag('chassis-sub-module'):
                    pic_num = pic_num['name'].get_cdata()
                    for sfp in pic.find_nodes_with_tag('chassis-sub-sub-module'):
                        sfp_num = sfp['name'].get_cdata()
                        ssdescription = sfp['description'].get_cdata()
                        iname = str(int(re.findall('\d+', fpc_num)[0]))
                        isname = str(int(re.findall('\d+', pic_num)[0]))
                        issname = str(int(re.findall('\d+', sfp_num)[0]))
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
            r = dict(zip(interface_L, description_L))
            return r




def main():
    sys.stdout = open('output.txt', 'w')
    for a, b in zip(FileList.file_list("./show_chassis_hardware/*"), FileList.file_list("./show_interfaces_terse/*")):
        print(a, b)
        key_list = list(useCheck(a).keys())
        for key_list1 in key_list:
            aaaa = useCheck(a).get(key_list1)
            bbbb = interStatus(b).get(key_list1)
            cccc = key_list1
            print("[", cccc, ":", end=" ")
            print(aaaa, end=" ")
            print(":", bbbb, "]")

main()