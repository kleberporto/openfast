import os.path


def remove_extension(file):
    return file[0:len(file) - 4]


def get_file_name(file_full_path):
    file_name = ""
    for char in file_full_path:
        if char == "/":
            file_name = ""
        else:
            file_name += char
    return file_name


def delete_files(file):
    if os.path.exists(file):
        os.remove(file)
