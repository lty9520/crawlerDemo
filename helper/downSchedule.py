# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     downScheduler
   Description :
   Author :        LHY
   date：          2020/08/29
-------------------------------------------------
   Change Activity:
                   2020/08/29: urlScheduler
-------------------------------------------------
"""
import random

__author__ = 'LHY'

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor

from handler.configHandler import ConfigHandler
from handler.logHandler import LogHandler
from helper.urlDown import execDown


def runDownScheduler():
    """
    down shecdule random(1-5)hour
    :return:
    """
    timezone = ConfigHandler().timezone
    scheduler_log = LogHandler("schedule")
    scheduler = BackgroundScheduler(logger=scheduler_log, timezone=timezone)

    intlTime = random.randint(1, 5)
    scheduler.add_job(execDown(random.randint(5, 30)), 'interval', hour=intlTime, id="down_url", name="url下载")

    executors = {
        'default': {'type': 'threadpool', 'max_workers': 20},
        'processpool': ProcessPoolExecutor(max_workers=5)
    }

    job_defaults = {
        'coalesce': False,
        'max_instances': 10
    }

    scheduler.configure(executors=executors, job_defaults=job_defaults, timezone=timezone)

    scheduler.start()


if __name__ == '__main__':
    runDownScheduler()