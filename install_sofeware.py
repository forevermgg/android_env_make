# 这是一个示例 Python 脚本。
import subprocess

from common import execCmdBySys


def test():
    subprocess.check_call(["brew", "search", "@jdk"])


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # test()
    execCmdBySys("brew install git")
    execCmdBySys("brew install git-lfs")
    execCmdBySys("brew install gradle")
    execCmdBySys("brew install binutils")
    execCmdBySys("brew install coreutils")
    execCmdBySys("brew install bloaty")
    execCmdBySys("brew install patchelf")
    execCmdBySys("brew install util-linux")
    execCmdBySys("brew install bazel")
    execCmdBySys("brew install curl")
    execCmdBySys("brew install ffmpeg")
    execCmdBySys("brew install media-info")
    execCmdBySys("brew install clang-format")
    execCmdBySys("brew install tree")