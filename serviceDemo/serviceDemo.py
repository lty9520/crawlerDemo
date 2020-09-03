#encoding = utf-8
import inspect
import os
import servicemanager
import subprocess
import sys
import win32event
import win32service

import win32serviceutil
import logging

import winerror


this_file = inspect.getfile(inspect.currentframe())
cur_path = os.path.abspath(os.path.dirname(this_file))
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))


class pythonServiceDemo(win32serviceutil.ServiceFramework):

    #Service name
    _svc_name_ = "PythonService"
    #Service name in win
    _svc_display_name_ = "Python Service Test"
    #Service description
    _svc_description_ = "this is a description of python service test code!"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):

        logger = logging.getLogger('[PythonService]')


        handler = logging.FileHandler(os.path.join(cur_path, "service.log"))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        self.logger.info("service is run ...")
        self.start()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.logger.info("service is stop ...")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop()


class myService(pythonServiceDemo):
    def start(self):
        """ start service"""
        self.child = subprocess.Popen("python proxyPool.py server", cwd=rot_path)
        logging.warning('child pid is %s', self.child.pid)

    def stop(self):
        """ kill the service pid"""
        os.system("taskkill /t /f /pid %s", self.child.pid)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            evtsrc_dll =  os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(pythonServiceDemo)
            servicemanager.Initialize('PythonService', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(myService)