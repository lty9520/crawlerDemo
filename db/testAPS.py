# -*- coding: utf-8 -*-
"""
--------------------------------
    @File Name:      testAPS.py
    @Description:    
    @Author:         
    @Date:           2020/9/13 8:19
    @Software:       PyCharm
--------------------------------
    Change Activity:
                     2020/9/13 :
"""
import pickle


from apscheduler.jobstores.memory import MemoryJobStore
from apscheduler.jobstores.redis import RedisJobStore

__author__ = 'LHY'

import time

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor

# 配置执行其 Processpool 同时最多3个进程
executor = {
    'default': {'type': 'threadpool', 'max_workers': 20},
    'processpool': ProcessPoolExecutor(max_workers=5)
}

# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, password='12345')
# r = redis.StrictRedis(connection_pool=pool)  # 连接redis数据库，decode_responses参数决定hget()返回值为string类型
# 定义jobstore  使用redis 存储job信息
connect_args = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '12345'
}
# redis_store = RedisJobStore(3, host='127.0.0.1', port=6379, password='12345')
jobstores = {
    'default': RedisJobStore(db=2,
                             jobs_key='apscheduler.jobs',
                             run_times_key='apscheduler.run_times',
                             pickle_protocol=pickle.HIGHEST_PROTOCOL,
                             **connect_args)

}

job_defaults = {
    'coalesce': False,
    'max_instances': 3
}


def myJob():
    print(time.time())


# 创建调度器对象，指定执行器
scheduler = BackgroundScheduler(jobstores=jobstores, executors=executor, job_defaults=job_defaults)

# 添加定时任务
'''
# 时间的设置
weeks (int) – number of weeks to wait
days (int) – number of days to wait
hours (int) – number of hours to wait
minutes (int) – number of minutes to wait
seconds (int) – number of seconds to wait
start_date (datetime|str) – starting point for the interval calculation
end_date (datetime|str) – latest possible date/time to trigger on
timezone (datetime.tzinfo|str) – time zone to use for the date/time calculations
'''
scheduler.add_job(myJob, "interval", minutes=1, id="myId", name="testMyJob")

if __name__ == '__main__':
    # 开始调度器
    scheduler.start()
    while 1:
        time.sleep(5 * 60)
