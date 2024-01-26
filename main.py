import os
import shutil

project_path = 'G:\\SD&S Tracking'
employee_list_path = "employees_list.txt"
employee_list: list[str] = []

# create new site folder and copy the am1 and 2 files into it
def initialize_sitename(s: str):
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

def initialize_employee_list():
    try:
        with open(employee_list_path, 'r') as file:
            content = file.read()
            employee_list = content.splitlines()
            print("current employee list: " + ', '.join(employee_list))
    except FileNotFoundError:
        print(f"The file was not found!")

def add_new_employee(name: str, pin: str):
    data = name + '-' + str(hash(pin))
    try:
        with open(employee_list_path, 'a') as file:
            file.write(data)
    except FileNotFoundError:
        print(f"The file was not found!")        

def main():
    initialize_employee_list()

    if not os.path.exists(project_path):
        os.makedirs(project_path)

    sitename_list: list[str] = os.listdir(project_path)
    print("current Sitename list: " + ', '.join(sitename_list))

    sitename_new: str = input("Enter site name to create new: ")
    initialize_sitename(sitename_new)

if __name__ == "__main__":
    main()