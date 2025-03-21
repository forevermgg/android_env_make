brew install openjdk@11
# 1.一定先把JAVA_HOME 清空
unset JAVA_HOME
 
# 设置已经安装的版本，可以通过/usr/libexec/java_home -V查看
export JAVA_6_HOME=$(/usr/libexec/java_home -v1.6) 
export JAVA_8_HOME=$(/usr/libexec/java_home -v1.8) 
export JAVA_16_HOME=$(/usr/libexec/java_home -v16)
 
# 设置临时切换jdk版本命令
alias jdk6="export JAVA_HOME=$JAVA_6_HOME" 
alias jdk8="export JAVA_HOME=$JAVA_8_HOME" 
alias jdk16="export JAVA_HOME=$JAVA_16_HOME"
 
# 2.最后设置默认版本 finally set JAVA_HOME 
export JAVA_HOME=$(/usr/libexec/java_home -v1.8)
#等价于export JAVA_HOME=$JAVA_8_HOME
 
# 把JAVA_HOME加入到path
export PATH=$JAVA_HOME/bin:$PATH
export CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar