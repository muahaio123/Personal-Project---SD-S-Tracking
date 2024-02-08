import os
import shutil
import hashlib

project_path = 'G:\\SD&S Tracking'
sitename_list: list[str] = []
current_sitename: str
current_user: str
current_sitename_path: str

def initialize_sitename_list():
    global sitename_list
    sitename_list = os.listdir(project_path)
    return sitename_list

def set_current_sitename(sitename: str):
    global current_sitename, current_sitename_path
    current_sitename = sitename
    current_sitename_path = project_path + "\\" + current_sitename
    return current_sitename

def set_current_user(username: str):
    global current_user
    current_user = username
    return current_user

# create new site folder and copy the am source files into it
def initialize_sitename(s: str):
    print(f"initialize_sitename({s})")
    am_source_files_path = os.getcwd() + "\\am_source_files"

    # create new folder for that site
    sitename_path = project_path + '\\' + s
    if not os.path.exists(sitename_path):
        os.makedirs(sitename_path)
    
    # copy the am1 am2 source files to that folder
    # list all items inside AM_source_files
    for filename in os.listdir(am_source_files_path):
        source_file = am_source_files_path + "\\" + filename
        destination_file = sitename_path + "\\" + filename

        # Check if source is a file and not exist in destination folder
        if os.path.isfile(source_file) and not os.path.exists(destination_file):
            shutil.copy(source_file, destination_file)
    
    initialize_sitename_list()