import os


def kill(pid):
    # kill 相应pid进程
    if os.name == 'nt':
        # windows
        cmd = 'taskkill /pid ' + str(pid) + '/f'
        try:
            os.system(cmd)
        except Exception as e:
            print(e)

    elif os.name == 'posix':
        # linux
        cmd = 'kill ' + str(pid)
        try:
            os.system(cmd)
        except Exception as e:
            print(e)
    else:
        print('Undefined os.name')

