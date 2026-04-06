import os
import shutil



directory_name = 'arranged'
parent_dir = os.path.dirname(os.getcwd())


if not os.path.exists(directory_name):
    os.mkdir(directory_name)


sub_directory_number = 5
file_set = set()


def search_types():
    parent_dir = os.path.dirname(os.getcwd())
    working_dir = os.path.join(parent_dir,"Downloads")

    for i in os.listdir(working_dir):
        type = (os.path.splitext(i))[-1].upper()
        file_set.add(type)
    
    print(file_set)
    return file_set
        
file_set = {'.PY', '.TXT', '.PNG'}


def create_dir(file_set):
    for i in (file_set):
        print('Testing',i)
        sub_directory_name = os.path.join(directory_name, 'folder_'+str(i[1:]))     #starting indexing from 1 removes the . in the file name
    

        if not os.path.exists(sub_directory_name):
            os.mkdir(sub_directory_name)
            print(f"Created {sub_directory_name}")

        else:

            if os.listdir(sub_directory_name):      #Checking if the sub directory already exists
                choice = input(f"{(os.getcwd())} already has file named {sub_directory_name} which is not empty. Do you want to overwrite it (y/n)?").lower()

                if choice == 'y':
                    shutil.rmtree(sub_directory_name)
                    print(f"Created new {sub_directory_name}")
                    os.mkdir(sub_directory_name)
                else:
                    print("Skipping file"+{sub_directory_name})


print('Directories created successfully!')

def find_file_type(file_path):

    split = os.path.splitext(file_path)
    return (split[-1][1:]).upper()




def assign_files():
    downloads_path = os.path.join(parent_dir,"Downloads") 
    file_list = os.listdir(downloads_path)
    print(file_list)

    for file in (file_list):
        print("Working on "+ file)
        current_file = os.path.join(downloads_path,file)
        if os.path.isfile(current_file):                                            # check if file
            file_type = find_file_type(file)                                        # return file type
            destination = os.path.join(parent_dir,"file_reader/arranged")
            shutil.move(current_file , f"{destination}/folder_{file_type}")
            


if __name__ == "__main__":
    sample_path = "/home/mann/Projects/Automation/Downloads/sample.py"

    print(assign_files())