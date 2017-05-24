## 基于相关滤波器的追踪（Correlation Filter-based Tracking）原理

相关论文：An Experimental Survey on Correlation Filter-based Tracking

基于相关滤波器的追踪算法，典型的算法有 KCF，DSST，STC，SAMF 等。这些算法的大致框架都是差不多的。


### 介绍

在视频的第一帧给定目标的初始位置，追踪的目标就是预测目标之后的位置。追踪受到很多因素影响，比如光照变化（illumination variations），遮挡，形变，旋转等。在过去对于追踪的研究之中，主要分两种方法：**生成型模型（generative model）和判别式模型（discriminative models）。前者的主要思想就是通过寻找最佳匹配的窗口，而后者的主要思想就是学习从背景中区分目标。**

在判别式模型中，基于相关滤波器的追踪算法（Correlation Filter-based Tracking）表现比较好。一般的，相关滤波器的原理就是在场景中，对每个感兴趣的目标产生高响应（相关峰（correlation peak）），对于背景则产生低的响应。


Correlationfilter-based tracking（CFTs）主要可以通过以下几个方面提高：

- 1）引入更好的训练方案（introducing better training schemes）
- 2）提取更强大的特征（extracting powerful features）
- 3）减轻尺度变化的影响（relieving scaling issue）
- 4）结合基于部分的追踪策略（applying part-based tracking strategy），即相对于对目标整体识别，可以将目标分成好几个部分，对各个部分进行识别
5）结合 long-term 的追踪（cooperating with long-term tracking）


### CFT 整体框架介绍

**对于输入的第一帧，将给定的要追踪的区域提取出特征，然后进行训练，得到相关滤波器。**

对于之后的每一帧，先裁剪下之前预测的区域（由于是对前一帧区域做相关，所以对于物体快速移动处理的不好），然后进行特征提取，这些特征经过 cos 窗函数之后，做 FFT 变换，然后与相关滤波器相乘，将结果做 IFFT 之后，最大响应点所在的区域即为要追踪目标的新位置，然后再用新位置区域训练更新得到新的相关滤波器，用于之后的预测。

![](http://okye062gb.bkt.clouddn.com/2017-05-24-032829.jpg)

用数学的方式描述工作流程如下：

- $x$: 检测器的输入。要么是 raw image patch，要么是提取的特征；
- $h$: 相关滤波器。

根据卷积理论，时域上的卷积相当于频域上的乘积，可以得到如下式子：

![](http://okye062gb.bkt.clouddn.com/2017-05-24-032927.jpg)

符号`^`表示傅里叶变换，`⊙`表示 element-wise 相乘，`*`表示复共轭，$F^{-1}$ 表示反傅里叶变换。(1) 的结果就是 x 与 h 的相关输出，也就是之前提到的 confidence map，根据最大的响应位置，可以得到目标新预测的位置。

对于训练滤波器，我们首先定义一个期望的相关输出 y（可以是任意形状，比如 MOSSE 算法就是将 y 定义为 2D 峰值在中心的高斯分布的函数，UMACE 算法就是目标中心点为 1，其余位置为 0 的 Kronecker delta 函数）。使用目标的新实例 x’，相关滤波器 h 应该满足：

![](http://okye062gb.bkt.clouddn.com/2017-05-24-033449.jpg)

因此：

![](http://img.blog.csdn.net/20160810181845298)

其中，(2) 表示 y 的 DFT，除法的计算也是 element-wise 的。

对于一幅 $n\times n$ 大小的图片进行循环卷积的计算复杂度是 O(n^4), 而使用 FFT 之后，计算复杂度变为 O(n^2 log(n)), 因此使用 FFT 的加速作用很明显。


















































