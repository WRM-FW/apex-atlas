# -*- coding: utf-8 -*-
"""ApexAtlas content, batch B: R05-R10."""

TRACKS = {
'montreal': dict(
    round='R05', zh='加拿大大奖赛', en='Canadian Grand Prix',
    circuit_zh='吉尔·维伦纽夫赛道', circuit_en='Circuit Gilles Villeneuve',
    country='加拿大', city='蒙特利尔', flag='🇨🇦', dates='5月22-24日', sprint=True,
    length=4.361, laps=70, left=6, right=8,
    record='1:13.078', record_who='V. Bottas', record_year=2019,
    downforce=('低', 2), throttle=74, braking=('极重', 5), tyre=('中等', 3),
    archetype='stop-and-go', kind='半永久街道赛道（冲刺赛站）',
    intro='蒙特利尔是典型的“冲刺—重刹”赛道：直道、慢弯、再直道，一圈要刹十几次极限刹车。'
          '赛道两侧紧邻水泥护墙和砂石区，路肩高得能把车弹起来。它也是全年刹车盘温度最高的分站之一。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='塞纳发卡与路肩劈砍',
             text='T1-T2 是先右后左的塞纳弯复合发卡；紧接 T3-T4 双向减速弯，车手必须暴力骑上大路肩切线，'
                  '这对悬挂和底盘的抗冲击能力是直接测试。'),
        dict(id='S2', rng=[5, 9], title='圣劳伦斯河岸加速段',
             text='穿过 T5 高速弯后是 T6-T7 与 T8-T9 两组中速减速弯。因为旁边就是水泥护墙，'
                  '刹车点精度要求达到厘米级——多十公分就可能上墙。'),
        dict(id='S3', rng=[10, 14], title='冠军之墙与超级直道',
             text='T10 极窄的大发卡是经典超车区；随后是超过 340 km/h 的 Casino 长直道，'
                  '直道尽头的 T13-T14 终点减速弯紧贴传奇的“冠军之墙”。')],
    corners_analysis=[
        dict(cs='T1-T2', name='塞纳弯复合发卡',
             text='先右后左，入口重刹、出口要给第二弯留角度。第一弯走顺了第二弯才能全油门。'),
        dict(cs='T3-T4', name='骑路肩减速弯',
             text='必须压上路肩才能走直线。路肩高、反弹大，悬挂撑不住的车出弯会跳。'),
        dict(cs='T5', name='高速右弯',
             text='全油门弯，之后接一段加速，是这条赛道少见的流畅点。'),
        dict(cs='T6-T7', name='河岸中速弯',
             text='贴墙的重刹区，刹车点判断比走线更重要。'),
        dict(cs='T8-T9', name='第二组减速弯',
             text='出弯要贴外侧护墙抢角度，容错空间极小。'),
        dict(cs='T10', name='大发卡（超车点）',
             text='全场最窄最慢的弯，也是最好超车的地方，正赛里经常看到三车并排进弯。'),
        dict(cs='T13-T14', name='终点减速弯与冠军之墙',
             text='超长直道之后的极限重刹，直道尾速高意味着这里能追回很多时间，也最容易撞墙。')],
    setup='刹车盘温度常年突破 1000°C，冷却与刹车平衡是第一优先级；同时这里的重刹让 MGU-K 回收效率排在全季前列，'
          '能量收支反而比较宽裕。',
    watch='看 T10 发卡的多车并排，以及 T13 之前谁还在防守线内——直道尾速差在这里最直观。'),

