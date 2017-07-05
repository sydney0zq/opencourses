## Plug-and-Play -- Auto-configuration

- **Auto-configuration** means that a computer will automatically discover and register the parameters that it needs to use in order to connect to the Internet.
- One should be able to change IPv6 addresses dynamically as one changes ISP **providers**.
- Addresses would be assigned to interfaces for a **limited lifetime**.
- Two modes for address configuration
    - Stateless mode
    - Stateful mode(using DHCPv6)

### Link State Addresses

- When an interface is initialized, the host can build up a **link local address** for this interface by concatenating the well-known **link local prefix** and a unique token(48-bit Ethernet address).
- A typical link local address:
    FE80:0:0:0:0:0:XXXX:XXXX:XXXX
- Link local address can only be used on the local link.

### Stateless Autoconfiguration

- IPv6 nodes join the **all nodes** multicast(这个网络上所有的node它都可以搜到) group by programming their interfaces to receive all the packets for the address = **FF02::1**.
- Send a solicitation(找router) message to the routers on the link, using the **all routers** address, **FF02::2**
- Routers reply with a **router advertisement**
- Does not require any servers


## Plug-and-Play -- Address Resolution

- The **neighbor discovery procedure** offers the functions of ARP(IP-MAc) and router discovery
- Defined as part of IPv6 ICMP
- Host maintains four separate caches:
    - The destination's cache(到底经过谁出去的)
    - The neighbor's cache(neighbor的MAC, 谁和你连在一起)
    - The prefix list(这些位置是从哪些router来的)
    - The router list(哪些router和我连)

### Destination's cache

- The destination's cache has an entry for each destination address toward which the host **recnet sent packets**
- It associates the **IPv6 address** of the destination with that of the neighbor toward the packets were sent

![](http://okye062gb.bkt.clouddn.com/2017-07-04-143225.jpg)

### Neighbor's Cache(IP/MAC)

- The neighbor's cache has an entry for the immediately **adjacent neighbor** to which packets were recently relayed.
- It associated the **IPv6 address** of that neighbor with the corresponding **MAC address(48 bits)**

![](http://okye062gb.bkt.clouddn.com/2017-07-04-143510.jpg)

### Prefix List and Router List

- The **prefix list** includes the prefixes that have been recently **learned from router advertisements**
- The **router list** includes the IPv6 addresses of all routers from which advertisements have recently been received


## Basic Algoritm to Transmit a Packet

- To transmit a packet, the host must first find out the **next hop** for the destination. The next hop should be **a neighbor** directly connected to the same link as the host
- In most case, the neighbor address will be found in the **destination's cache**
- If not, the host will check whether one of the **cached prefixes** matches the destination address
- If yes, the destination is **local**, the next hop is the destination itself
    -双方都在同一个子网内, 可直接传送给对方

## Basic Algorithm

- Otherwise, the destination is probably **remote**
- A **router** should be selected from the router list as the next hop
    双方不在同一个网络, 需要通过Router传送给对方
- The corresponding entry for the next hop is added to the **destination's cache(更新)**, and the **neighbor's cache** is looked up to find the MAC address of that neighbor



