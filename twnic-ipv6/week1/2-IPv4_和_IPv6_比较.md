# IPv4 and IPv6 封包的比较

- Three major simplifications
    - Assign a fixed format to all headers(40 bytes)
    - Remove the header checksum(IPv6 是否需要 TCP 协议）
    - Remove the hop-by-hop segmentation procedure（切割封包的动作是不做的，这个动作是源主机完成的）


## From Options to **Extension** Headers

- Hop-by-Hop options header
- Routing header（要不要 source routing)
- Fragment header
- Authentication header
- Encrypted security payload
- Destination options header

![](http://okye062gb.bkt.clouddn.com/2017-07-01-064459.jpg)

### Routing Header

![](http://okye062gb.bkt.clouddn.com/2017-07-01-064740.jpg)

图中的 strict 模式是说我们必须按照封包所写的 IP 地址一个个的前进，但是 loose 就是只要经过就可以。

### Fragment Header

![](http://okye062gb.bkt.clouddn.com/2017-07-01-065036.jpg)

Identifier 和 Offset 将一个个封包组合起来。


## IPv6 Addressing





























