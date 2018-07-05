# 图像中文描述

用一句话描述给定图像中的主要信息，中文语境下的图像理解问题。尝试自然语言处理与计算机视觉的结合。

## 依赖
- [NumPy](http://docs.scipy.org/doc/numpy-1.10.1/user/install.html)
- [Tensorflow](https://www.tensorflow.org/versions/r0.8/get_started/os_setup.html)
- [Keras](https://keras.io/#installation)
- [OpenCV](https://opencv-python-tutroals.readthedocs.io/en/latest/)

## 数据集

使用 AI Challenger 2017 的图像中文描述数据集，包含30万张图片，150万句中文描述。训练集：210,000 张，验证集：30,000 张，测试集 A：30,000 张，测试集 B：30,000 张。


 ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/dataset.png)

下载点这里：[图像中文描述数据集](https://challenger.ai/datasets/caption)，放在 data 目录下。


## ImageNet 预训练模型

下载点这里： [ResNet-152](https://drive.google.com/file/d/0Byy2AcGyEVxfeXExMzNNOHpEODg/view?usp=sharing)， 放在 models 目录下。

## 用法

### 数据预处理
提取210,000 张训练图片和30,000 张验证图片：
```bash
$ python pre-process.py
```

### 训练
```bash
$ python train.py
```

可视化训练过程，执行：
```bash
$ tensorboard --logdir path_to_current_dir/logs
```

### 演示
下载 [预训练模型](https://github.com/foamliu/Image-Captioning/releases/download/v1.0/model.85-0.7657.hdf5) 放在 models 目录，然后执行:

```bash
$ python demo.py
```

1 | 2 | 3 | 4 |
|---|---|---|---|
|![image](https://github.com/foamliu/Image-Captioning/raw/master/images/0_out.png)  | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/1_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/2_out.png)| ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/3_out.png) |
|![image](https://github.com/foamliu/Image-Captioning/raw/master/images/4_out.png)  | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/5_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/6_out.png)| ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/7_out.png) |
|![image](https://github.com/foamliu/Image-Captioning/raw/master/images/8_out.png)  | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/9_out.png) |![image](https://github.com/foamliu/Image-Captioning/raw/master/images/10_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/11_out.png)|
|![image](https://github.com/foamliu/Image-Captioning/raw/master/images/12_out.png)  | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/13_out.png) |![image](https://github.com/foamliu/Image-Captioning/raw/master/images/14_out.png)| ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/15_out.png)|
|![image](https://github.com/foamliu/Image-Captioning/raw/master/images/16_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/17_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/18_out.png) | ![image](https://github.com/foamliu/Image-Captioning/raw/master/images/19_out.png) |
