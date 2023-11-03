import shutil

from common import execCmdBySys


def checkWhich(cmd):
    return shutil.which(cmd)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print(checkWhich("flatc"))
    print(checkWhich("ffmpeg"))
    print(checkWhich("node"))
    # print(execCmdByPopen("which python"))
    # print(execCmdBySys("/Library/Frameworks/Python.framework/Versions/2.7/bin/python -V"))
    print(execCmdBySys("python3 -V"))
    # execCmdBySys("which python")