'monaco': dict(
    round='R06', zh='摩纳哥大奖赛', en='Monaco Grand Prix',
    circuit_zh='蒙特卡洛市街赛道', circuit_en='Circuit de Monaco',
    country='摩纳哥', city='蒙特卡洛', flag='🇲🇨', dates='6月05-07日', sprint=False,
    length=3.337, laps=78, left=8, right=11,
    record='1:12.909', record_who='L. Hamilton', record_year=2021,
    downforce=('最大', 5), throttle=35, braking=('重度', 4), tyre=('极低', 1),
    archetype='street-precision', kind='街道赛道',
    intro='摩纳哥是全年最短、最慢、也最不容许犯错的赛道。弯角之间几乎没有直道，超车极难，'
          '所以排位赛成绩基本决定正赛结果。2026 新规下它是唯一禁用直道模式的分站，全圈锁定高下压力姿态。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='圣德沃特与赌场广场',
             text='T1 圣德沃特弯是发车后的第一个右弯，出口角度决定上坡速度；沿博索莱依大街全油门上坡后掠过 T2-T3 大众弯，'
                  '抵达著名的 T4 赌场广场。'),
        dict(id='S2', rng=[5, 12], title='费尔蒙发卡与海滨隧道',
             text='T5 米拉波上弯之后是 T6 费尔蒙发卡——车速只有 45 km/h，全赛历最慢，转向机需要专门扩角；'
                  'T7-T8 钻进海滨隧道，路面颠簸且气流突变；T9-T11 隧道出口的新减速弯重刹，T12 是塔巴克弯。'),
        dict(id='S3', rng=[13, 19], title='泳池区与拉斯卡斯',
             text='T13-T16 泳池双减速弯以超过 200 km/h 贴墙掠过，是摩纳哥最快的一段；'
                  'T17-T18 拉斯卡斯发卡，T19 安东尼·诺盖斯弯接回发车线。')],
    corners_analysis=[
        dict(cs='T1', name='圣德沃特弯',
             text='发车后第一个弯，右弯带坡度，出口要给上坡直道留位置。'),
        dict(cs='T2-T3', name='大众弯',
             text='上坡中的连续变向，视野受限，靠记忆和节奏。'),
        dict(cs='T4', name='赌场广场',
             text='窄右弯，护墙就在车头几米处，是摩纳哥“贴墙艺术”的代表。'),
        dict(cs='T6', name='费尔蒙发卡（45 km/h）',
             text='全赛季最慢的弯，需要最大转向角。这里拉开的差距往往就是整圈差距。'),
        dict(cs='T7-T8', name='海滨隧道',
             text='隧道内阴影和气流变化让车手看不清路面，出口还有起伏，是摩纳哥最“吓人”的一段。'),
        dict(cs='T9-T11', name='隧道出口新减速弯',
             text='重刹加快速变向，刹车在隧道里已经预热，出隧道立刻要用。'),
        dict(cs='T13-T16', name='泳池双减速弯',
             text='超过 200 km/h 的贴墙变向，摩纳哥速度最高、风险也最高的段落。'),
        dict(cs='T17-T18', name='拉斯卡斯发卡',
             text='低速右发卡，出口窄，是少数能尝试内线超越的位置。'),
        dict(cs='T19', name='安东尼·诺盖斯弯',
             text='最后一个弯，出弯要正对接回主直道的那段上坡。')],
    setup='唯一禁用直道模式的分站，全圈锁定弯道模式；空气动力学阻力不再是敌人，机械抓地力、悬挂行程和低速牵引力才是一切。',
    watch='别看超车，看排位赛：摩纳哥 0.1 秒就是两三个名次。正赛里注意进站时机的赌博。'),

