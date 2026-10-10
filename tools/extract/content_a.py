# -*- coding: utf-8 -*-
"""Hand-authored ApexAtlas content, derived from the 2026 Circuit Technical Guide.

Schema per track (see build_data.py for how it is merged with map geometry):
  corners_analysis[].cs  corner codes as shown on the map, e.g. "T1-T2", "T5", "T20A"
  sectors[].rng          [first corner, last corner] per the guide's sector split
  downforce/braking/tyre (label, 1-5) straight from the guide's matrix
"""

TRACKS = {
'albert-park': dict(
    round='R01', zh='澳大利亚大奖赛', en='Australian Grand Prix',
    circuit_zh='阿尔伯特公园赛道', circuit_en='Albert Park Circuit',
    country='澳大利亚', city='墨尔本', flag='🇦🇺', dates='3月06-08日', sprint=False,
    length=5.278, laps=58, left=6, right=8,
    record='1:19.813', record_who='C. Leclerc', record_year=2024,
    downforce=('中高', 4), throttle=72, braking=('重度', 4), tyre=('中等', 3),
    archetype='stop-and-go', kind='公园半永久赛道',
    intro='墨尔本是很多赛季的开场站，也是一条“不像街道赛的街道赛”：赛道围绕阿尔伯特湖展开，大部分路面平时为公园公共道路，赛事期间才封闭使用。它的特点是长直道与高速弯较多、制动负荷高，超车机会主要集中在 T3 和 T13 两个重刹区。',
    sectors=[
        dict(id='S1', rng=[1, 5], title='重刹入场段',
             text='发车直道末端进 T1 是全场刹车最狠的地方，纵向减速最大。T1-T2 是一组先右后左的减速弯，'
                  '出弯时车身贴外侧路肩很常见。T3 是紧凑右弯，也是全场最主要的内线超车点；T4-T5 连续中速变向，'
                  '出弯线路直接决定能不能带着高车速进入湖畔大道。'),
        dict(id='S2', rng=[6, 10], title='湖畔高速巡航段',
             text='改装后的 T6 开阔平缓，赛车全油门冲进沿湖展开的高速走廊。最狠的是 T9-T10 这组极速变向弯：'
                  '车速超过 245 km/h，横向载荷超过 4.5G，车身侧倾控制不好的赛车会明显推头或甩尾。'),
        dict(id='S3', rng=[11, 14], title='技术重刹与出弯牵引力',
             text='T11-T12 是中速复合弯，T13 迎来全场第二大重刹点，内线强超经常在这里发生。'
                  '最后一弯 T14 是紧凑左弯，油门开度控制不好会后轮打滑，白白丢掉主直道的冲刺速度。')],
    corners_analysis=[
        dict(cs='T1-T2', name='发车重刹 + 琼斯减速弯',
             text='先右后左的连续减速弯。进弯前的减速强度全场第一，刹车点差一米就会被前车堵住线路。出弯要借外侧路肩把车头甩正。'),
        dict(cs='T3', name='全场头号超车点',
             text='紧凑右弯，前速低、出弯油门重要。后车通常在这里靠内线强行占位，是正赛开场最常见的超越。'),
        dict(cs='T4-T5', name='中速连续变向',
             text='两次方向切换，节奏比单圈速度更重要。这组弯的出弯线路决定后面整条湖畔大道的初速。'),
        dict(cs='T6-T8', name='湖畔高速走廊',
             text='开阔平缓的高速段，赛车基本全油门，主要考验空气动力学稳定性和悬挂吸震。'),
        dict(cs='T9-T10', name='极速变向弯（4.5G）',
             text='全场最出名的一段：车速超过 245 km/h 的连续变向，横向加速度超过 4.5G。底盘侧倾刚度不足的车手会在这里损失大量时间。'),
        dict(cs='T13', name='第二重刹区',
             text='刹车点晚、减速幅度大，是全场第二个主要超车窗口，也是进站出站最容易发生缠斗的位置。'),
        dict(cs='T14', name='收官左弯',
             text='紧凑左弯，出弯牵引力决定主直道尾速。车手常说“墨尔本的圈速是在 T14 出弯时定生死”。')],
    setup='湖畔高速段可以充分使用直道模式（低风阻姿态）；T1 与 T13 两次强重刹为 MGU-K 提供大量电能回收，'
          '是能量收支最容易做正的赛道之一。',
    watch='看两个点：开场几圈 T3 的内线争夺，以及 T9-T10 赛车在 245 km/h 以上连续变向时的车身姿态。'),

'shanghai': dict(
    round='R02', zh='中国大奖赛', en='Chinese Grand Prix',
    circuit_zh='上海国际赛车场', circuit_en='Shanghai International Circuit',
    country='中国', city='上海', flag='🇨🇳', dates='3月13-15日', sprint=True,
    length=5.451, laps=56, left=9, right=7,
    record='1:32.238', record_who='M. Schumacher', record_year=2004,
    downforce=('中高', 4), throttle=58, braking=('极重', 5), tyre=('极高', 5),
    archetype='stop-and-go', kind='专用赛道（冲刺赛站）',
    intro='上海国际赛车场是一条“前段磨车、后段拼直线”的典型赛道。发车后紧接着一段独一无二、盘旋超过 270 度的螺旋收缩右弯（“蜗牛弯”），对左前胎和制动系统极其残酷；赛道末段则是长达 1.2 公里的超长大直道接重刹发卡弯，构成了全场最主要的超车窗口。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='金石弯（螺旋收缩右弯）',
             text='T1-T2 是一个 270 度、半径越来越小的右弯：车一边减速一边持续承受向心载荷，前轮同时被纵向和横向摩擦力撕扯，'
                  '是全赛季对前左胎最狠的一段。T3-T4 用左转收尾，对前轮指向响应要求极高。'),
        dict(id='S2', rng=[5, 10], title='中高速流动 + 重刹发卡',
             text='T6 是重刹右发卡；紧接着 T7-T8 高速摇摆弯，车速保持在 230 km/h 以上，气流稳不稳直接决定单圈；'
                  'T9-T10 双左弯考验低档位出弯时的机械抓地力。'),
        dict(id='S3', rng=[11, 16], title='1.2 公里大直道与终点发卡',
             text='T11-T13 一组半径递增的抛物线弯把车带进长达 1.2 公里的直道，尾速逼近 340 km/h。'
                  '直道尽头的 T14 极慢发卡是全球最有戏剧性的重刹超车点，刹车载荷达到 5.2G；T16 回到发车区。')],
    corners_analysis=[
        dict(cs='T1-T2', name='金石弯 · 螺旋收缩右弯',
             text='入口宽、出口窄，半径持续收缩。车手要在减速的同时一直加转向角，前轮负荷在整圈里最高。'),
        dict(cs='T3-T4', name='左转收尾',
             text='从长右弯突然换成左转，车头指向必须干净。这里慢一点，后面直道的初速就跟着掉。'),
        dict(cs='T6', name='重刹右发卡',
             text='第二段的第一次重刹，刹车点判断错了要么冲过头要么出弯速度不够。'),
        dict(cs='T7-T8', name='高速摇摆弯（230 km/h+）',
             text='两次快速换向，车速很高，车身姿态稍微不稳就会破坏空气动力学平衡。'),
        dict(cs='T9-T10', name='双左弯',
             text='低档位弯角，考验出弯时后轮的牵引力，是轮胎磨损被放大的地方。'),
        dict(cs='T11-T13', name='抛物线组合弯 → 大直道',
             text='半径越来越大，出弯角度越来越开，目的只有一个：把车速带进 1.2 公里直道。'),
        dict(cs='T14', name='终点发卡（5.2G 重刹）',
             text='全场最重要的超车点。后车会赌晚刹车，前车则要保住内线；刹车盘温度和轮胎状态在这里同时到极限。'),
        dict(cs='T16', name='回归发车线',
             text='最后一个弯，出弯线路要正对维修区直道。')],
    setup='1.2 公里大直道对 350kW 电机的电量分配是极限考验：直道模式开早了、放电磁线太狠，'
          '后半程就会出现明显掉速（超剪辑）。这里的调校核心是能量释放曲线，而不是单纯的下压力取舍。',
    watch='注意 T14 之前的直道尾速和两车电量状态：谁在直道末端还留着电，谁就能在发卡弯前完成超越。'),

