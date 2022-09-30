import os #os for os walk through the files

def count_lines(directory, extension): # the directory and the file path
    num_files = 0      # the could of files present of the given extension 
    lines_total = []   # the count of lines

    for root, dirs, files in os.walk(directory):  # walk through the files and open them
        for f in files:
            if f.endswith(extension):             # file with particular extension of .csv or .txt 
                num_files += 1
                filename = os.path.join(root, f)
                num_lines = sum(1 for _ in open(filename))
                lines_total.append(num_lines)
                print(filename, '\t\t', num_lines)     # print the file path and the number of lines present in each file

    total = sum(lines_total)
    avg = total / num_files

    print("\nNumber of files found: ", num_files)
    print("Total number of lines: ", total)
    print("Average lines per file: ", avg)

def enter_path():
    path = input("Enter the path: ")  
    file_extension = input("Enter the file extension:(.txt or .csv or leave blank) ")

    print("\nPath name: ", path)

    if file_extension:
        print("File extension: ", file_extension)
    else:
        file_extension = '.txt'
        print("File extension: ", file_extension)


    print("\nThe files are: ")
    return path,file_extension

if __name__ == "__main__":

    path,file_extension = enter_path()
    count_lines(path, file_extension)
