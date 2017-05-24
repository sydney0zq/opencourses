## KCF高速跟踪详解

Henriques, João F., et al. “High-speed tracking with kernelized correlation filters.” Pattern Analysis and Machine Intelligence, IEEE Transactions on 37.3 (2015): 583-596.

<http://blog.csdn.net/shenxiaolu1984/article/details/50905283>

本文的跟踪方法效果甚好，速度奇高，思想和实现均十分简洁。其中利用循环矩阵进行快速计算的方法尤其值得学习。另外，作者在[主页](http://www.robots.ox.ac.uk/~joao/circulant/)上十分慷慨地给出了各种语言的实现代码。 

本文详细推导论文中的一系列步骤，包括论文中未能阐明的部分。请务必先参看这篇简介循环矩阵性质的博客。


## 思想

一般化的跟踪问题可以分解成如下几步： 

1. 在$I\_t$帧中，在当前位置$p\_t$附近采样，训练一个回归器。这个回归器能计算一个小窗口采样的响应。
2. 在$I\_t+1$帧中，在前一帧位置$p\_t$附近采样，用前述回归器判断每个采样的响应。 
3. 响应最强的采样作为本帧位置$p\_{t+1}$。























