'suzuka': dict(
    round='R03', zh='日本大奖赛', en='Japanese Grand Prix',
    circuit_zh='铃鹿国际赛车场', circuit_en='Suzuka International Racing Course',
    country='日本', city='铃鹿', flag='🇯🇵', dates='3月27-29日', sprint=False,
    length=5.807, laps=53, left=8, right=10,
    record='1:30.983', record_who='L. Hamilton', record_year=2019,
    downforce=('高', 5), throttle=67, braking=('中等', 3), tyre=('极高', 5),
    archetype='high-downforce', kind='专用赛道（8 字形）',
    intro='铃鹿赛道由专业设计师精心规划打造，依自然山势起伏铺就，是全球唯一呈“8字形”立体交叉布局的 F1 赛道。整圈节奏连贯紧凑、毫无喘息之机，被历代车手公认为最能真实检验赛车综合空气动力学与底盘平衡的终极考场。',
    sectors=[
        dict(id='S1', rng=[1, 7], title='S 弯与逆转弯',
             text='起跑直道后高速掠过 T1-T2 双右弯，接着切入 T3-T6 的极速韵律弯群。这一段对前轮导流和底盘下压力平衡的要求'
                  '是全季最高的，赛车必须“稳”，任何一次车身起伏都会连锁传到后面几个弯。T7 邓禄普弯是上坡全油门左弯。'),
        dict(id='S2', rng=[8, 14], title='德格纳双弯与立交桥',
             text='T8 德格纳 1 号是高速盲弯，T9 德格纳 2 号是直角重刹，两弯都极度贴墙，偏差一点就是撞墙。'
                  '穿过桥洞后是全场最慢的 T11 发卡（约 65 km/h），随后经 T12 200R 冲入经典的 T13-T14 匙形弯。'),
        dict(id='S3', rng=[15, 18], title='130R 与卡西欧三角',
             text='背直道上坡后以接近 310 km/h 全油门通过 T15“130R”，这是全年最考验下压力的单个弯角；'
                  '随后在 T16 卡西欧减速弯暴力减速（塞纳与普罗斯特 1989 年冲突的发生地），T17-T18 冲向终点。')],
    corners_analysis=[
        dict(cs='T1-T2', name='双右弯入口',
             text='高速进入，走线要留给后面的 S 弯，太靠外会毁掉整段节奏。'),
        dict(cs='T3-T6', name='极速 S 弯群',
             text='连续左右快速换向，靠的是空气动力学而不是机械抓地。这一段是铃鹿单圈的骨架。'),
        dict(cs='T7', name='邓禄普弯',
             text='上坡全油门左弯，车身负载大，出弯接一段短直道。'),
        dict(cs='T8-T9', name='德格纳双弯',
             text='T8 是看不见出口的高速盲弯，T9 紧接直角重刹，两弯都贴墙。全年最容易在这里出事故。'),
        dict(cs='T11', name='安圣发卡（约 65 km/h）',
             text='全场最慢的弯，重刹加低速转向，是少数能拉开差距的慢弯。'),
        dict(cs='T12', name='200R',
             text='名字来自入弯速度约 200 km/h 的长右弯，下压力不足的车在这里会明显吃亏。'),
        dict(cs='T13-T14', name='匙形弯',
             text='两段相连的左弯，需要稳定的车头指向，出弯接背直道。'),
        dict(cs='T15', name='130R',
             text='接近 310 km/h 全油门通过，颈部和下压力的双重极限，全年最标志性的单个弯角。'),
        dict(cs='T16', name='卡西欧三角减速弯',
             text='从 130R 的高速直接暴力减速，历史名场面发生地，也是超车与失误的高发点。')],
    setup='整圈大部分时间处于弯道模式（高下压力），S 弯段把下压力推到极限；高横向载荷让硬配方轮胎的胎壁承受极大形变剪切，'
          '轮胎起泡和颗粒化在这里比别处更早出现。',
    watch='看车手在 130R 是否敢完全松开油门踏板，以及 S 弯里前后车的车身起伏是否同步——这最能反映下压力平衡。'),

