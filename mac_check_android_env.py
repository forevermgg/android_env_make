import shutil
from common import execCmdBySys, execCmdByPopen


def checkWhich(cmd):
    return shutil.which(cmd)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(checkWhich("flatc"))
    print(checkWhich("ffmpeg"))
    print(checkWhich("node"))
    print(execCmdByPopen("which python"))
    execCmdBySys("which python")
