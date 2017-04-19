##Convolution Networks

Let's talk about convolutional networks, or convnets. Convnets are neural networks that share their parameters across space.

Imagine you have an image. It can be represented as a flat pancake. It has a width and a height. And because you typically have red, green, and blue channels, it also has a depth. In this instance, depth is 3, that's your input.

Now imagine taking a small patch of this image and running a tiny neural network on it, with say, K outputs. Let's represent those outputs vertically, in a tiny column like this.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-082939.jpg)

Now let's slide that little neural network across the image without changing the weights. Just slide across and vertically like we're painting it with a brush.

On the output, we've drawn another image. It's got a different width, a different height, and more importantly, it's got a different depth. Instead of just R, G and B, now you have an output that's got many color channels, K of them. This operation is called a convolution.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-083152.jpg)

If your patch size were the size of the whole image, it would be no different than a regular layer of a neural network. **But because we have this small patch instead, we have many fewer weights and they are shared across space.**

A convnet is going to basically be a deep network where instead of having stacks of matrix multiply layers, we're going to have stacks of convolutions.

The general idea is that they will form a pyramid. At the bottom you have this big image but very shallow, just R, G, and B.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-083418.jpg)

You're going to apply convolutions that are going to progressively squeeze the spatial dimensions while increasing the depth, which corresponds roughly to the semantic complexity of your representation.

At the top you can put your classifier. You have a representation where all the spatial information has been squeezed out and only parameters that map to contents of the image remain.

So that's the general idea. If you're going to implement this, there are lots of little details to get right and a fair bit of lingo to get used to. You've met the concept of patch and depth. **Patches are sometimes called kernels. Each pancake in your stack is called a feature map.** 

Here, you're mapping three feature maps to K feature maps.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-083815.jpg)

Another term that you need to know is stride. It's the number of pixels that you're shifting each time you move your filter. A stride of 1 makes the output roughly the same size as the input. A stride of 2 means it's about half the size. I say roughly, because it depends a bit about what you do at the edge of your image.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-083917.jpg)


Either, you don't go past the edge, and it's often called valid padding as a shortcut. Or you go off the edge and pad with zeros in such a way that the output map size is exactly the same size as the input map. That is often called same padding as a shortcut.

![](http://okye062gb.bkt.clouddn.com/2017-04-19-084145.jpg)