'sepang': dict(
    round='R16', zh='巴林大奖赛（雪邦承办）', en='Bahrain GP (Sepang)',
    circuit_zh='雪邦国际赛车场', circuit_en='Sepang International Circuit',
    country='马来西亚', city='雪邦', flag='🇲🇾', dates='10月02-04日', sprint=False,
    length=5.543, laps=56, left=5, right=10,
    record='1:34.080', record_who='S. Vettel', record_year=2017,
    downforce=('中高', 4), throttle=65, braking=('重度', 4), tyre=('极高', 5),
    archetype='stop-and-go', kind='专用赛道（异地承办）',
    intro='按 2026 赛季指南，原定巴林站因地区局势改到马来西亚雪邦承办。雪邦的看点是两条超长直道和一组剪刀形发卡，'
          '加上热带多变的天气，让策略和轮胎管理常常比排位赛成绩更能决定结果。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='剪刀形交叉双发卡',
             text='大直道末端的 T1-T2 是先下坡再上坡的反向发卡组合，两弯之间几乎没有喘息空间；'
                  '随后加速进入长半径快速右弯 T3，在 T4 用一次重刹收尾。'),
        dict(id='S2', rng=[5, 11], title='高速横摆与技术发卡',
             text='T5-T6 是极速变向左弯，T7-T8 双中速右弯考验前轮指向，T9 则是极慢的下坡左发卡，'
                  '刹车与低速转向的落差很大。'),
        dict(id='S3', rng=[12, 15], title='双长大直道与看台终局',
             text='T12-T13 高速掠过，接着是 900 多米的背直道狂飙，最后进入 T15 标志性大看台发卡——重刹超车点，'
                  '折回主看台发车直道。')],
    corners_analysis=[
        dict(cs='T1-T2', name='剪刀形双发卡',
             text='反向相连的两个发卡，中间有坡度变化。第一弯的出弯位置决定第二弯能不能走对线。'),
        dict(cs='T3', name='长半径右弯',
             text='高速弯，考验下压力和前轮稳定性，是雪邦最容易拉开时间的一段。'),
        dict(cs='T4', name='重刹收尾',
             text='赛段 1 的刹车点，晚刹能带更多速度进直道，但风险是出弯偏宽。'),
        dict(cs='T5-T6', name='极速变向',
             text='连续变向中的左弯组合，气流不稳会立刻反映在车尾上。'),
        dict(cs='T7-T8', name='双中速右弯',
             text='机械抓地力主导，前轮指向精度决定出弯速度。'),
        dict(cs='T9', name='下坡左发卡',
             text='赛段 2 最慢的弯，下坡入口让刹车感受很奇怪，很多车手在这里锁死。'),
        dict(cs='T12-T13', name='高速掠过段',
             text='为背直道做准备，重点是保持车速而不是走线漂亮。'),
        dict(cs='T15', name='大看台发卡（超车点）',
             text='900 米直道之后的重刹区，全年最典型的“直道速度换超车位置”的场面。')],
    setup='热带高温与突发暴雨同时存在，冷却负荷和雨地策略都要准备；两条长直道让直道模式与超车模式的博弈非常直接。',
    watch='注意 T15 之前背直道的尾速差：超车模式能不能开、电量还剩多少，往往在这条直道上就见分晓。'),

