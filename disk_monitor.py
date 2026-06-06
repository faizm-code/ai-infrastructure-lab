import shutil

total, used, free = shutil.disk_usage("/")
print(f"Disk Used: {used // (2**30)} GB")
print(f"Disk Free: {free // (2**30)} GB")
