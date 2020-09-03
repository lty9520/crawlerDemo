# encoding = utf-8
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

# this_file = inspect.getfile(inspect.currentframe())
cur_path = os.path.split(os.path.abspath(__file__))[0]  # os.path.abspath(os.path.dirname(__file__))
rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
log_path = os.path.join(rot_path, 'log')


class pythonServiceDemo(win32serviceutil.ServiceFramework):
    # Service name
    _svc_name_ = "UrlService"
    # Service name in win
    _svc_display_name_ = "Url Service"
    # Service description
    _svc_description_ = "This service provide downloading url pool service!"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.logger = self._getLogger()
        self.run = True

    def _getLogger(self):
        logger = logging.getLogger('[Url Service Log]')

        handler = logging.FileHandler(os.path.abspath(os.path.join(log_path, "url_service.log")))

        formatter = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.setLevel(logging.INFO)

        return logger

    def SvcDoRun(self):
        self.logger.info("url service is run ...")
        self.start()
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)

    def SvcStop(self):
        self.logger.info("url service is stop ...")
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.stop()


class myService(pythonServiceDemo):
    def start(self):
        """ start service"""
        self.child = subprocess.Popen("python proxyPool.py urlserver", cwd=rot_path)
        # self.logger.info('child pid is %s', os.getpid())
        # self.logger.info('parent pid is %s', os.getppid())

    def stop(self):
        """ kill the service pid"""
        self.child.terminate()
        # os.system("taskkill /t /f /pid %s", os.getppid())
        # os.system("taskkill /t /f /pid %s", os.getpid())


if __name__ == '__main__':
    if len(sys.argv) == 1:
        try:
            evtsrc_dll = os.path.abspath(servicemanager.__file__)
            servicemanager.PrepareToHostSingle(pythonServiceDemo)
            servicemanager.Initialize('UrlService', evtsrc_dll)
            servicemanager.StartServiceCtrlDispatcher()
        except win32service.error as details:
            if details[0] == winerror.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
                win32serviceutil.usage()
    else:
        win32serviceutil.HandleCommandLine(myService)
