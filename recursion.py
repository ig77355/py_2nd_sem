from pathlib import Path


def sum_space(folder):
    size = 0
    counter = 0
    for file in folder.iterdir():
        if file.is_file():
            size += file.stat().st_size
            counter += 1
        elif file.is_dir():
            t_size, t_counter = sum_space(file)
            size += t_size
            counter += t_counter
    return size, counter


path = Path('..')
p_size, p_counter = sum_space(path)
print("Total size is: " + str(p_size) + " bytes\r\nTotal number of files: " + str(p_counter))


'''
def sum_space(folder):
    sum = 0
    for file in folder.iterdir():
        path = os.path.join(folder, file)
        if os.path.isfile(folder):
            sum += os.path.getsize(file)
        else:
            if os.path.isdir(file):
                sum += sum_space(path)
    return sum


print("Total size is:" + str(sum_space(folder)) + "byte")


def sum_space_loop(folder):
    sum_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if os.path.isfile(file_path):
                sum_size += os.path.getsize(file_path)
    return sum_size
my_folder = "../Python_Summer_2021_2/data"
print("Total size is:" + str(sum_space_loop(my_folder)) + "byte")
'''
