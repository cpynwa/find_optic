import find_optics as fo
import find_interfaces as fi
import sc_flielist as cfl
import si_filelist as ifl
import re
import sys

sys.stdout = open('output.txt','w')

for a, b in zip(cfl.sc_fileList(),ifl.si_fileList()):
    print(a, b,)
    key_list=list(fo.useCheck(a).keys())
    for key_list1 in key_list:
        aaaa=fo.useCheck(a).get(key_list1)
        bbbb=fi.interStatus(b).get(key_list1)
        cccc=key_list1
        print("[",cccc,":",end=" ")
        print(aaaa,end=" ")
        print(":",bbbb,"]")
