import os
import subprocess


def execCmdBySys(cmd):
    try:
        # print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        # 没有返回值
        os.system(cmd)
        # print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except:
        print('%s\t 运行失败' % cmd)


def execCmdByPopen(cmd):
    result = os.popen(cmd).read()
    return result


# subprocess.Popen()
# 返回值：Popen类的构造函数，返回结果为subprocess.Popen对象，脚本命令的执行结果可以通过stdout.read()获取。
def execCmdBySubProcessPopen(cmd):
    # 执行cmd命令，如果成功，返回(0, 'xxx')；如果失败，返回(1, 'xxx')
    res = subprocess.Popen(cmd,
                           shell=False,
                           stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE)  # 使用管道
    result = res.stdout.read()  # 获取输出结果
    res.wait()  # 等待命令执行完成
    res.stdout.close()  # 关闭标准输出
    return result
