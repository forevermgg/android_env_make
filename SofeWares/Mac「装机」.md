# 下载 Homebrew
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
## 利用Homebrew管理程序包
```
brew install package-name
```
## 软件管理利器：Homebrew-Cask
```
brew tap caskroom/cask
brew cask install software-name
brew cask search chrome
```
## homebrew-cask-upgrade
```
brew tap buo/cask-upgrade
brew cu -a
```
# 下载第三方应用
```
brew cask install google-chrome
brew cask install iina
```
# 下载 MAS
+ mas 作为终端上的 Mac App Store，其劣势是无法随意浏览众多应用、没有编辑推荐、没有排行榜… 但也因为不用加载这么多东西，甚至不用加载图片，它才有着惊人的速度。 
+ Mac App Store 中每一个应用都有自己的应用识别码（Product Identifier），这可以在每个应用的链接中看到。mas 就是根据 Product Identifier 安装与更新应用，也提供了查询应用 ID 的命令。
+ 由 1Password 的链接可知其识别码为 443987910 
https://itunes.apple.com/cn/app/1password/id443987910?mt=12
```
brew install mas
```
除了查看链接，有以下 x 种方法获取应用的识别码：
+ 用命令 mas search 关键词 查询应用。比如在终端中执行 mas search xcode，大概 1 秒就显示了结果；
+ 用命令 mas list 查询已安装应用及其识别码。
+ https://sspai.com/post/40382
# 下载 Mac App Store 应用
```
mas install 441258766 # magnet
mas install 425424353 # the unarchiver
mas install 836500024 # wechat
mas install 863486266 # sketchbook
mas install 595191960 # copyclip
mas install 880001334 # reeder
mas install 1254743014 # lyricsx
mas install 937984704 # amphetamine
mas install 1081413713 # gif brewery 3
```
# 重置启动台图标顺序
```
defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock
```

# 注：
+ 对于使用 MAS 安装应用需要 app ID，可以使用 mas list 来快速获取现安装的所有应用的 app ID。
+ 把上面的代码保存为 (s.command)[https://www.jianshu.com/p/5c99ce6daea2]，然后给予执行权限，以后只要双击即可使用，参考：mac 的 command 文件