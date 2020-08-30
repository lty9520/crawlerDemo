import os

cur_path = os.path.dirname(os.path.abspath(__file__))
#join后的路径是简单的拼接，需要通过abspath将路径可用化
unuse_rot_path = os.path.join(cur_path, os.path.pardir)
use_rot_path = os.path.abspath(os.path.join(cur_path, os.path.pardir))
down_path = os.path.join(use_rot_path, 'down')
print("cur_path" + cur_path)
print("use_rot_path" + use_rot_path)
print("unuse_rot_path" + unuse_rot_path)
print("downpath" + down_path)