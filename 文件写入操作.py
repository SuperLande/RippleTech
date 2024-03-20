# 打开文件
import time

f = open('python.txt', 'w')
# 文件写入，并未真正写入，只是存到缓存区
#f.write('hello word')
# 内容刷新,此时才开始写入硬盘
#f.flush()
#time.sleep(600000)
# close关闭
#f.close()
# 打开一个已经存在的文件
# write写入，flash刷新
f.write('hiahiahia')
f.flush()
f.close()