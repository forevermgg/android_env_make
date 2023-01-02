# 这是一个示例 Python 脚本。
import os
import subprocess


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

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


def test():
    subprocess.check_call(["brew", "search", "@jdk"])


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # test()
    # execCmdBySys("brew install binutils")
    # execCmdBySys("javac -version")
    # execCmdBySys("/usr/libexec/java_home -V")
    execCmdBySys("brew install --cask jetbrains-toolbox")
    execCmdBySys("brew install openjdk@11")
    print(execCmdByPopen("/usr/libexec/java_home -v11"))
    # print(execCmdByPopen("javac -version"))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