'barcelona': dict(
    round='R07', zh='加泰罗尼亚大奖赛', en='Catalan Grand Prix',
    circuit_zh='加泰罗尼亚赛道', circuit_en='Circuit de Barcelona-Catalunya',
    country='西班牙', city='巴塞罗那', flag='🇪🇸', dates='6月12-14日', sprint=False,
    length=4.657, laps=66, left=6, right=8,
    record='1:16.330', record_who='M. Verstappen', record_year=2023,
    downforce=('高', 4), throttle=66, braking=('中等', 3), tyre=('高', 4),
    archetype='high-downforce', kind='专用赛道',
    intro='加泰罗尼亚是 F1 的“基准线”赛道：过去十几年几乎所有测试都在这里跑，因为它的高速弯、中速弯和上坡段分布均衡，'
          '任何一辆车的平衡好坏在这里都藏不住。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='长直道与雷诺大右弯',
             text='长直道冲刺到 T1-T2 艾尔夫减速弯；随后是标志性的长半径全油门上坡大右弯 T3 雷诺弯，'
                  '左前胎在这段持续被横向撕扯。'),
        dict(id='S2', rng=[5, 9], title='下坡发卡与坎普萨盲弯',
             text='T5 雷普索尔是下坡紧凑左弯；T7-T8 上坡连续弯；T9 坎普萨高速弯以接近 240 km/h 贴着路肩盲飞掠过，'
                  '看不见出口是它的难点。'),
        dict(id='S3', rng=[10, 14], title='体育场重刹与经典双右弯',
             text='T10 体育场发卡是主要重刹超车点；恢复旧版高速双右弯布局后的 T13-T14，'
                  '用全速过弯把车弹射进发车大直道。')],
    corners_analysis=[
        dict(cs='T1-T2', name='艾尔夫减速弯',
             text='直道末端先右后左的减速弯，刹车点晚的一方往往能占内线。'),
        dict(cs='T3', name='雷诺上坡大右弯',
             text='长半径、带坡度、几乎全油门。左前胎负荷全年最大之一，是这条赛道的名片。'),
        dict(cs='T5', name='雷普索尔下坡左弯',
             text='下坡入口让刹车距离感觉变短，很容易刹早或锁死。'),
        dict(cs='T7-T8', name='上坡连续弯',
             text='节奏型组合弯，第一弯的出弯线决定第二弯的入口。'),
        dict(cs='T9', name='坎普萨盲弯（240 km/h）',
             text='高速盲弯，靠记忆和勇气，也是这条赛道最出成绩的地方。'),
        dict(cs='T10', name='体育场发卡',
             text='主要超车点，重刹加低速转向，出弯牵引力决定后面一段直道。'),
        dict(cs='T13-T14', name='高速双右弯',
             text='旧版布局的回归：两个相连的高速右弯，用下压力换速度，弹射进发车直道。')],
    setup='综合空气动力学效率的检验场：2026 年更轻更短的底盘在高速弯里的机械支撑好不好，这里看得最清楚。',
    watch='注意 T3 出弯时前轮的指向和 T9 是否敢全油门——这两处最能反映赛车的下压力水平。'),

'red-bull-ring': dict(
    round='R08', zh='奥地利大奖赛', en='Austrian Grand Prix',
    circuit_zh='红牛环赛道', circuit_en='Red Bull Ring, Spielberg',
    country='奥地利', city='施皮尔贝格', flag='🇦🇹', dates='6月26-28日', sprint=False,
    length=4.318, laps=71, left=3, right=7,
    record='1:05.619', record_who='C. Sainz', record_year=2020,
    downforce=('中低', 2), throttle=77, braking=('重度', 4), tyre=('高', 4),
    archetype='stop-and-go', kind='专用赛道（短圈）',
    intro='红牛环只有 10 个弯、单圈约 64 秒，是全年最快节奏的赛道之一。三段长直道配三次重刹，'
          '超车机会多、攻防转换快，也因此成了超车模式博弈最白热化的分站。',
    sectors=[
        dict(id='S1', rng=[1, 1], title='上坡重刹 T1',
             text='整个赛段只有一个弯：起跑上坡后的 T1 尼基·劳达弯。刹车点极晚，出弯宽阔的路肩经常引发白线超限争议。'),
        dict(id='S2', rng=[2, 6], title='阿尔卑斯山坡高落差段',
             text='全速仰冲到现场最高点 T3 雷姆希发卡，是超强超车区；顺势下坡重刹杀入 T4 劳希弯，'
                  '再用 T5-T6 中速左弯收尾。'),
        dict(id='S3', rng=[7, 10], title='极速下坡回旋',
             text='T7-T8 连续高速右弯紧贴砂石区；T9 约亨·林特弯和 T10 最后一弯是全油门下的白线博弈。')],
    corners_analysis=[
        dict(cs='T1', name='尼基·劳达弯',
             text='上坡重刹右弯，全场第一超车点。出弯外侧路肩宽，越线与否常需裁判介入。'),
        dict(cs='T2', name='连接弯',
             text='通往上坡直道的过渡弯，走线要直，为仰冲做准备。'),
        dict(cs='T3', name='雷姆希发卡（全场最高点）',
             text='上坡顶点的慢弯，前车视野受限、后车容易追近，是超车模式最常生效的位置。'),
        dict(cs='T4', name='劳希弯',
             text='下坡入口的重刹左弯，刹车稳定性要求高。'),
        dict(cs='T5-T6', name='中速左弯组',
             text='机械抓地力主导，出弯角度决定进入最后直道的速度。'),
        dict(cs='T7-T8', name='高速右弯组',
             text='紧贴砂石区的高速弯，走线偏一点就要付很大代价。'),
        dict(cs='T9-T10', name='林特弯与收官弯',
             text='全油门极限下的白线博弈，圈速常常在这里被抹掉。')],
    setup='海拔约 700 米的稀薄空气影响涡轮响应；三段长直道让超车模式的攻防极其频繁，能量管理策略比单圈速度更能决定名次。',
    watch='看 T1 和 T3 的两次“晚刹赌博”，以及白线超限是否被记录。'),

