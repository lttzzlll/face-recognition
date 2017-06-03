# face-recognition
*** a simple face recognition system based on [facenet](https://github.com/davidsandberg/facenet)
一个基于facenet的人脸识别系统(BS)

### usage
*** 为一个要识别的用户上传若干张图片(理论上越多越好，一般在十张左右)，然后系统会在上传的图片中找到人脸的位置对图片进行剪裁，然后用这些剪裁后的图片作为训练集
为该用户训练一个模型；然后再次上传一张图片，系统可以识别出该张图片中的人脸是不是要识别的用户。
