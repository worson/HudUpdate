>
相信你用过Jcenter和Maven，今天我想告诉你，这里有一个更简单的仓库管理方案-JitPack.io。

参考：
http://www.jianshu.com/p/e443456bb506
http://www.jianshu.com/p/e443456bb506
使用
https://jitpack.io
提交库
https://jitpack.io/docs/ANDROID/

![JitPack1](/assets/JitPackHome2.png)

![JitPack2](/assets/JitPackHome2.png)

![JitPack2](/assets/JitPackHome2.png)

# 使用
JitPack.io的使用和Maven仓库的使用是一致的。比如：
```
compile 'com.github.worson:AndroidLibraryJitPack:V0.1'
```
上面依赖的是我个人在github上的一个库，格式即为：
```
compile 'com.github.username:projectname:tag'

```
其中tag可以是git 打的release名称，也可是JitPack.io根据提交记录生成的标识号等等。
另外在工程根目录下的仓库通过build.gradle指明即可：
```
repositories {
maven { url 'https://jitpack.io' }
}
```

# 搭建仓库
## 主要步骤
- 建立安卓Library
- 配置 Library的gradle文件
- 提交代码到github
