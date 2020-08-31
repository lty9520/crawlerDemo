from helper import killPid
import os


cur_path = os.path.dirname(os.path.abspath(__file__))
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))


def stopServer():

    with open(rot_path + "\\pid.txt", 'r') as file:
        pid = file.readlines()

    for str_pid in pid:
        killPid(str(str_pid).strip("\n"))


if __name__ == '__main__':
    stopServer()
    with open(rot_path + "\\pid.txt", 'w') as file:
        file.truncate()