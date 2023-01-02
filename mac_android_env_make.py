# 这是一个示例 Python 脚本。
import datetime
import os
import subprocess


# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。

def execCmd(cmd):
    try:
        print("命令%s开始运行%s" % (cmd, datetime.datetime.now()))
        os.system(cmd)
        print("命令%s结束运行%s" % (cmd, datetime.datetime.now()))
    except:
        print('%s\t 运行失败' % cmd)


def test():
    subprocess.check_call(["brew", "search", "@jdk"])


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # test()
    execCmd("/usr/libexec/java_home -V")
    execCmd("brew install binutils")
    execCmd("brew install @jdk17")
    execCmd("javac -version")

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
