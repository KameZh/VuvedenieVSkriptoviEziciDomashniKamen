import os

def size_of_files(*argc):
    returnvalues = []
    avr_size = 0
    vid = "b"
    for file_path in argc:
        if os.path.isfile(file_path):
            avr_size += os.path.getsize(file_path)
    avr_size = avr_size // len(argc)
    if avr_size > 1000:
        avr_size = avr_size // 1000
        vid = "KB"
    elif avr_size > 1000000:
        avr_size = avr_size // 1000000
        vid = "MB"
    returnvalues.append(avr_size)
    returnvalues.append(vid)
    return returnvalues

if __name__ == "__main__":
    files = ["file1.txt", "file2.txt", "image.png"]
    total = size_of_files(*files)
    print(f"Total size of files: {total}")
    