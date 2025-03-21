# 这是一个示例 Python 脚本。
import subprocess

from common import execCmdBySys, execCmdByPopen


def test():
    subprocess.check_call(["brew", "search", "@jdk"])


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    execCmdBySys("javac -version")
    execCmdBySys("/usr/libexec/java_home -V")
    # execCmdBySys("brew install --cask jetbrains-toolbox")
    # execCmdBySys("brew install openjdk@11")x
    print(execCmdByPopen("/usr/libexec/java_home -v11"))
    # print(execCmdByPopen("javac -version"))

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
