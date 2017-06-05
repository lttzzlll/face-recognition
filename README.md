# face-recognition
> a simple face recognition system based on [facenet](https://github.com/davidsandberg/facenet)
一个基于facenet的人脸识别系统(BS)

## usage
> 为一个要识别的用户上传若干张图片(理论上越多越好，一般在十张左右)，然后系统会在上传的图片中找到人脸的位置对图片进行剪裁，然后用这些剪裁后的图片作为训练集
为该用户训练一个模型；然后再次上传一张图片，系统可以识别出该张图片中的人脸是不是要识别的用户。


## install
> ### prepare
> 首先安装python环境.
> linux or macos自带python环境, windows需要另外安装[url](https://www.python.org/downloads/windows/).
> 如果是linux or macos 推荐使用默认的pyhton2.7.x版本,对应的tensorflow版本也是python2.7.x版本,如果是windows环境,只能选择安装python3.5.x版本,
> 因为tensorflow对windows只支持python3.5.x版本.

> ### clone this reposity
> linux & macos自带git 所以只需打开shell, 执行 git clone https://github.com/lttzzlll/face-recognition.git
> windows没有git, 可以选择首先安装git, 然后在 cmd 命令界面或者是powershell界面 执行 git clone https://github.com/lttzzlll/face-recognition.git
> 或者是转到该[url](https://github.com/lttzzlll/face-recognition.git), 在界面上的 clone or download, 选择download
> git下载安装[url](https://git-for-windows.github.io/), 下载之后点击安装，一路按确认. 安装完成后在cmd界面或者是powershell界面输入 git查看是否安装成功

> * install for linux(ubantu)
> 
> * install for macos
> * install for windows
> * install with docker
> 跨越所有这些平台的方法目前就是使用docker虚拟化环境,前提是所使用的平台已经安装好了docker,剩下的就是给出一个镜像.
> docker对linux最友好,macos和windows次之,可能需要安装virtualbox虚拟机来为要运行的程序专门虚拟化一个环境.
