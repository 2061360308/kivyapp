[app]

# (str) 应用程序的名称
title = My Application

# (str) 应用程序的包名
package.name = myapp

# (str) 应用程序的包目录
package.domain = org.test

# (str) 应用程序的源代码入口点
source.dir = .

# (str) 源代码的主要Python文件
source.main = main.py

# (list) 包含的Python包（手动添加其他需要的包）
requirements = python3,kivy

# (str) 应用程序的图标
icon.filename = %(source.dir)s/data/icon.png

# (str) 应用程序的版本
version = 0.1

# (list) 应用程序需要的权限
android.permissions = INTERNET

# (bool) 是否使用--private参数在apk中包含你的Python安装？如果是False，那么你的apk将尝试连接到一个在设备上已经安装的Python，这通常是不可能的。
android.private_storage = True

# (str) Android的API版本
android.api = 27

# (str) Android的最小API版本
android.minapi = 21

# (str) Android的目标API版本
android.targetapi = 27

# (str) Android SDK版本
android.sdk = 24

# (str) Android NDK版本
android.ndk = 19b