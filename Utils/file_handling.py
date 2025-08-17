def get_file_content_of(path):
    with open(path) as file:
        return file.read()