import os

def list_files(path="."):
    return os.listdir(path)

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def create_file(path, content):
    with open(path, "w") as f:
        f.write(content)

    return f"Archivo {path} creado"
