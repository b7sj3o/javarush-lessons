# file = open("info.txt", "w")
# file.write("Hello World!")
# file.close()
#
# file = open("info.txt", "a")
# file.write("\nNew text!")
# file.close()


def read_file():
    file = open("info.txt", "r", encoding="utf-8")
    for line in file.readlines():
        yield line
    file.close()
def read_file2():
    file = open("info.txt", "r", encoding="utf-8")
    line = file.readline()
    while line:
        line = file.readline()
        yield line
def read_file3():
    file = open("info.txt", "r", encoding="utf-8")

    while line := file.readline():
        print(repr(line))

# read_file3()

# lines = ["First line.", "Second line.", "Third line."]
# lines_lst = ["First line.\n", "Second line.\n", "Third line.\n"]
#
# file = open('example.txt', 'w')
#
# file.write("\n".join(lines))
# file.writelines(lines_lst)
#
# file.close()


# lines = ["Appending first line from list.\n","Appending second line from list\n","Appending third line from list.\n"]
#
# file = None
# try:
#     file = open('example.txt', 'a')
#     file.writelines(lines)
# finally:
#     if file:
#         file.close()
#
#
# class Test:
#     def __enter__(self): ...
#     def __exit__(self): ...


# with open("message.txt") as file:
#     data = file.read()
#     ...
#     ...
#
mgr = open("message.txt")
file = mgr.__enter__()
try:
    data = file.read()
    ...
    ...
finally:
    mgr.__exit__(None, None, None)

class IgnoreError:
    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc, tb):
        print("exit", exc_type)
        return True


# with IgnoreError() as ignored:
#     print(1/0)
# print("Didn't crash")

#
# with open("file.bin", "wb") as f:
#     f.write(b"Hello World!")
#
#
# with open("file.bin", "rb") as f:
#     print(f.read())


def read_image(image_path):
    try:
        with open(image_path, 'rb') as image_file:
            binary_data = image_file.read()
            return binary_data
    except FileNotFoundError:
        print(f"Error: {image_path} not found.")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None


def write_image(binary_data, output_path):
    if binary_data is None:
        print("No data to write.")
        return

    try:
        with open(output_path, 'wb') as output_file:
            output_file.write(binary_data)
            print(f"Successfully wrote data to {output_path}")
    except IOError as e:
        print(f"Error writing file: {e}")


import os
import shutil



def create_files(dest: str, amount: int):
    if not os.path.exists(dest):
        os.mkdir(dest)

    for i in range(1, amount+1):
        with open(f"{dest}/{str(i)}.txt", "w") as file:
            file.write(str(i))


# create_files("data", 100)
# os.makedirs('path/1/a/z')
# os.makedirs('path/1/b/x')
# os.makedirs('path/2/a/c')
# shutil.rmtree("data")

# import os
# files = os.listdir('data')
# for file in files:
#     print(file)

# for dirpath, dirnames, filenames in os.walk("path"):
#     print(dirpath, dirnames, filenames)


import pickle

# user = {
#     "name": "Bob",
#     "age": 18
# }

# with open("obj.pkl", "wb") as file:
#     pickle.dump(user, file)


with open("obj.pkl", "rb") as file:
    obj: dict = pickle.load(file)

# print(obj)


EXTENSION_MAP = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Archives': ['.zip', '.rar', '.7z', '.tar'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Scripts': ['.py', '.js', '.html']
}

def sort_folder_data(dest: str):
    for folder_name in EXTENSION_MAP.keys():
        path = os.path.join(dest, folder_name)
        if not os.path.exists(path):
            os.mkdir(path)

    for item in os.listdir(dest):
        extension = item.split(".")[-1]
        for folder_name, extensions in EXTENSION_MAP.items():
            if f".{extension}" in extensions:
                shutil.move(
                    f"{dest}/{item}",
                    f"{dest}/{folder_name}/{item}"
                )


sort_folder_data("C:\\Users\\admin\\Downloads")

