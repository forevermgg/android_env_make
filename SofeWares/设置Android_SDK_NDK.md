# Android 环境变量
```bash
export ANDROID_HOME=/Users/centforever/Library/Android/sdk
```
# Android tools 路径
```bash
export PATH=${PATH}:${ANDROID_HOME}/tools
```
# Android 平台工具路径
```bash
export PATH=${PATH}:${ANDROID_HOME}/platform-tools
```
# Android NDK路径
```bash
export ANDROID_NDK=/Users/centforever/Library/Android/sdk/ndk-bundle
export ANDROID_NDK_HOME=/Users/centforever/Library/Android/sdk/ndk/21.4.7075529
export PATH=$ANDROID_NDK_HOME:$PATH
export PATH=$PATH:$ANDROID_NDK_HOME/toolchains/aarch64-linux-android-4.9/prebuilt/darwin-x86_64/bin
export PATH=$PATH:$ANDROID_NDK_HOME/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64/bin
export PATH=$PATH:$ANDROID_NDK_HOME/toolchains/x86-4.9/prebuilt/darwin-x86_64/bin
export PATH=$PATH:$ANDROID_NDK_HOME/toolchains/x86_64-4.9/prebuilt/darwin-x86_64/bin
#export EMULATOR_PATH=/Users/centforever/Library/Android/sdk/emulator
#export PATH=${PATH}:${EMULATOR_PATH}/
#Android 模拟器路径
export PATH=${PATH}:${ANDROID_HOME}/emulator
```
# cmake 路径
```
/Users/centforever/Library/Android/sdk/cmake
```
# sdkmanager
```bash
❯ pwd
/Users/centforever/Library/Android/sdk/tools/bin
❯ ls
apkanalyzer       jobb              screenshot2
archquery         lint              sdkmanager
avdmanager        monkeyrunner      uiautomatorviewer
```
# 安装ndk

# 查看clang信息
```bash
❯ cat $ANDROID_HOME/ndk/25.1.8937393/toolchains/llvm/prebuilt/darwin-x86_64/AndroidVersion.txt
14.0.6
based on r450784d
for additional information on LLVM revision and cherry-picks, see clang_source_info.md%
```

