
# import need manager module

#-----Redis struct-----
#
#   use_proxy   --->   useful proxy ips
#                              |
#                              |  Json
#                              ---> {
#                                    "proxy" : x.x.x.x:xx,  ---> proxyIP
#                                    "fail_count" : x,      ---> 1 is pass, 0 is fail
#                                    "region" : x,          ---> IP region
#                                    "type" : x,            ---> type of proxy
#                                    "source" : x,          ---> proxy source
#                                    "check_count" : x,     ---> 1 is pass, 0 is fail
#                                    "last_status" : x,     ---> 1 is pass, 0 is fail
#                                    "last_time" : xx       ---> last prove time
#                                   }
#
#   down_ulr    --->   down file urls
#                              |
#                              |  Json
#                              ---> {
#                                    "title" : xx           ---> article title
#                                    "down_url" : xx             ---> file down url
#                                    "down_count" : x       ---> down count
#                                    "down_status" : x      ---> 1 is down, 0 is pause down
#                                   }
#

import requests

__all__ = ['requests']