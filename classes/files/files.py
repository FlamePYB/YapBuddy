class FileContent:
    def __init__(self,path):
        with open(path,"r") as file:
            self.file =file.read()
        return self.file
class Ressource:
    def __init__(self):
        pass