'silverstone': dict(
    round='R09', zh='英国大奖赛', en='British Grand Prix',
    circuit_zh='银石赛道', circuit_en='Silverstone Circuit',
    country='英国', city='银石', flag='🇬🇧', dates='7月03-05日', sprint=True,
    length=5.891, laps=52, left=8, right=10,
    record='1:27.097', record_who='M. Verstappen', record_year=2020,
    downforce=('极高', 5), throttle=70, braking=('中等', 2), tyre=('极高', 5),
    archetype='high-downforce', kind='专用赛道（高速）',
    intro='银石是 F1 的发源地，也是全年对下压力和车手体能要求最高的赛道之一。高速弯一连串没有中断，'
          '横向载荷长期维持在 4G 以上，2026 新规下它还是检验主动空气动力学前后翼切换是否顺畅的标杆。',
    sectors=[
        dict(id='S1', rng=[1, 5], title='艾比弯与维拉奇回环',
             text='全速冲过 T1 艾比弯和 T2 农场弯，接着重刹切入 T3-T4 维拉奇与 The Loop 紧凑发卡，'
                  'T5 艾恩顿弯出弯衔接惠灵顿直道。'),
        dict(id='S2', rng=[6, 14], title='马戈茨—贝克茨—查佩尔弯群',
             text='T6-T7 布鲁克兰兹与拉菲尔德之后穿过原发车直道，以接近 290 km/h 杀入 T10-T14 传奇高速连续弯，'
                  '横向 G 值达到 5.2G，随后直奔机库直道。'),
        dict(id='S3', rng=[15, 18], title='斯托弯与俱乐部复合弯',
             text='机库直道尽头是入弯速度超过 250 km/h 的 T15 斯托弯；谷地减速后切进 T16-T18 俱乐部复合弯，'
                  '返回汉密尔顿主直道。')],
    corners_analysis=[
        dict(cs='T1-T2', name='艾比弯与农场弯',
             text='高速右左组合，几乎不减速，靠下压力硬吃。'),
        dict(cs='T3-T4', name='维拉奇与 The Loop',
             text='从极快到极慢的落差弯，重刹加发卡，是这条高速赛道少见的超车机会。'),
        dict(cs='T5', name='艾恩顿弯',
             text='出弯线路决定惠灵顿直道初速。'),
        dict(cs='T6-T7', name='布鲁克兰兹与拉菲尔德',
             text='两个高速弯，命名致敬赛道早期历史，节奏连贯不能断。'),
        dict(cs='T10-T14', name='高速连续弯群（5.2G）',
             text='银石的核心：接近 290 km/h 的连续高速弯，横向载荷 5.2G，车手的颈部和轮胎同时到极限。'),
        dict(cs='T15', name='斯托弯（250 km/h+）',
             text='机库直道末端的重刹高速右弯，入弯速度超过 250 km/h，刹车稳定性要求极高。'),
        dict(cs='T16-T18', name='俱乐部复合弯',
             text='减速、变向、再加速，是回到主直道前的最后一组技术活。')],
    setup='侧向能量负荷全年之首，轮胎横向热衰减来得最快；2026 赛车在这里最需要的是前后翼切换时的姿态平稳过渡。',
    watch='看高速弯群里谁的车身起伏最小，以及正赛里谁先保不住轮胎。'),

