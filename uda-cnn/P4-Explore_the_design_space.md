##Explore The Design Space

Now that you've seen what a simple convnet looks like, there are many things that we can do to improve it.

We're going to talk about three of them, pooling, one by one convolutions and something a bit more advanced called the inception architecture.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-085618.jpg)


<hr>

####Max Pooling

The first improvement is a better way to reduce the spatial extent of your feature maps in the convolutional pyramid.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-085740.jpg)

Until now, we've used striding to shift the filters by a few pixel each time and reduce the future map size. This is a very aggressive way to downsample an image. It removes a lot of information. **What if instead of skipping one in every two convolutions, we still ran with a very small stride, say for example one. But then took all the convolutions in a neighborhood and combined them somehow.** That operation is called pooling, and there are a few ways to go about it. The most common is max pooling. At every point in the future map, look at a small neighborhood around that point and compute the maximum of all the responses around it. 

![](http://okye062gb.bkt.clouddn.com/2017-04-19-090028.jpg)

There are some advantages to using max pooling. First, it doesn't add to your number of parameters. So you don't risk an increasing over fitting. Second, it simply often yields more accurate models.

However, since the convolutions that run below run at a lower stride, the model then becomes a lot more expensive to compute. **And now you have even more hyper parameters to worry about. The pooling region size, and the pooling stride, and they don't have to be the same.**

A very typical architecture for a covenant is a few layers alternating convolutions and max pooling, followed by a few fully connected layers at the top.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-090225.jpg)

The first famous model to use this architecture was LENET-5 designed by Yann Lecun to the character recognition back in 1998. Modern convolutional networks such as ALEXNET, which famously won the competitive ImageNet object recognition challenge in 2012, used a very similar architecture with a few wrinkles.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-090419.jpg)

Another notable form of pooling is average pooling. Instead of taking the max, just take an average over the window of pixels around a specific location. It's a little bit like providing a **blurred low resolution view** of the feature map below.


####1x1 Convolution

![](http://okye062gb.bkt.clouddn.com/2017-04-19-090657.jpg)

You might wonder, why might one ever want to use one by one convolutions? They're not really looking at a patch of the image, just that one pixel. Look at the classic convolution setting. It's basically a small classifier for a patch of the image, but it's only a linear classifier.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-090909.jpg)

Interspersing your convolutions with one by one convolutions is a very inexpensive way to make your models deeper and have more parameters without completely changing their structure.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-091104.jpg)

They're also very cheap, because if you go through the math, they're not really convolutions at all. They're really just matrix multiplies, and they have relatively few parameters.


I mention all of this, average pooling and one by one convolutions because I want to talk about a general strategy that has been very successful at creating covnets that are both smaller and better than covnets that simply use a pyramid of convolutions.
















