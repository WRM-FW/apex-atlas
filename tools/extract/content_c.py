# -*- coding: utf-8 -*-
"""ApexAtlas content, batch C: R11-R15, R17."""

TRACKS = {
'hungaroring': dict(
    round='R11', zh='匈牙利大奖赛', en='Hungarian Grand Prix',
    circuit_zh='亨格罗宁赛道', circuit_en='Hungaroring',
    country='匈牙利', city='布达佩斯', flag='🇭🇺', dates='7月24-26日', sprint=False,
    length=4.381, laps=70, left=6, right=8,
    record='1:16.627', record_who='L. Hamilton', record_year=2020,
    downforce=('极高', 5), throttle=55, braking=('重度', 4), tyre=('中等', 3),
    archetype='street-precision', kind='专用赛道（低速多弯）',
    intro='亨格罗宁常被称为“没有护栏的摩纳哥”：弯角密集、几乎没有真正的直道，全油门比例只有 55%，'
          '是全年最考验下压力和车手耐心的赛道之一。超车困难，排位赛成绩几乎决定正赛大局。',
    sectors=[
        dict(id='S1', rng=[1, 3], title='唯一直道与下坡重刹',
             text='大直道之后 T1 是下坡重刹右弯，也是全场唯一的超车黄金通道；T2 是带倾斜的长左弯，'
                  '紧接 T3 顺势全油门右弯。'),
        dict(id='S2', rng=[4, 11], title='卡丁车级密集连续弯',
             text='T4 是上坡高速盲弯，T5 抛物线下坡，T6-T7 双向减速弯极窄，T8-T11 连续不间断高频变向，'
                  '车手全程没有放松的机会。'),
        dict(id='S3', rng=[12, 14], title='体育场回旋',
             text='T12 是 90 度右弯重刹，T13 的 180 度长左弯持续磨损右前胎，T14 最后一弯考验出弯牵引力并接回主直道。')],
    corners_analysis=[
        dict(cs='T1', name='下坡重刹右弯（唯一超车点）',
             text='全场最好的超越机会，靠直道尾速加晚刹。刹车点判断决定成败。'),
        dict(cs='T2', name='倾斜长左弯',
             text='带横向坡度，前轮持续受力，是这条赛道最耗前胎的弯。'),
        dict(cs='T3', name='顺势右弯',
             text='几乎不用减速，出弯要立刻准备进入密集弯群。'),
        dict(cs='T4', name='上坡高速盲弯',
             text='顶点看不到出口，靠记忆和节奏。'),
        dict(cs='T5', name='抛物线下坡弯',
             text='半径变化加下坡，刹车与转向要同时精确。'),
        dict(cs='T6-T7', name='双向减速弯',
             text='极窄的左右组合，路肩几乎用不上，只能靠机械抓地力。'),
        dict(cs='T8-T11', name='高频连续变向',
             text='四个弯连成一段，节奏断一次整段都掉，是体力和专注度的双重消耗。'),
        dict(cs='T12', name='90 度右弯',
             text='重刹进弯，出弯要给 T13 留位置。'),
        dict(cs='T13', name='180 度长左弯',
             text='持续受力的半圆弯，右前胎磨损在整圈里最大。'),
        dict(cs='T14', name='收官弯',
             text='出弯牵引力决定主直道速度，是这条赛道少数的时间来源。')],
    setup='高下压力设定加狭窄多弯，刹车与动力单元的冷却是第一挑战；气温高时成绩下滑明显。',
    watch='看 T1 的晚刹赌博，以及谁能在密集弯群里保持节奏不断。'),

'zandvoort': dict(
    round='R12', zh='荷兰大奖赛', en='Dutch Grand Prix',
    circuit_zh='赞德弗尔特赛道', circuit_en='Circuit Zandvoort',
    country='荷兰', city='赞德弗尔特', flag='🇳🇱', dates='8月21-23日', sprint=True,
    length=4.259, laps=72, left=4, right=10,
    record='1:11.097', record_who='L. Hamilton', record_year=2021,
    downforce=('高', 4), throttle=65, braking=('中等', 3), tyre=('极高', 5),
    archetype='high-downforce', kind='专用赛道（倾斜弯道）',
    intro='赞德弗尔特坐落于北海沙丘之间，最具特色的当属 3 号弯与 14 号弯的两个大倾角碗状弯（分别达 19 度与 18 度）。这种斜坡碗状倾角如同环形赛道般牢牢托住赛车，允许车手以更高速度切弯，但也对悬挂载荷与差速器设定提出了极为严苛的适配要求。',
    sectors=[
        dict(id='S1', rng=[1, 3], title='塔赞发卡与碗状倾角弯',
             text='T1 塔赞发卡是发车后的主要超车区；加速穿过 T2 后杀入 T3 休根霍兹倾斜弯，'
                  '19 度的碗状倾角提供超常抓地力。'),
        dict(id='S2', rng=[4, 10], title='沙丘间极速飞跃',
             text='T7-T8 谢夫弯道车速极高并伴随强烈下沉盲坡，落地瞬间车身负荷突变；'
                  'T9-T10 是沙丘间的中速技术弯。'),
        dict(id='S3', rng=[11, 14], title='18 度大倾斜终曲',
             text='T11-T12 汉斯·恩斯特减速弯之后，全油门冲上高达 18 度倾角的 T14 阿里·伦戴克弯，'
                  '用向心力把车弹回发车直道。')],
    corners_analysis=[
        dict(cs='T1', name='塔赞发卡',
             text='名字取自早年在此放映的《人猿泰山》，是全场最慢也最好超车的弯。'),
        dict(cs='T2', name='过渡加速弯',
             text='出弯角度决定能否带着高车速进入倾斜弯。'),
        dict(cs='T3', name='休根霍兹倾斜弯（19°）',
             text='第一个碗状倾角弯，大角度碗状倾角牢牢托住车身，过弯车速比平坦弯道高出一大截。'),
        dict(cs='T7-T8', name='谢夫弯道',
             text='高速加盲坡，车头下沉的瞬间下压力突变，是这条赛道最考验胆量的地方。'),
        dict(cs='T9-T10', name='沙丘技术弯',
             text='中速弯，机械抓地力主导，出弯线路要正对终点方向。'),
        dict(cs='T11-T12', name='汉斯·恩斯特减速弯',
             text='先右后左的减速弯，刹车与变向紧凑衔接。'),
        dict(cs='T14', name='阿里·伦戴克倾斜弯（18°）',
             text='最后一个弯就是第二个碗状倾角弯，靠向心力弹射出弯，直接决定主直道尾速。')],
    setup='倾角改变了车身载荷分布，悬挂行程与差速器锁止率需要更平顺的动态过渡；连续高速弯让轮胎横向负荷很高。',
    watch='看车手在两个倾角弯里是否敢继续加深油门，以及谢夫弯道落地时车身是否失控。'),

'monza': dict(
    round='R13', zh='意大利大奖赛', en='Italian Grand Prix',
    circuit_zh='蒙扎国家赛车场', circuit_en='Autodromo Nazionale Monza',
    country='意大利', city='蒙扎', flag='🇮🇹', dates='9月04-06日', sprint=False,
    length=5.793, laps=53, left=4, right=7,
    record='1:21.046', record_who='R. Barrichello', record_year=2004,
    downforce=('最低', 1), throttle=80, braking=('极重', 5), tyre=('中等', 3),
    archetype='speed-temple', kind='专用赛道（速度圣殿）',
    intro='蒙扎被称为“速度圣殿”：全油门比例位居全年之首（约 80%），调校下压力极低且制动负荷极大。赛车绝大多数时间都在极限全开狂奔，仅有几处减速弯迫使车辆剧烈减速。超车比拼的不是弯道速度，而是直道极限尾速与更晚的刹车点。',
    sectors=[
        dict(id='S1', rng=[1, 3], title='第一减速弯',
             text='主直道超过 350 km/h 冲入 T1-T2 雷蒂菲洛减速弯，急刹到 75 km/h，刹车载荷达到 5.8G；'
                  '随后全油门掠过 T3 大弧弯。'),
        dict(id='S2', rng=[4, 7], title='罗吉亚与莱斯莫双弯',
             text='T4-T5 瓦里安特·罗吉亚减速弯之后，杀入皇家公园森林深处的 T6 莱斯莫 1 号与 T7 莱斯莫 2 号，'
                  '考验极低下压力下的抓地极限。'),
        dict(id='S3', rng=[8, 11], title='阿斯卡里与帕拉波利卡',
             text='高速穿过 Serraglio 直道切入 T8-T10 流畅的阿斯卡里减速弯；背直道之后是传奇的长抛物线弯'
                  'T11 帕拉波利卡。')],
    corners_analysis=[
        dict(cs='T1-T2', name='雷蒂菲洛减速弯（5.8G）',
             text='从 350 km/h 刹到 75 km/h，是全年最极端的减速。刹车盘、轮胎和车手颈部同时到极限，也是第一超车点。'),
        dict(cs='T3', name='大弧弯',
             text='高速右弯，几乎全油门，之后接一段加速。'),
        dict(cs='T4-T5', name='罗吉亚减速弯',
             text='两段紧凑的减速弯，第二次的出口角度决定后面森林段的速度。'),
        dict(cs='T6-T7', name='莱斯莫双弯',
             text='森林里的两个中高速右弯，极低下压力设定下抓地力全靠机械抓地与车手信心。'),
        dict(cs='T8-T10', name='阿斯卡里减速弯',
             text='三段相连的减速弯，节奏一旦乱了整段都慢，出弯接全年最长的直道之一。'),
        dict(cs='T11', name='帕拉波利卡',
             text='蒙扎的收官长抛物线右弯，车手都想榨干最后一点速度，因为出弯就是主直道。')],
    setup='全年最低风阻设定，2026 年直道模式加 350kW 电机爆发，直道尾速有望逼近历史峰值；代价是每个弯角都要靠刹车来补。',
    watch='看直道尾速的差距和 T1 谁刹得更晚——蒙扎的超车几乎全部发生在刹车区。'),

'madring': dict(
    round='R14', zh='西班牙大奖赛', en='Spanish Grand Prix',
    circuit_zh='马德里 IFEMA 市街赛道（Madring）', circuit_en='Madring, Madrid IFEMA Street Circuit',
    country='西班牙', city='马德里', flag='🇪🇸', dates='9月11-13日', sprint=False,
    length=5.474, laps=56, left=None, right=None,
    record=None, record_who=None, record_year=None,
    downforce=('中等', 3), throttle=62, braking=('重度', 4), tyre=('中等', 3),
    archetype='street-precision', kind='新建市街赛道（赛季首秀）',
    intro='2026 年西班牙大奖赛移师马德里，围绕 IFEMA 国际会展中心的新建市街赛道是本赛季最大的未知数。'
          '它既有展馆区的直角重刹弯，也有一段带倾角的高速长弯和一条地下隧道，属于“混合型”街道赛道。',
    sectors=[
        dict(id='S1', rng=[1, 8], title='IFEMA 展馆区',
             text='围绕会展中心内部街道展开，多为 90 度直角重刹弯与短促变向，重点考验低速牵引力和制动稳定性。'),
        dict(id='S2', rng=[9, 16], title='跨线桥与倾角高速弯',
             text='穿越 M-11 高速公路高架桥连接线，其中有一段带明显倾角的长弧高速弯，'
                  '空气动力学垂直下压力在这里冲击强烈。'),
        dict(id='S3', rng=[17, 22], title='隧道与外环大直道',
             text='穿过皇家马德里训练基地 Valdebebas 侧翼的专属地下隧道与宽阔外环直道，'
                  '末端配有开阔的重刹回旋超车点。')],
    corners_analysis=[
        dict(cs='T1-T3', name='展馆区直角组合',
             text='连续 90 度弯，刹车点、转向点、油门点都靠得很近，是低速牵引力的照妖镜。'),
        dict(cs='T4-T6', name='短促变向段',
             text='弯与弯之间几乎没有直道，车身响应快不快在这里最直观。'),
        dict(cs='T7-T8', name='连接加速弯',
             text='出弯角度决定能否带着速度进入跨线桥段。'),
        dict(cs='T9-T12', name='高架桥连接线',
             text='路面材质变化、接缝多，抓地力不稳定，车手要不断微调刹车点。'),
        dict(cs='T13-T16', name='倾角长弧高速弯',
             text='带横向倾角的长弯，赛道壁把车托住，是这条街道赛道上最快的一段。'),
        dict(cs='T17-T19', name='隧道段',
             text='进出隧道时光线突变、气流受限，路面还更滑，是失误高发区。'),
        dict(cs='T20-T22', name='外环直道与回旋超车点',
             text='宽阔外环直道之后是开阔的重刹回旋区，正赛超车大多发生在这里。')],
    setup='全新落成的混合市街赛道，路面涵盖展馆柏油与市政沥青，摩擦系数差异大；车队主要靠模拟器建模，实战中的抓地力预测全季最难。',
    watch='首秀站没有历史数据，注意练习赛里谁最快摸清不同路面的刹车距离。'),

'baku': dict(
    round='R15', zh='阿塞拜疆大奖赛', en='Azerbaijan Grand Prix',
    circuit_zh='巴库城市赛道', circuit_en='Baku City Circuit',
    country='阿塞拜疆', city='巴库', flag='🇦🇿', dates='9月24-26日', sprint=False,
    length=6.003, laps=51, left=8, right=12,
    record='1:43.009', record_who='C. Leclerc', record_year=2019,
    downforce=('低', 2), throttle=66, braking=('重度', 4), tyre=('低', 2),
    archetype='speed-temple', kind='街道赛道（矛盾之王）',
    intro='巴库是 F1 里最矛盾的赛道：一边是全世界最窄的古城墙段（最窄处仅 7.6 米），另一边是长达 2.2 公里的全油门长直道。车队必须在高下压力与超低风阻之间艰难折中；而狭窄街道与高速长直道的强烈反差，也让这里极易引发安全车与意外事故。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='直角林荫大道',
             text='沿普希金街布局的连续 90 度直角重刹弯（T1、T2、T3），极速冲刺后剧烈减速，路面宽阔，容易产生多车并排的超车。'),
        dict(id='S2', rng=[5, 15], title='古城堡狭窄迷宫',
             text='T7 险恶左弯进入中世纪内城；著名的 T8-T11 城堡弯赛道最窄处仅 7.6 米，容错率为零；'
                  '随后在 T13-T15 连续下坡高速盲弯贴墙呼啸而出。'),
        dict(id='S3', rng=[16, 20], title='2.2 公里全油门直道走廊',
             text='T16 90 度左弯出弯后进入长达 2.2 公里的全球最长全油门街道通道，'
                  'T17-T20 均为全油门弯，直道尾速突破 360 km/h。')],
    corners_analysis=[
        dict(cs='T1-T3', name='普希金街直角弯组',
             text='宽阔路面上的连续重刹直角弯，第一圈常出现三车并排。'),
        dict(cs='T4', name='过渡右弯',
             text='把车带向老城方向的入口弯。'),
        dict(cs='T7', name='入城左弯',
             text='从这里开始护墙突然贴近，车速虽然不高但心理压力最大。'),
        dict(cs='T8-T11', name='城堡弯（最窄 7.6 米）',
             text='全赛季最窄的一段，两车无法并排。任何一次擦墙都可能直接结束比赛。'),
        dict(cs='T13-T15', name='下坡高速盲弯',
             text='贴墙下坡，出口看不见，是这条赛道最容易出红旗的地方。'),
        dict(cs='T16', name='直道起点左弯',
             text='出弯牵引力决定 2.2 公里直道的尾速，是超车链条的起点。'),
        dict(cs='T17-T20', name='全油门弯群与终点重刹',
             text='四个不用减速的弯，之后是终点前的极限重刹区，全年超车概率最高的位置之一。')],
    setup='调校矛盾之王：S2 城堡区需要高下压力，S3 的 2.2 公里直道需要超低阻力，车队只能折中，而直道末端的能量管理（防止电机电量耗尽削波掉速）往往比设定本身更关键。',
    watch='看直道末端谁还留着电：在巴库，电量决定谁能在 T16 之后完成超越。'),

