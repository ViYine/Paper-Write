ANESAT-SATELLITEARCHITECTURE 指定模拟的卫星通信系统的类型( 子网要么在空间进行路由/交换，要么在地面进行交换/路由)
List:
• BENTPIPE
• PROCESSPAYLOAD
Default:
PROCESSPAYLOAD

ANESAT-UPLINK-CHANNEL 指定与该接口地址或者节点的信道
Integer
Range: ≥ 0
Default: 0

ANESAT-UPSTREAM-GROUP 指定共享同一上行波束的多个子网的上行波束的id，这只有物理现实义, 如果接口\子网都在一个节点上, 如多波束或多通道卫星。仅当场景具有多个 ANESAT 子网时, 才需要此参数。每个 ANESAT 子网都需要一个唯一的上行波束 ID。
String
Default:
DefaultUpstreamGroup

ANESAT-UPSTREAM-COUNT 指定在仿真中上行波束的数量
Integer
Range: > 0
Default: 1

ANESAT-UPSTREAM-BANDWIDTH 指定特定的上行波束信道的上行带宽  

Real
Range: > 0
Default: 1.0e6
Unit: bps

ANESAT-UPSTREAM-MACLATENCY 指定特定的上行波束信道的介质接入时延
Time
Range: ≥ 0S
Default: 0.04S

ANESAT-DOWNSTREAM-BANDWIDTH 指定特定的下行波束信道的下行带宽
Real
Range: > 0
Default: 70.0e6
Unit: bps

ANESAT-DOWNSTREAM-MACLATENCY 指定特定的下行波束信道的介质接入时延
Time
Range: ≥ 0S
Default: 0.005S

ANESAT-UPSTREAM-TRAFFICCONDITIONING-TYPE 指定上行波束的流量调节器的类型
List:
• RESIDUAL   保留带宽限制，使用这种类型的时候，ANESATUPSTREAM-BANDWIDTH-LIMIT和 ANESAT-UPSTREAMBANDWIDTH-MINIMUM 参数必须指定。
• STRICT  严格带宽限制，带宽是严格的限制在流量的范围内，ANESATUPSTREAM-BANDWIDTH-LIMIT 参数必须配置。
• NONE 在入口的上行接口上没有流量调节。
Default: NONE

ANESAT-UPSTREAMBANDWIDTH-MINIMUM 指定分配给上行波束流量调节器的最小带宽，为保留带宽类型的调节器的参数。
Real
Range: > 0
Default: 64000
Unit: bps

ANESAT-UPSTREAMBANDWIDTH-LIMIT 指定分配给上行波束流量调节器的最大带宽，为保留带宽类型的调节器的参数。
Real
Range: > ANESAT-UPSTREAM-BANDWIDTH-MINIMUM
Default: 512000
Unit: bps

ANESAT-CHANNEL-ID 指定节点的子网信道的名字
String

ANE-EQUATION-DEFINITION 指定方程对象的名字
Optional
Scope: Subnet
Prarmeter：
List:
• ane_default_mac 基础卫星
• anesat_mac 多信道卫星
Default:
ane_default_mac

ANE-SUBNET-ARCHITECTURE 指定子网的top类型
Optional
Scope: Subnet
Parameter：
List:
• ASYMMETRIC 子网的类型是主机到网关的结构，使用这种模式的时候ANE-HEADEND-NODE也要配置
• SYMMETRIC  子网结构式主机到主机
Default: SYMMETRIC

ANE-HEADEND-NODE 指定管理子网传输功能的节点，只是在ASYMMETRIC结构下使用。
Optional
Scope: Subnet

Integer
Range: > 0

ANE-PROCESSOR-NODE  指定分布式内存结构或者集群结构的中心处理器的节点号 是中心处理器的必要参数。
Required
Scope: Subnet

Integer
Range: > 0

ANE-PROCESSOR-NODE-INDEX 指定中心处理器的节点的接口号
Required
Scope: Subnet

Integer
Range: > 0

GESTALT-PREFER-SHAREDMEMORY 仿真使用共享内存优化，减少仿真开销，在集群环境中不适用。
List:
• YES
• NO
Default: YES