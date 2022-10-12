import shutil

def hard_disk_check():
 com = shutil.disk_usage("/")
 print(com)


hard_disk_check()
