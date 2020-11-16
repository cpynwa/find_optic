import glob

def si_fileList():
    path = "./show_interfaces_terse/*"
    file_list = glob.glob(path)
    file_list_1 = [file for file in file_list if file.endswith(".xml")]
    return file_list_1
