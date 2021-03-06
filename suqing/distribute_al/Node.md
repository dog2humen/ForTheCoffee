# 分布式相关算法

## 一.分布式协调与同步
### 1.互斥(Distributed Mutual Exclusion):
在分布式系统中, 多个节点共享临界资源(如全局配置文件)或者同时执行某个函数等, 就产生互斥问题.
一般来说, 分布式互斥算法要实现以下目标特性:
- 安全性: 即任何时刻只能有一个进程访问共享资源, 即持有互斥锁.
- 公平性: 有些场景需要尽量保证访问共享资源的公平性，这表明：系统不能出现死锁，任何进程持有锁的时间是有限的，任何等待的进程最终都能获取锁，以及等待获取锁的进程的等待时间是有限的.
- 低带宽: 尽量减少消息传输量.
- 低延迟: 尽量减少进程进入临界区之前的等待的时间.
- 动态性: 允许进程在任何时刻加入到访问共享资源的进程集合中，或者从其中退出.
- 容忍进程失败: 允许访问共享资源的进程集合中的进程因失败而退出，而保证整个系统不受影响
- 容忍消息丢失: 在消息不能按时到达、乱序甚至丢失的情况下，整个系统依然正常工作

#### 集中式算法(centralized algorithm):
- 主要思想: 引入一个协调者(coordinator)负责处理临界资源的请求. 每个程序(进程, 线程)需要访问临界资源前, 先给coordinator发送请求, 若当前临界资源没有被任何程序使用, 直接授权程序访问.否则, 针对请求顺序放入一个队列中等待.若持有临界资源的程序使用完, 则通知coordinator, coordinator从等待队列中取出一个请求, 并给它发送授权消息使其可以直接使用临界资源.
- 优点: 简单,易于实现
- 缺点: 依赖coordinator, 可用性低, 性能容易受coordinator影响
- 典型应用: 利用分布式锁去实现一个client-server


#### 分布式算法(distributed algorithm):

##### 1.使用组播和逻辑时钟(Ricart Agrawala) 
- 主要思想: Ricart & Agrawala算法是在1981年被提出的一个基于请求的分布式互斥算法. 当一个程序要访问临界资源时, 先向系统中的其他程序发送一条请求消息, 在接受到所有程序返回的同意消息后, 才可以访问临界资源.其中,请求消息必须需要包含时钟信息(时间戳), 请求id, 请求资源等.
- 算法流程:
    - 进程A在准备进入临界区时, 必须发送一条带时间戳的消息给其他进程.
    - 进程A收到其他所有进程的同意消息后, 可以进入临界区
    - 若存在进程B在收到进程A的请求之前, 发出了一个更早的请求(更小的时间戳), 进程B中维护一个延迟队列, 将进程A的请求消息加入队列中, 等进程B使用完临界区后, 从队列中取出发消息给进程A

- 优点: 可用性较高
- 缺点: 
    - 1. 向其他n-1个程序发送访问临界资源请求, 需要n-1次交互. 
    - 2. 需要接受其他n-1个程序的同意消息才可访问资源, n-1次交互
    - 3. 总共需要2(n - 1), 大型系统中大大增加消息量, 产生高昂的交互成本
    - 4. 一旦某个程序故障, 无法发送同意消息, 会造成其他程序均处于等待状态, 导致系统不可用
- 典型应用: 系统规模较小, 临界资源使用频度低的场景. 比如p2p的系统, hdfs的文件修改

##### 2.令牌环算法(Token Ring):
- 主要思想: 所有程序(进程)在逻辑上构成一个环形结构, 将token在环上按照一定的顺序传递, 拿到token的程序可以访问临界资源, 如果拿到token的程序不需要访问临界资源, 则直接传递给下一个程序.
- 优点: 
    - 公平性好, 在一个周期内每个程序都能访问到临界资源
    - 通信效率较好, 不需要通知其他所有程序.
- 缺点: 当参与者多, 并且对临界资源使用频度低时, 会产生较多的无效通信
- 典型应用: 无人机通信