'jeddah': dict(
    round='—', zh='沙特阿拉伯大奖赛（吉达）', en='Saudi Arabian GP (Jeddah)',
    circuit_zh='吉达滨海赛道', circuit_en='Jeddah Corniche Circuit',
    country='沙特阿拉伯', city='吉达', flag='🇸🇦', dates='未列入 2026 赛历', sprint=False,
    length=6.174, laps=50, left=10, right=17,
    record=None, record_who=None, record_year=None,
    downforce=('中低', 2), throttle=79, braking=('重度', 4), tyre=('低', 2),
    archetype='speed-temple', kind='市街高速赛道',
    intro='吉达是赛历上最快的街道赛道：赛道沿红海滨海大道铺开，全油门比例极高且护墙紧贴路面，容错率极低。尽管 2026 赛季该分站未列入正赛日程，但其极致的高速市街特性依然极具代表性。',
    sectors=[
        dict(id='S1', rng=[1, 13], title='海岸线高速长弯段',
             text='发车后是一段很长的全油门区，T1-T2 是高速右左组合，随后 T3-T6 用一组逐渐收紧的右弯把车带向海岸线。'
                  '这一段几乎没有重刹，主要考验赛车在高速下的稳定性与车手的注意力。'),
        dict(id='S2', rng=[14, 19], title='旧城区技术回旋',
             text='T14-T16 是全场节奏最慢的连续弯，路肩高、出口窄，是少数能靠机械抓地力拉开差距的地方；'
                  'T17-T19 再次加速，把车送回主直道方向。'),
        dict(id='S3', rng=[20, 27], title='回场冲刺与终点长弯',
             text='T20-T22 的高速左弯之后是一条很长的全油门段，T23-T27 用一组高速右弯收尾，'
                  '进终点直道时车速很高，超车模式通常在这段被触发。')],
    corners_analysis=[
        dict(cs='T1-T2', name='发车高速右左组合',
             text='第一弯就要在高速下决定线路，走错一步后面几个弯全部连锁受影响。'),
        dict(cs='T3-T6', name='逐渐收紧的右弯群',
             text='半径越来越小，需要一边加速一边加转向，是这条赛道最考验节奏的地方。'),
        dict(cs='T7-T13', name='海岸线全油门段',
             text='护墙紧贴赛道，赛车几乎没有容错空间，车手在这里的“敢不敢”差异最明显。'),
        dict(cs='T14-T16', name='旧城区慢弯',
             text='全场少数的低速段，路肩和出口角度都不友好，机械抓地力好的车能追回时间。'),
        dict(cs='T17-T19', name='重新加速',
             text='出弯牵引力决定后面直道的尾速，是超车链条的起点。'),
        dict(cs='T20-T22', name='高速左弯组',
             text='下压力需求高，轮胎外侧负荷大，常在这里出现轮胎颗粒化。'),
        dict(cs='T23-T27', name='终点前长右弯群',
             text='高速收尾，走线要正对终点直道，也是超车模式最容易生效的位置。')],
    setup='全油门比例高、刹车区少而短，能量回收主要靠几个减速弯；低风阻设定与贴墙高速之间的取舍是这条赛道的核心矛盾。',
    watch='看车手在护墙前是否还能保持全油门，以及直道末端超车模式的开启时机。'),

