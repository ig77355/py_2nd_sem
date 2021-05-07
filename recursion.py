from pathlib import Path


def sum_space(folder):
    size = 0
    counter = 0
    for file in folder.iterdir():
        # if the object is a file
        if file.is_file():
            # calculating the size of a file
            size += file.stat().st_size
            # calculating how many files are in a current folder
            counter += 1
        # if the object is a folder
        elif file.is_dir():
            # creating a tuple consisting of size and counter of files
            # here the recursion is used, as sum_space function is used
            t_size, t_counter = sum_space(file)
            size += t_size
            counter += t_counter
    return size, counter

# setting the path to the folder - going backward 2 times in the current file path
path = Path('..')
p_size, p_counter = sum_space(path)
# dividing the above tuple's results into 2 separate numbers and sentences
print("Total size: " + str(p_size) + " bytes\r\nTotal number of files: " + str(p_counter))