### 2.选举

#### Bully算法
- 主要思想: 选取ID最大的节点为主节点.
    - Bully算法中, 节点角色有两种, **普通节点和主节点**.初始化时所有节点都是普通节点, 都可成为主节点.当选主成功后, **有且只有一个**为主节点, 其他都是普通节点.只有当主节点与其他节点失去心跳后, 才重洗选主.
    - 选举过程包含3种消息:
        - Election消息, 用于发起选举.
        - Alive, 用于应答Election
        - Victory, 竞选成功的主向其他节点发送的消息
    - 选举过程:
        - 1. 集群中每个节点判断自己的ID是否为当前活着的节点中ID最大的, 如果是, 直接向其他节点发送Victory
        - 2. 如果不是ID最大的, 则向比自己ID大的发Election消息, 等待回复.
        - 3. 在给定时间内, 本节点未收到Alive, 则认为自己选主成功, 向其他节点发送Victory.
        - 4. 若本节点收到比自己ID小的节点发的Election消息, 则回复Alive, 重新选举.

- 优点: 谁ID最大谁是老大, 简单, 算法复杂度低, 选举速度快.
- 缺点: 每个节点需要包含其他节点的信息, 存储额外信息多; 任意一个比当前主节点ID大的节点加入集群会触发重洗选主, 如果该节点频繁退出加入集群, 会导致频繁选举.
- 典型应用: MongoDB的副本集故障转移采用Bully. MongoDB采用节点的最后操作时间戳作为ID, 时间戳最新的节点ID最大, 成为主节点.

#### Raft算法
- 主要思想: 少数服从多数
    - Raft算法包含三种角色:
        - **Leader**: 主节点, 同一时刻只有一个Leader.
        - **Candidate**: 候选节点, 每个节点都可以成为Candidate, 只有Candidate才有权被选为Leader
        - **Follwer**: Leader跟班, 不可以发起选举
    - 选举过程:
        - 1. 初始化, 所有节点置为Follwer.
        - 2. 开始选主时, 所有节点由Follwer -> Candidate, **并向其他节点发送选主请求**.
        - 3. 其他节点根据接收到的选主请求的先后顺序, 回复是否同意.**每个节点只可投一张票**.
        - 4. 若发起选主的节点获得超过一半的投票, 则成为主节点 , 状态变为Leader, 其他节点从Candidate变为Follwer. Leader与Follwer会发送心跳, 以检测Leader是否活着.
        - 5. Leader任期时间到了, Leader变为Follwer, 进入新一轮选主.
- 优点: 选举速度快, 复杂度低, 易于实现. 算法稳定性比Bully好, 因为当有新节点加入后或者Leader节点故障后, 会触发选主, 但不一定真正切主.
- 缺点: 要求每个节点能互相通信, 通信量大.
- 典型应用: 开源服务发现组件etcds采用了Raft算法来实现选主和一致性.

#### ZAB(ZooKeeper Atomic Broadcast)算法
- 主要思想: 利用ID实现权重优先级, 优先级高者为主.ZAB算法增加节点ID和数据ID, 节点ID和数据ID越大表示数据越新, 优先成为主.相当于Raft的改进
    - ZAB算法包含三种角色:
        - Leader 主节点.
        - Follwer 跟随者.
        - Observer 观察者, 无投票权
    - 选举过程中有4个状态:
        - Looking: 选举状态, 处于该状态, 会认为当前集群中没有Leader, 自己进入选举状态.
        - Leading: 表示当前节点为Leader节点.
        - Following: 集群选主后, 其他节点状态更新为Following.
        - Observing: 观察者状态, 没投票权和选举权.
    - 选举过程:
        - 每个节点维护一个三元组(server_ID, server_zxID, epoch), server_ID表示当前节点id, server_zxID表示点前节点的数据id, epoch表示当前选举轮数. 选主原则是server_zxID最大的为Leader, server_zxID一样的, server_ID大的为Leader. 投票过程采取每个节点广播投票消息给其他节点, 消息为(vote_id, vote_zxID)的二元组.vote_id为投票给哪个server_ID, vote_zxID为数据id
        - 假设集群有三个节点, 每个节点的server_zxID都为0. 初始化, epoch = 1, 每个节点都给自己投票, 并将投票信息广播给其他节点, (vote_id, vote_zxID).
        - 根据规则, 由于三个节点的epoch, server_zxID都一样, 因此server_ID大的应被选举为主, 更新投票信息, server1, server2将vote_id 改为3, 重新广播.
        - 此时系统内全部节点都选了server3,  因此server3变为Leader, 状态改为Leading. Leader向其他节点发心跳. server1, server2 变为Following状态.
