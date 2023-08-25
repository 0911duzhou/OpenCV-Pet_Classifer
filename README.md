# 基于TensorFlow2实现的宠物识别系统（爬虫、模型训练和调优、模型部署）

完整资源下载地址：https://drive.google.com/file/d/1YEoaa7fludUzr_JzV7VsLJDp3Og09eJV/view?usp=drive_link
​


这是一个从零开始构建的深度学习小项目，提供猫、狗、鼠、兔四种宠物的识别服务。

共包含如下几部分：

- 爬虫
  - 从网络上下载宠物图片，构建训练用的数据集
  - gevent + requests + beautifulsoup4
- 深度学习模型
  - 鉴于我们的数据比较少，这部分需要做迁移学习
  - TensorFlow 2.0 + DenseNet121
- 部署
  - 使用Gradio提供宠物图片识别服务
 
如何训练自己的模型？

- 切换到项目根目录下;
- 通过`python3 spider.py`启动爬虫程序;
- 人工筛选，删除不正确的图片;
- 修改`settings.py`里的相关参数;
- 通过`python3 train.py`启动训练脚本。
