# -*- coding: utf-8 -*-
"""ApexAtlas content, batch D: R18-R23."""

TRACKS = {
'cota': dict(
    round='R18', zh='美国大奖赛', en='United States Grand Prix',
    circuit_zh='美洲赛道（COTA）', circuit_en='Circuit of the Americas',
    country='美国', city='奥斯汀', flag='🇺🇸', dates='10月23-25日', sprint=False,
    length=5.513, laps=56, left=11, right=9,
    record='1:36.169', record_who='C. Leclerc', record_year=2019,
    downforce=('中高', 4), throttle=62, braking=('重度', 4), tyre=('高', 4),
    archetype='high-downforce', kind='专用赛道（起伏地形）',
    intro='COTA 是把世界经典弯角“抄”在一起的赛道：开头模仿银石的高速 S 弯，中段有土耳其式的多顶点长弯，'
          '第一弯则是全赛季最陡的上坡发卡。高低起伏是它的关键词，也是赛车调校最难的地方。',
    sectors=[
        dict(id='S1', rng=[1, 6], title='40 米高坡与蛇形弯群',
             text='发车后以 11% 坡度仰攻到 T1 盲弯发卡顶点，这段高差约 40 米；下坡后以超过 260 km/h 杀入'
                  '融合银石精髓的 T3-T6 高速 S 弯蛇形矩阵。'),
        dict(id='S2', rng=[7, 12], title='1.2 公里反向大直道',
             text='T7-T9 是技术中速弯，T11 紧凑左发卡出弯衔接长达 1.2 公里的背直道，'
                  '直道末端 T12 迎来 5.4G 的超强重刹。'),
        dict(id='S3', rng=[13, 20], title='体育场弯与四重顶点长弯',
             text='T13-T15 是体育场慢速弯；紧接模仿伊斯坦布尔 8 号弯的四重 APEX 多半径长右弯 T16-T18；'
                  '经 T19-T20 回到主直道。')],
    corners_analysis=[
        dict(cs='T1', name='陡坡发卡（11% 坡度）',
             text='全赛季最陡的上坡入口，看不到出口就要刹车。出弯位置决定后面整段高速弯。'),
        dict(cs='T3-T6', name='高速 S 弯矩阵',
             text='连续起伏的高速变向，节奏来自银石。底盘离地间隙稍低就会刮地。'),
        dict(cs='T7-T9', name='技术中速弯',
             text='机械抓地力主导，出弯角度为 T11 做准备。'),
        dict(cs='T11', name='紧凑左发卡',
             text='1.2 公里直道的起点，这里省下的每一公里时速都会在直道上放大。'),
        dict(cs='T12', name='5.4G 重刹区',
             text='全场最主要的超车点，刹车载荷极高，也是能量回收最集中的地方。'),
        dict(cs='T13-T15', name='体育场弯群',
             text='慢速连续弯，牵引力和低速转向精度的考验。'),
        dict(cs='T16-T18', name='四重顶点长右弯',
             text='一个弯里有四个切点，半径不断变化，走线选择没有标准答案。'),
        dict(cs='T19-T20', name='回归主直道',
             text='最后两个弯，出弯要正对发车线。')],
    setup='赛道颠簸严重考验悬挂阻尼，全景式高低起伏对空气动力学平台的平稳度极其挑剔——车高设定稍微不对，'
          '下压力就会随路面起伏剧烈波动。',
    watch='看 T1 上坡刹车点，以及 T16-T18 长右弯里谁选的走线更省力。'),

'rodriguez': dict(
    round='R19', zh='墨西哥城大奖赛', en='Mexico City Grand Prix',
    circuit_zh='罗德里格斯兄弟赛车场', circuit_en='Autódromo Hermanos Rodríguez',
    country='墨西哥', city='墨西哥城', flag='🇲🇽', dates='10月30-11月01日', sprint=False,
    length=4.304, laps=71, left=7, right=10,
    record='1:17.774', record_who='V. Bottas', record_year=2021,
    downforce=('最大', 5), throttle=54, braking=('极重', 5), tyre=('低', 2),
    archetype='street-precision', kind='专用赛道（高海拔）',
    intro='墨西哥城海拔 2285 米，空气密度比海平面低约 25%。这意味着下压力和发动机进气同时“打折”，'
          '车队会装上全年最大的尾翼，但阻力却只有蒙扎水平。最独特的场面是赛车冲进棒球场看台环绕的那段低速弯。',
    sectors=[
        dict(id='S1', rng=[1, 3], title='全季最长起跑冲刺',
             text='从杆位到 T1 刹车点距离超过 800 米，尾速逼近 360 km/h；T1-T3 是典型的右-左-右组合减速弯。'),
        dict(id='S2', rng=[4, 11], title='湖泊路段高速 S 弯',
             text='长直道后 T4-T5 减速弯是超车区；随后的 T7-T11 是一组考验下压力平衡的高速摇摆 S 弯。'),
        dict(id='S3', rng=[12, 17], title='索尔棒球场传奇看台',
             text='T12 右弯切入旧棒球场看台腹地，在数万车迷环绕下以极低速完成 T13-T15（约 65 km/h）的回旋；'
                  '穿过佩拉尔塔区后半段，T17 重返发车线。')],
    corners_analysis=[
        dict(cs='T1', name='800 米后的重刹',
             text='全年最长的全油门冲刺段之后，刹车点判断和刹车热管理同时到极限。'),
        dict(cs='T2-T3', name='右左组合弯',
             text='先右后左的过渡，出弯要给长直道留线路。'),
        dict(cs='T4-T5', name='减速弯超车区',
             text='赛段 2 的主要超越点，内线空间足够。'),
        dict(cs='T7-T11', name='高速摇摆 S 弯',
             text='连续变向，下压力在稀薄空气里效果打折，车手要靠更慢的转向输入避免失控。'),
        dict(cs='T12', name='进入棒球场',
             text='右弯切入体育场路段，观众声浪在这里最响。'),
        dict(cs='T13-T15', name='球场内低速回旋（约 65 km/h）',
             text='被看台包围的极慢弯，牵引力和转向角是关键，也是全年最有画面感的一段。'),
        dict(cs='T16-T17', name='佩拉尔塔与回归发车线',
             text='出体育场后的加速弯，走线要正对终点直道。')],
    setup='空气稀薄让散热效率下降，涡轮与刹车通风口必须大幅扩充；即便装上最高下压力套件，实际阻力也只有蒙扎水平。',
    watch='看直道尾速为什么在低阻设定下依然不高（空气密度），以及棒球场段谁的车迷反应最热烈。'),

'interlagos': dict(
    round='R20', zh='圣保罗大奖赛', en='São Paulo Grand Prix',
    circuit_zh='英特拉格斯赛道', circuit_en='Autódromo José Carlos Pace, Interlagos',
    country='巴西', city='圣保罗', flag='🇧🇷', dates='11月06-08日', sprint=False,
    length=4.309, laps=71, left=10, right=5,
    record='1:10.540', record_who='V. Bottas', record_year=2018,
    downforce=('中高', 4), throttle=68, braking=('重度', 4), tyre=('高', 4),
    archetype='high-downforce', kind='专用赛道（逆时针）',
    intro='英特拉格斯是少数逆时针运行的赛道，对车手颈部是反向考验。它起伏大、弯角组合多变，'
          '而且天气说变就变，历史上无数次争冠悬念在这里的最后一段揭晓。',
    sectors=[
        dict(id='S1', rng=[1, 3], title='塞纳 S 弯',
             text='起跑下坡冲刺进 T1 下坡盲点左重刹，顺势扭入 T2 右弯再展开到 T3 太阳弯，'
                  '是全场最具视觉冲击的高速超车舞台。'),
        dict(id='S2', rng=[4, 11], title='逆时针内圈技术起伏群',
             text='Reta Oposta 直道后 T4 是下坡左发卡；随后进入狭窄盘旋的 T6-T7 费拉杜拉双右弯，'
                  'T8-T10 连续慢速发卡考验机械抓地力。'),
        dict(id='S3', rng=[12, 15], title='全油门上坡冲线',
             text='T12 容克弯出弯牵引力直接决定全圈生死；自此赛车全油门冲上陡峭的 T13-T15 连续上坡大弧度弯道直达终点线。')],
    corners_analysis=[
        dict(cs='T1', name='塞纳 S 弯入口',
             text='下坡加盲点，刹车点只能靠记忆。这里是全年最经典的高速超车起点。'),
        dict(cs='T2-T3', name='右弯接太阳弯',
             text='展开的大右弯，之后接 Reta Oposta 长直道。'),
        dict(cs='T4', name='下坡左发卡',
             text='直道末端的重刹慢弯，超车与失误同时高发。'),
        dict(cs='T6-T7', name='费拉杜拉双右弯',
             text='狭窄盘旋的两个右弯，逆时针布局让这里的横向力压在另一侧颈部。'),
        dict(cs='T8-T10', name='连续慢速发卡',
             text='低档位弯群，机械抓地力和出弯牵引力决定时间。'),
        dict(cs='T12', name='容克弯',
             text='出弯速度决定最后一段上坡直道，是整圈最关键的一次油门。'),
        dict(cs='T13-T15', name='上坡大弧度冲线弯',
             text='全油门上坡连续弯，底盘刮地声在这里最响。')],
    setup='逆时针高横向载荷压迫车手颈部肌肉；天气多变、超车窗口丰富，历来是争冠大戏的高潮地。',
    watch='看 T1 的高速内线尝试，以及雨天地面湿滑时谁敢在 T12 提前全油门。'),

'las-vegas': dict(
    round='R21', zh='拉斯维加斯大奖赛', en='Las Vegas Grand Prix',
    circuit_zh='拉斯维加斯街道赛道', circuit_en='Las Vegas Strip Circuit',
    country='美国', city='拉斯维加斯', flag='🇺🇸', dates='11月19-21日', sprint=False,
    length=6.201, laps=50, left=11, right=6,
    record='1:35.490', record_who='O. Piastri', record_year=2023,
    downforce=('最低', 1), throttle=78, braking=('极重', 5), tyre=('低', 2),
    archetype='speed-temple', kind='街道赛道（午夜低温）',
    intro='拉斯维加斯是全年最冷的赛道之一，午夜气温常常不足 15℃，轮胎很难进入工作温度。'
          '赛道沿赌城大道铺开，长直道极快、弯角极少，是典型的“尾速决定一切”。',
    sectors=[
        dict(id='S1', rng=[1, 4], title='围场区回旋',
             text='起跑大直道冲向 T1 的 180 度重刹左弯；T2-T4 是紧随其后的开阔变向加速段。'),
        dict(id='S2', rng=[5, 9], title='Sphere 巨球周边技术段',
             text='T5 重刹切入沉浸式建筑 The Sphere 外环，环绕进行 T6-T9 的中低速连贯变向。'),
        dict(id='S3', rng=[10, 17], title='1.9 公里赌城大道超级直道',
             text='穿过 T10-T11 后杀入著名的 Strip 大道直道，以超过 350 km/h 掠过百乐宫喷泉与凯撒宫；'
                  '在 T14 暴烈重刹，经 T16-T17 驶向终点。')],
    corners_analysis=[
        dict(cs='T1', name='180 度重刹左弯',
             text='发车直道末端的大角度弯，刹车点极晚才有超车机会。'),
        dict(cs='T2-T4', name='围场开阔变向段',
             text='路面宽阔，走线自由，主要看牵引力。'),
        dict(cs='T5', name='Sphere 入口重刹',
             text='绕向巨球建筑前的刹车区，是赛段 2 的节奏起点。'),
        dict(cs='T6-T9', name='中低速连贯变向',
             text='四个弯连成一串，低温下轮胎抓地力不足最容易在这里出事故。'),
        dict(cs='T10-T11', name='直道起点弯',
             text='出弯角度决定 1.9 公里直道的尾速，是超车链条的起点。'),
        dict(cs='T14', name='大道末端暴烈重刹',
             text='全年最重的刹车区之一，直道尾速超过 350 km/h，超车模式与电量博弈在这里见分晓。'),
        dict(cs='T16-T17', name='终点前收尾',
             text='最后两个弯，出弯要正对终点线。')],
    setup='午夜极低温让轮胎升温困难，暖胎圈和第一圈的表现被放大；低阻长直道让 2026 直道模式展现出恐怖的尾速。',
    watch='看谁能在低温下让轮胎进入工作区间，以及 T14 之前直道尾速的差距。'),

'lusail': dict(
    round='R22', zh='卡塔尔大奖赛', en='Qatar Grand Prix',
    circuit_zh='罗赛尔国际赛车场', circuit_en='Lusail International Circuit',
    country='卡塔尔', city='罗赛尔', flag='🇶🇦', dates='11月27-29日', sprint=False,
    length=5.419, laps=57, left=6, right=10,
    record='1:24.319', record_who='M. Verstappen', record_year=2023,
    downforce=('高', 5), throttle=68, braking=('中等', 3), tyre=('极高', 5),
    archetype='high-downforce', kind='专用赛道（轮胎地狱）',
    intro='罗赛尔是全年对轮胎最狠的赛道：一连串 200-240 km/h 的高速弯持续横撕胎壁，'
          '加上沙粒覆盖的路面，抓地力随时变化。车手身体和轮胎结构刚性同时被推到极限。',
    sectors=[
        dict(id='S1', rng=[1, 5], title='长直道与中速回环',
             text='1 公里长的主直道后 T1 重刹；随后进入极其宽阔、流动性极佳的 T2-T5 中速组合弯。'),
        dict(id='S2', rng=[6, 11], title='不间断高 G 值弯道群',
             text='T6 是紧凑弯角；随后 T7-T11 几乎由一连串以 200-240 km/h 掠过的高速弯组成，'
                  '横向 G 值持续维持在 4G 以上。'),
        dict(id='S3', rng=[12, 16], title='三联右弯与回场冲刺',
             text='著名的 T12-T14 三重高速连续右弯是轮胎剥离高危地带；T15-T16 顺畅过渡回主直道。')],
    corners_analysis=[
        dict(cs='T1', name='主直道末端重刹',
             text='1 公里直道之后的刹车区，超车机会明显但出口要给宽弯留位置。'),
        dict(cs='T2-T5', name='宽阔中速组合弯',
             text='路面宽、容错高，是这条赛道唯一能喘口气的段落。'),
        dict(cs='T6', name='紧凑过渡弯',
             text='节奏变化点，出弯角度决定高速弯群的入口。'),
        dict(cs='T7-T11', name='持续 4G 高速弯群',
             text='连续高速变向，横向载荷长期在 4G 以上，车手颈部和轮胎同时报警。'),
        dict(cs='T12-T14', name='三重高速右弯',
             text='三个相连右弯，轮胎外侧被反复剥离，是全年最容易爆胎起泡的路段。'),
        dict(cs='T15-T16', name='回场冲刺弯',
             text='顺畅过渡回主直道，出弯速度决定下一圈的直道尾速。')],
    setup='高下压力设定下的底盘吸地平稳性至关重要；轮胎结构刚性与胎压管理是全赛季最精细的工作。',
    watch='看谁的轮胎能撑到最后一组高速弯，以及正赛里进站窗口是否被胎泡打乱。'),

'yas-marina': dict(
    round='R23', zh='阿布扎比大奖赛', en='Abu Dhabi Grand Prix',
    circuit_zh='亚斯码头赛道', circuit_en='Yas Marina Circuit',
    country='阿联酋', city='阿布扎比', flag='🇦🇪', dates='12月04-06日', sprint=False,
    length=5.281, laps=58, left=9, right=7,
    record='1:26.103', record_who='M. Verstappen', record_year=2021,
    downforce=('中等', 3), throttle=65, braking=('重度', 4), tyre=('中等', 3),
    archetype='stop-and-go', kind='专用赛道（日落收官战）',
    intro='阿布扎比是赛季收官站，比赛在日落时分开始、夜间结束，地表温度会在正赛里持续下降。'
          '赛道布局改建后更流畅：长直道配重刹，加上第三赛段游艇码头的技术弯，考验的是全面性。',
    sectors=[
        dict(id='S1', rng=[1, 5], title='主看台直道与北看台高速段',
             text='T1 是 90 度左弯；T2-T3 全油门高速上坡穿梭；T5 宽阔发卡弯是主要重刹超车点。'),
        dict(id='S2', rng=[6, 8], title='双长大直道与减速弯',
             text='长达 1.2 公里的第一背直道狂飙，在 T6-T7 减速弯重刹超车；随后进入第二长直道冲向 T8 倾斜大弯。'),
        dict(id='S3', rng=[9, 16], title='游艇码头与总督酒店区',
             text='改建后流畅的 T9 大弧度中速弯；穿过豪华游艇码头与著名的酒店桥下'
                  '（T12-T15 连续中低速技术弯）；T16 回归发车大直道。')],
    corners_analysis=[
        dict(cs='T1', name='90 度左弯',
             text='发车后的第一个弯，刹车点决定第一圈的名次变化。'),
        dict(cs='T2-T3', name='上坡高速穿梭',
             text='带坡度的高速弯，车身负载变化快。'),
        dict(cs='T5', name='宽阔发卡（超车点）',
             text='赛段 1 的主要超越区，出口宽，可以强行占位。'),
        dict(cs='T6-T7', name='直道末端减速弯',
             text='1.2 公里直道之后的重刹，超车模式在这里最容易生效。'),
        dict(cs='T8', name='倾斜大弯',
             text='带倾角的长弯，靠赛道壁托住车身，出弯接第二直道。'),
        dict(cs='T9', name='大弧度中速弯',
             text='改建后的流畅点，走线越圆越省胎。'),
        dict(cs='T12-T15', name='酒店桥下技术弯群',
             text='桥洞下光线变化、路面温度更低，连续中低速弯考验机械抓地力。'),
        dict(cs='T16', name='收官弯',
             text='最后一个弯，出弯直接决定冠军归属的时刻往往就在这里。')],
    setup='日落黄昏战，地表温度从白昼骤降，赛车平衡会随比赛进行不断变化；'
          '兼顾长直道低风阻与第三赛段机械抓地力是收官战的胜负关键。',
    watch='注意比赛中后段赛道温度下降时谁还能保住前胎，以及最后一圈的保护性驾驶。'),
}