- 优点: zab算法性能高, 对系统无特殊要求.选举稳定性比较好, 新节点加入集群或者节点故障恢复后触发选主, 但不一定真正切主(除非新节点或者故障恢复的节点的id和zxID都最大, 且获得投票过半)
- 缺点: 广播通信量大, n个节点, 广播一遍就是n\*(n - 1), 容易导致广播风暴. 每个节点都需要维护其他节点的id和数据id信息, 选举时间较长.

### 3.共识
- 综述: 分布式选举和分布式共识都可以来解决一致性问题, 在**分布式记账(区块链, 比特币...)**这个应用领域, 如果用之前选举的相关算法, 选主节点去记账, 容易出现造假和性能瓶颈的问题. 使用**分布式共识**的相关算法可以解决.**分布式共识就是在多个节点均可独自操作或记录的情况下，使得所有节点针对某个状态达成一致的过程**
- 关于区块链这种数据结构: 区块链是由包含交易信息的区块从后向前有序链接起来的数据结构，其中区块是指很多交易数据的集合，每个区块包括区块头和区块体，区块头包括前一区块的哈希值、本区块的哈希值和时间戳；区块体用来存储交易数据。 
- 分布式记账问题中, 针对同一笔交易, 有且仅有一个节点可以获得记账权, 然后其他节点同意该节点的记账结果, 从而达成一致. **分布式共识的关键点就是: 获得记账权和所有节点达成一致**

#### PoW(Proof-of-Work, 工作量证明)算法
- 主要思想: 根据每个节点的计算能力来竞争记账权, 谁的算力强, 谁获得记账权的可能性大. 这是一种**使用工作量证明机制的共识算法**. 如何体现算力-做题.
    - 获取记账权的题目算法: 利用区块的index, 前一个区块的hash值, 交易的时间戳, 区块数据和一个nonce值, 通过SHA256哈希算法计算一个hash值, 判断该值的前k个是否为0, 如果不是, nonce递增, 重新计算. nonce是常量用来找到满足条件的hash值, k为hash值前导0的个数, 用来描述计算难度.
    - 如何达成共识: 获得记账权的节点将该区块信息广播给其他节点, 其他节点判断**该节点中的所有交易都是有效的且之前从未存在, 则认为该区块有效, 并接受该区块, 达成一致.**
    - 算法流程: 假设有a, b, c, d, e五个节点, 假设a产生一个交易, 则记账流程如下:
        - a产生新的交易, 向全网其他节点进行广播, 要求对交易进行记账.
        - 每个记账节点接收到请求后, 将收到的交易信息放入一个区块中.
        - 每个节点执行Pow算法, 计算本节点区块的hash值, 尝试找到一个工作量证明.
        - 若节点b找到了一个工作量证明, 并全网广播.
        - 其他节点接收到广播信息后, 若该区块有效, 接受该区块, 并跟随在该区块的末尾, 制造新区块延长该链条, 将被接受的区块的随机哈希值视为新区块的随机哈希值.
- 特点: 去中心化
- 劣势: 计算量大, 效率低, 消耗资源, 共识周期达成时间长.

#### PoS(Proof-of-Stake, 权益证明)
    

#### DPoS(Delegated Proof of Stake，委托权益证明)
