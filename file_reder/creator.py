import os
import shutil



directory_name = 'arranged'

if not os.path.exists(directory_name):
    os.mkdir(directory_name)


sub_directory_number = 5


for i in range(sub_directory_number + 1):
    sub_directory_name = os.path.join(directory_name, 'file_'+str(i))
 

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