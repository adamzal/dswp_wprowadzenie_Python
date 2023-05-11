import os


def create_folders(paths):
    for path in paths:
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Utworzono folder: {path}")
        else:
            print(f"Folder już istnieje: {path}")


folders = ['zad1', 'zad1/zad11', 'zad1/zad11/zad111', 'zad1/zad12/zad121']
create_folders(folders)
os.remove('zad1')
