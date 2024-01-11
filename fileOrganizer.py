import os, shutil

path = r"C:/Users/username/Downloads/" #replace 'username' with your username

file_name = os.listdir(path)

folder_names = ['csv files', 'image files', 'doc files', 'pdf files', 'zip files', 'exe files', 'video files', 'audio files']


for loop in range(0, 8):
    if not os.path.exists(path + folder_names[loop]):
        os.makedirs((path + folder_names[loop]))


for file in file_name:
    if ".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)

    elif ".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file) 

    elif ".docx" in file and not os.path.exists(path + "doc files/" + file):
        shutil.move(path + file, path + "doc files/" + file)

    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)
    
    elif ".zip" in file and not os.path.exists(path + "zip files/" + file):
        shutil.move(path + file, path + "zip files/" + file)
    
    elif ".exe" in file and not os.path.exists(path + "exe files/" + file):
        shutil.move(path + file, path + "exe files/" + file)

    elif ".mp4" in file and not os.path.exists(path + "video files/" + file):
        shutil.move(path + file, path + "video files/" + file)

    elif ".mp3" in file and not os.path.exists(path + "audio files/" + file):
        shutil.move(path + file, path + "audio files/" + file)
    
    else:
        print("Some files were not moved")