'miami': dict(
    round='R04', zh='迈阿密大奖赛', en='Miami Grand Prix',
    circuit_zh='迈阿密国际赛道', circuit_en='Miami International Autodrome',
    country='美国', city='迈阿密', flag='🇺🇸', dates='5月01-03日', sprint=True,
    length=5.412, laps=57, left=12, right=7,
    record='1:29.708', record_who='M. Verstappen', record_year=2023,
    downforce=('中等', 3), throttle=60, braking=('重度', 4), tyre=('中等', 3),
    archetype='street-precision', kind='体育场周边混合赛道（冲刺赛站）',
    intro='迈阿密国际赛道围绕硬石体育场而建，兼具致敬银石与斯帕的高速连续弯段，以及高速公路立交桥下的狭窄技术弯群。赛道弯角众多、重心切换频繁，加之当地的高温高湿环境，对整车散热系统构成了严峻考验。',
    sectors=[
        dict(id='S1', rng=[1, 8], title='发车重刹与流动变向',
             text='T1 是主直道末端的开阔右弯，重刹加宽出口，超车机会多；随后的 T4-T8 是模仿斯帕与银石的高速连续摇摆段，'
                  '需要灵敏的前翼抓地和能吸掉颠簸的悬挂。'),
        dict(id='S2', rng=[9, 16], title='高架桥下的狭窄迷宫',
             text='快速穿过 T9-T11 后进入高速公路高架桥下的 T14-T15 微型减速弯：路面起伏、有盲坡、路肩颠簸，'
                  '前轮抱死和打滑在这里非常常见。'),
        dict(id='S3', rng=[16, 19], title='1.28 公里反向大直道',
             text='T16 出弯的牵引力直接决定后直道初速；长达 1.28 公里的直道尽头，T17 左弯是核心超车区，'
                  '随后经 T18-T19 驶向主看台。')],
    corners_analysis=[
        dict(cs='T1', name='发车开阔右弯',
             text='刹车点晚、出口宽，是正赛第一圈最容易发生连环超车的入口。'),
        dict(cs='T4-T8', name='高速连续摇摆段',
             text='一段接一段的中高速弯，节奏不能断。前翼不稳的车在这里会一段一段掉时间。'),
        dict(cs='T9-T11', name='过渡加速段',
             text='把车速带到桥下迷宫前的加速区，走线要尽量拉直。'),
        dict(cs='T14-T15', name='桥下微型减速弯',
             text='狭窄、颠簸、有盲坡。这里最容易发生前轮锁死和出弯跑宽，也是安全车的高发区。'),
        dict(cs='T16', name='直道起点弯',
             text='出弯牵引力决定 1.28 公里直道的尾速，是超车链条的第一环。'),
        dict(cs='T17', name='核心超车弯',
             text='长直道尽头的左弯，配合超车模式，是全场超越概率最高的位置。'),
        dict(cs='T18-T19', name='回归主看台',
             text='两弯收尾，线路要正对发车直道。')],
    setup='高温高湿对 2026 全新动力单元的散热是严苛考验，电控的防过热保护策略往往比底盘调校更能决定成绩。',
    watch='注意桥下 T14-T15 谁的车轮锁死、谁跑宽；这段之后长直道的超车往往就是这里排好的。'),
}
