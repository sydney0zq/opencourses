# IPv6 简介

## IPv6 设计理念

- The Internet could have been so successful in the past years if IPv4 had contained any major flaw.
- IPv4 was a very good design, and IPv6 should indeed keep most of this characteristics.
- **Simply increase the size of addresses** and to keep everything else unchanged? No
- However, 20 years of experience brought lessons, IPv6 is not a simple derivation of IPv4, but a definitive improvement.


## IPv6 Header Format

![](http://okye062gb.bkt.clouddn.com/2017-07-01-022010.jpg)

对比 IPv4 的 Header:

![](http://okye062gb.bkt.clouddn.com/2017-07-01-022135.jpg)

不固定长度，分包切割需要涉及`Identification`, `Fragment Offset`。路由选择的话设计`Options + Padding`。由于IPv4的复杂性, 导致路由器处理封包的时候带来一定的复杂性。


**A Comparsion of Two Headers**

- **Six fields** were suppressed:
    - Header Length, Type of Service, Identification, Flags, Fragment Offset, Header Checksum.
- **Three fields** were renamed:
    - Length, Protocol Type, Time to Live
- The **option mechanism** was entirely revised:
    - Source Routing
    - Route Recording
- Two new fields were added:
    - **Priority** and **Flow Label**(for real-time traffic).
- Three major simplifications:
    - Assign a fixed format to all headers(40 bytes)
    - Remove the header checksum
    - Remove the hop-by-hop segmentation procedure


## Transition(过度) Approaches

- Dual Stack
    - System completely supports IPv6
- Tunneling
    - IPv6 packets are encapsulated for transmission over existing IPv4 infrastruture
- Translation
    - IPv6 packets are translated into IPv4 packets and vice versa(最重要的是IP信息要转换过去)
    - Header information is preserved as much as possible


### Dual Stack Mechasnisms

- **Simple dual stack(RFC 1933)**
    - Both IPv4 and IPv6 are directly supported

![](http://okye062gb.bkt.clouddn.com/2017-07-01-030842.jpg)


- **Dual Stack Transition Mechanism(DSTM)**
    - Assures communication between IPv4 applications in IPv6 only networks and the rest of the Internet
    - Temporary IPv4 addresses are assigned when communicating with an IPv4-only host
    - Cooperation between DNS and DHCPv6
    - Dynamic Tunnel Interface encapsulates the IPv4 packets

![](http://okye062gb.bkt.clouddn.com/2017-07-01-034830.jpg)


#### DSTM: principle

- Assumes IPv4/IPv6 dual stack on host
- IPv4 stack is configured only when one or more applications need it
    - A **temporal IPv4 address** is given to the host
- All IPv4 traffic coming from the host is tunneled towards the **DSTM gateway**(IPv4 over IPv6)
    - DSTM gateway encapsulates/decapsulates packets
    - Maintains an IPv6 <-> IPv4 mapping table

**How DSTM works(v6->v4)**

![](http://okye062gb.bkt.clouddn.com/2017-07-01-040026.jpg)

![](http://okye062gb.bkt.clouddn.com/2017-07-01-040419.jpg)

```
1) In A, the v4 address of C is used by the application, which sends v4 packet to the kernel;
2) The interface asks DSTM Server for a v4 source address;
3) DSTM server returns: 
    - A temporal IPv4 address for A
    - IPv6 address of DSTM gateway
4) A creates the IPv4 packet ($A_4$ -> $C_4$)
5) A tunnels the V4 packet to B using IPv6 ($A_6$ -> $B_6$)
6) B decapsulates the V4 packet and send it to $C_4$
7) B keeps the mapping between $A_4$ <-> $A_6$ in the routing table
```

