'marina-bay': dict(
    round='R17', zh='新加坡大奖赛', en='Singapore Grand Prix',
    circuit_zh='滨海湾市街赛道', circuit_en='Marina Bay Street Circuit',
    country='新加坡', city='滨海湾', flag='🇸🇬', dates='10月09-11日', sprint=True,
    length=4.940, laps=62, left=8, right=11,
    record='1:34.486', record_who='D. Ricciardo', record_year=2024,
    downforce=('极高', 5), throttle=50, braking=('极重', 5), tyre=('中等', 3),
    archetype='street-precision', kind='夜间街道赛道（冲刺赛站）',
    intro='新加坡是 F1 历史上的首场夜间大奖赛，也是全年体能消耗最为严苛的分站：这里高温高湿、路面颠簸、弯角密集且制动负荷极高。在耗时近两小时的整场正赛中，车手往往会流失数公斤汗水。',
    sectors=[
        dict(id='S1', rng=[1, 5], title='薛尔思减速弯',
             text='发车直道后经 T1-T3 薛尔思复合弯进入市区，穿过共和国林荫道加速后迎来 T5 90 度右弯。'),
        dict(id='S2', rng=[6, 14], title='金融街与安德逊桥',
             text='长直道后 T7 是 90 度左弯重刹超车点；穿过草场经过古老狭窄的安德逊桥（T11-T13），'
                  '紧接著名的 T14 重刹右弯。'),
        dict(id='S3', rng=[15, 19], title='改建后的高速直道',
             text='移除原看台附近的四个迟缓直角弯后形成开阔直道；随后进入 T16-T17 右左快速弯，'
                  '经 T18-T19 驶向主看台。')],
    corners_analysis=[
        dict(cs='T1-T3', name='薛尔思复合弯',
             text='连续变向的减速弯，出口要给林荫道加速段留位置。'),
        dict(cs='T5', name='90 度右弯',
             text='赛段 1 收尾，刹车点晚能多带一点速度进下一段。'),
        dict(cs='T7', name='金融街重刹左弯',
             text='主要超车点，护墙近在咫尺，锁死就等于上墙。'),
        dict(cs='T11-T13', name='安德逊桥',
             text='桥面窄、路面接缝滑，车速不高但极其考验耐心，也是事故高发点。'),
        dict(cs='T14', name='重刹右弯',
             text='全年制动负荷最严苛的重刹区之一，车手在这里的心率和颈部负荷均达峰值。'),
        dict(cs='T16-T17', name='右左快速弯',
             text='改建后节奏最快的一段，是新加坡少见的“流畅”时刻。'),
        dict(cs='T18-T19', name='主看台前收尾',
             text='出弯线路要正对终点直道，最后一圈的保护或进攻都发生在这里。')],
    setup='夜战高温高湿，赛道颠簸，制动系统承受全季最严苛的热衰减威胁，电池冷却也面临重大考验。'
          '这条赛道上“完赛”本身就是成绩。',
    watch='注意车手在 T14 之后是否还能保持刹车精度，以及进站窗口时机的赌博。'),
}
