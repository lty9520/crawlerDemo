import os


def getPid():
    # 获取进程pid
    pid = os.getpid()

    cur_path = os.path.dirname(os.path.abspath(__file__))
    rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))

    # 将pid写入本地文件
    with open(rot_path + "\\pid_file.txt", 'a') as file:
        file.write(pid.__str__())
        file.write("\n")