'spa': dict(
    round='R10', zh='比利时大奖赛', en='Belgian Grand Prix',
    circuit_zh='斯帕-弗朗科尔尚赛道', circuit_en='Circuit de Spa-Francorchamps',
    country='比利时', city='斯塔沃洛', flag='🇧🇪', dates='7月17-19日', sprint=False,
    length=7.004, laps=44, left=9, right=10,
    record='1:46.286', record_who='V. Bottas', record_year=2018,
    downforce=('中等', 3), throttle=71, braking=('中等', 3), tyre=('高', 4),
    archetype='speed-temple', kind='专用赛道（最长）',
    intro='斯帕是赛历上最长的赛道（7 公里），也是最著名的一条：艾尔罗格-拉迪隆上坡盲弯几乎是 F1 的象征。'
          '它同时拥有超长全油门段和很慢的弯角，天气又常在一圈内变化多次。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='拉源发卡与艾尔罗格神话',
             text='发车后 T1 拉源发卡重刹；接着下坡狂飙直插谷底，以超过 310 km/h 全油门拔地而起冲上'
                  'T2-T4 艾尔罗格-拉迪隆，并在科姆直道达到极速。'),
        dict(id='S2', rng=[5, 15], title='阿登森林流动弯群',
             text='科姆直道尽头是 T5-T7 莱孔布减速弯；T8-T9 布鲁塞尔发卡下坡；随后进入 T10-T11 号称全球最壮丽的高速双左弯'
                  '普汉弯，再经 T12-T15 连续中速弯下坡。'),
        dict(id='S3', rng=[16, 19], title='布兰奇蒙特与巴士站',
             text='T16-T17 以超过 320 km/h 掠过布兰奇蒙特弯；最终在 T18-T19 巴士站减速弯强力重刹，'
                  '回到发车直道。')],
    corners_analysis=[
        dict(cs='T1', name='拉源发卡',
             text='发车后的低速右发卡，重刹区，第一圈常在这里发生接触。'),
        dict(cs='T2-T4', name='艾尔罗格 — 拉迪隆',
             text='先下坡再上坡的盲弯组合，超过 310 km/h 全油门通过，落地感极强。车手说这里是“信任赛车的时刻”。'),
        dict(cs='T5-T7', name='莱孔布减速弯',
             text='科姆直道末端的重刹区，刹车热衰减在这里最明显。'),
        dict(cs='T8-T9', name='布鲁塞尔发卡',
             text='下坡慢弯，出弯角度决定后面一段高速弯的入口。'),
        dict(cs='T10-T11', name='普汉弯',
             text='高速双左弯，带坡度、看不见出口，全年最受推崇的弯角之一。'),
        dict(cs='T12-T15', name='中速连续弯下坡',
             text='节奏段，机械抓地力与下压力都要，出错会一路掉到布兰奇蒙特。'),
        dict(cs='T16-T17', name='布兰奇蒙特（320 km/h）',
             text='长半径高速右弯，历史上多次改造降速，如今仍是全年最快的弯角之一。'),
        dict(cs='T18-T19', name='巴士站减速弯',
             text='终点前的最后重刹，名字来自早年路边真有公交车站，是超车与失误的高发点。')],
    setup='单圈 7 公里，接近 2 公里的科姆冲刺段极易耗尽电能，车队必须精细编排能量释放模型，否则后段明显失速。',
    watch='看车手在艾尔罗格顶点的油门是否完全踩住，以及一圈之内天气是否突然变化。'),
}
