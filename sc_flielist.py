import glob

def sc_fileList():
    path = "./show_chassis_hardware/*"
    file_list = glob.glob(path)
    file_list_1 = [file for file in file_list if file.endswith(".xml")]
    return file_list_1
