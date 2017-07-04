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

- Three categories of IPv6 addresses:
    - Unicast（送给某一个特定的 IP)
    - Multicast（送给一群的 IP)
    - Anycast(IPv6 比较特别的地方，送给谁不在意，只要这一群中的一个就可以）
- Notation of IPv6 addresses:
    - Write 128 bits as **eight** 16-bit integers separated by **colons**
    - Examples:
        FEDC:BA98:7654:3210:FEDC:BA98:7654:3210
    A set of consecutive null 16-bit numbers can be replaced by two colons
        1080:0   :   0:   0:   8: 800:200C:417A
        1080:              :   8: 800:200C:417A
    Wrong example:
        1080:   0:   0:   0:   8:   0:   0:417A
        1080:    :             8:   0:   0:417A --> Right
        1080:    :             8:    :     417A --> Wrong
    我们只能把一组连续的 0 变成冒号冒号，因为假如把多组变化的话我们就没办法知道到底是多少个 0。

- Some Addresses formats
    - Provider Addresses
    - Link Local Addresses（一个 link 相当与一个网络, 在电脑刚打开的时候会使用）
    - Site Local Addresses（一个 site 相当与一个 router 把他们都连接起来）
    - Multicast Addresses
    - Anycast Addresses

![](http://okye062gb.bkt.clouddn.com/2017-07-04-122215.jpg)

当一台机器打开的时候, 会用一个Link Local Address去找Router, 然后和Router接触, 然后Router会给它一个正式的IPv6位置。


### Global Unicast Addresses

![](http://okye062gb.bkt.clouddn.com/2017-07-04-122712.jpg)

- `TLA` = Top-Level Aggregator
- `NLA*` = Next-Level Aggregator
- `SLA*` = Site-Level Aggregator
- all subfields variable-length (like CIDR)
- TLAs may be assigned to providers or exchanges


#### Link-Local and Site-Local address

Link-Local addresses for use during auto-configuration and when no routers are supported:

![](http://okye062gb.bkt.clouddn.com/2017-07-04-124030.jpg)

Site-Local addresses for independence from changes of `TLA/NLA*`:

![](http://okye062gb.bkt.clouddn.com/2017-07-04-124132.jpg)


#### Interface IDs

- Lowest-order 64-bit field of unicast addres may be assigned in several different ways:
    - auto-configured from a 64-bit EUI-64, or expanded from a 48-bit MAC address(e.g., Ethernet address)
    - auto-generated pseudo-random number(to address privacy concerns)
    - assigned via DHCP
    - manually configured
    - possibly other methods in the future

#### IPv6 Address Space

![](http://okye062gb.bkt.clouddn.com/2017-07-04-124527.jpg)


## The Revolution of ICMP

```
ICMP Type       Meaning
1               Destination Unreachable
2               Packet Too Big
3               Time Exceeded
4               Parameter Problem
128             Echo Request
129             Echo Reply
------IPv6 only Below------
130             Group Membership Query
131             Group Membership Request
132             Group Membership Termination
133             Router Solicitation(邀请附近的Router)
134             Router Advertisement(Router收到Solicitation之后就会回Advertisement)
135             Neighbor Solicitation
136             Neighbor Advertisement
137             Redirect
```

## IPv6 Routing

- As in IPv4, IPv6 supports IGP and EGP routing protocols:
    - IGP(Interior Gateway Protocol) for within an autonomous system(AS) are
        - RIPng(RFC 2080)
        - OSPFv3(RFC 2740)
        - Integrated IS-ISv6(draft-ietf-isis-ipv6-02.txt)
    - EGP(Edge Gateway Protocol) for peering between autonomous systems(ASs)
        - MP-BGP4(RFC 2858 and RFC 2545)
        - BGP4+
            - Added IPv6 address-family
            - Added IPv6 transport
            - Runs within the same process - only one AS supported
            - All generic BGP functionality works as for IPv4
            - Added functionality to route-maps and prefix-lists
