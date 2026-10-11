/* ApexAtlas · router + pages */
(function () {
  'use strict';

  var view = document.getElementById('view');
  var navEl = document.getElementById('site-nav');
  var toggle = document.getElementById('nav-toggle');
  var esc = AA.esc;

  var ARCH = {
    'speed-temple': { zh: '极速殿堂型', color: 'var(--s3)' },
    'high-downforce': { zh: '高下压力流动型', color: 'var(--s1)' },
    'stop-and-go': { zh: '重刹牵引型', color: 'var(--s2)' },
    'street-precision': { zh: '狭窄街道技巧型', color: 'var(--overtake)' }
  };

  /* ---------- small helpers ---------- */
  function el(html) {
    var t = document.createElement('template');
    t.innerHTML = html.trim();
    return t.content.firstChild;
  }
  function loading(msg) {
    view.innerHTML = '<div class="loading"><div class="spinner"></div>' + esc(msg || '加载中…') + '</div>';
  }
  function fail(e) {
    view.innerHTML = '<section class="err fade"><h2>页面加载失败</h2><p>' + esc(e.message || e) +
      '</p><p>如果你在本地直接双击打开 <code>index.html</code>，浏览器会禁止读取数据文件。' +
      '请在项目目录下启动一个本地服务器（例如 <code>python -m http.server 8080</code>）后访问 ' +
      '<code>http://localhost:8080</code>。</p></section>';
  }
  function setTitle(s) { document.title = s ? (s + ' · ApexAtlas') : 'ApexAtlas · 2026 F1 赛道新手手册'; }
  function pips(n, max) {
    var out = '';
    for (var i = 1; i <= (max || 5); i++) out += '<span class="pip' + (i <= n ? ' on' : '') + '"></span>';
    return '<span class="pips">' + out + '</span>';
  }
  function archChip(id) {
    var a = ARCH[id] || { zh: id, color: 'var(--line-2)' };
    return '<span class="tagline"><span class="dot" style="background:' + a.color + '"></span>' + a.zh + '</span>';
  }

  /* ---------- header ---------- */
  function markNav(key) {
    Array.prototype.forEach.call(navEl.querySelectorAll('a'), function (a) {
      a.classList.toggle('on', a.dataset.nav === key);
    });
    navEl.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }
  toggle.addEventListener('click', function () {
    var open = navEl.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  navEl.addEventListener('click', function (e) {
    if (e.target.tagName === 'A') navEl.classList.remove('open');
  });

  /* ============================================================
     HOME
     ============================================================ */
  function pageHome() {
    loading();
    AA.season().then(function (S) {
      markNav('home');
      setTitle('');
      var ts = S.tracks;
      var sprints = ts.filter(function (t) { return t.sprint; }).length;
      var corners = ts.reduce(function (a, t) { return a + t.corners_total; }, 0);
      var longest = ts.reduce(function (a, t) { return t.length_km > a.length_km ? t : a; });
      var shortest = ts.reduce(function (a, t) { return t.length_km < a.length_km ? t : a; });

      view.innerHTML = '' +
        '<div class="hero fade">' +
          '<div class="hero-top">' +
            '<div>' +
              '<span class="eyebrow">FIA Formula 1 World Championship · 2026</span>' +
              '<h1>用一张赛道图，<em>看懂</em>一场比赛</h1>' +
              '<p class="lede" style="margin-top:16px">' + esc(S.season.intro) + '</p>' +
              '<div class="hero-stats">' +
                '<div class="stat"><b>' + S.season.rounds + '</b><span>场大奖赛</span></div>' +
                '<div class="stat"><b>' + sprints + '</b><span>含冲刺赛</span></div>' +
                '<div class="stat"><b>' + corners + '</b><span>可点击弯角</span></div>' +
                '<div class="stat"><b>' + esc(AA.km(longest.length_km)) + '</b><span>最长 ' + esc(longest.circuit_zh) + '</span></div>' +
                '<div class="stat"><b>' + esc(AA.km(shortest.length_km)) + '</b><span>最短 ' + esc(shortest.circuit_zh) + '</span></div>' +
              '</div>' +
            '</div>' +
            '<div class="cols-2" style="grid-template-columns:1fr">' +
              '<div class="note blue"><b>第一次看 F1？</b> 先花三分钟弄懂 2026 年的三个新变化：' +
              '主动空气动力学、电机功率翻倍、超车模式取代 DRS。' +
              '<div style="margin-top:10px"><a class="chip solid" style="background:var(--s2)" href="#/guide">阅读新手指南 →</a></div></div>' +
            '</div>' +
          '</div>' +
          '<div class="hero-strip"></div>' +
        '</div>' +

        '<section>' +
          '<div class="sec-head"><div><span class="eyebrow">Step 1</span><h2>先看懂地图上的符号</h2></div>' +
            '<a class="chip" href="#/guide">完整图例</a></div>' +
          '<div class="cols-2">' + legendMini(S.map_legend[0]) + legendMini(S.map_legend[1]) + legendMini(S.map_legend[2]) + '</div>' +
        '</section>' +

        '<section>' +
          '<div class="sec-head"><div><span class="eyebrow">Step 2</span><h2>2026 赛季 24 张赛道地图</h2></div></div>' +
          '<div class="filters" id="filters">' +
            '<button class="fchip" data-f="all" aria-pressed="true">全部</button>' +
            Object.keys(ARCH).map(function (k) {
              return '<button class="fchip" data-f="' + k + '" aria-pressed="false">' + ARCH[k].zh + '</button>';
            }).join('') +
            '<label class="search"><svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
              'stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4.2-4.2"/></svg>' +
              '<input id="q" type="search" placeholder="搜索赛道 / 国家 / 城市" aria-label="搜索赛道"></label>' +
          '</div>' +
          '<div class="grid" id="grid"></div>' +
        '</section>' +

        '<section>' +
          '<div class="sec-head"><div><span class="eyebrow">Step 3</span><h2>四类赛道，四种看法</h2></div></div>' +
          '<div class="sectors">' + S.archetypes.map(function (a) {
            return '<div class="sector" style="--sc:' + (ARCH[a.id] || {}).color + '">' +
              '<h3>' + esc(a.zh) + '</h3><div class="rng">' + esc(a.en) + '</div><p>' + esc(a.desc) + '</p>' +
              '<div class="td-chips" style="margin-top:12px">' + a.tracks.map(function (id) {
                var t = ts.filter(function (x) { return x.id === id; })[0];
                return t ? '<a class="chip" href="#/track/' + id + '">' + esc(t.circuit_zh) + '</a>' : '';
              }).join('') + '</div></div>';
          }).join('') + '</div>' +
        '</section>';

      function legendMini(item) {
        return '<div class="note"><b>' + esc(item.item) + '</b><br>' +
          esc(item.text.length > 96 ? item.text.slice(0, 96) + '…' : item.text) + '</div>';
      }

      var grid = document.getElementById('grid');
      var state = { f: 'all', q: '' };
      function render() {
        var q = state.q.trim().toLowerCase();
        grid.innerHTML = ts.filter(function (t) {
          if (state.f !== 'all' && t.archetype !== state.f) return false;
          if (!q) return true;
          return [t.name_zh, t.name_en, t.circuit_zh, t.circuit_en, t.country, t.city]
            .join(' ').toLowerCase().indexOf(q) >= 0;
        }).map(card).join('') || '<p class="lede">没有匹配的赛道，换个关键词试试。</p>';
      }
      function card(t) {
        return '<a class="tcard" href="#/track/' + t.id + '">' +
          '<div class="tcard-map"><span class="rn">' + esc(t.round) + '</span>' +
            '<img src="' + AA.url(t.thumb) + '" alt="' + esc(t.circuit_zh) + '赛道缩略图" loading="lazy"></div>' +
          '<div class="tcard-body">' +
            '<h3>' + t.flag + ' ' + esc(t.name_zh.replace(/大奖赛$/, '')) + '</h3>' +
            '<div class="tcard-sub">' + esc(t.circuit_zh) + ' · ' + esc(t.city) + '</div>' +
            '<p class="tcard-note">' + esc(t.intro_short) + '</p>' +
            '<div class="tcard-meta">' + archChip(t.archetype) +
              '<span class="chip">' + t.length_km.toFixed(3).replace(/0+$/, '').replace(/\.$/, '') + ' km</span>' +
              '<span class="chip">' + t.corners_total + ' 弯</span>' +
              (t.sprint ? '<span class="chip solid sprint">冲刺赛</span>' : '') +
            '</div>' +
          '</div></a>';
      }
      document.getElementById('filters').addEventListener('click', function (e) {
        var b = e.target.closest('.fchip');
        if (!b) return;
        state.f = b.dataset.f;
        Array.prototype.forEach.call(this.querySelectorAll('.fchip'), function (x) {
          x.setAttribute('aria-pressed', String(x === b));
        });
        render();
      });
      document.getElementById('q').addEventListener('input', function () { state.q = this.value; render(); });
      render();
    }).catch(fail);
  }

  /* ============================================================
     TRACK DETAIL
     ============================================================ */
  function pageTrack(id, focus) {
    loading();
    Promise.all([AA.track(id), AA.season()]).then(function (r) {
      var t = r[0], S = r[1];
      markNav('home');
      setTitle(t.circuit_zh);
      var list = S.tracks;
      var idx = list.findIndex(function (x) { return x.id === id; });
      var prev = idx > 0 ? list[idx - 1] : null;
      var next = idx >= 0 && idx < list.length - 1 ? list[idx + 1] : null;

      view.innerHTML = '' +
        '<div class="crumb"><a href="#/">← 2026 赛历总览</a></div>' +
        '<div class="td-head fade">' +
          '<div class="td-title"><span class="td-flag">' + t.flag + '</span>' +
            '<div><span class="eyebrow">' + esc(t.round === '—' ? '未列入本赛季赛历' : 'Round ' + t.round.replace('R', '')) +
            ' · ' + esc(t.kind) + '</span><h1>' + esc(t.name_zh) + '</h1></div></div>' +
          '<div class="td-names">' + esc(t.circuit_zh) + ' · ' + esc(t.circuit_en) +
            ' · ' + esc(t.country) + esc(t.city) + '</div>' +
          '<div class="td-chips">' +
            '<span class="chip round">' + esc(t.dates) + '</span>' +
            '<span class="chip">' + t.length_km.toFixed(3) + ' km</span>' +
            '<span class="chip">' + t.laps + ' 圈</span>' +
            '<span class="chip">' + t.corners.total + ' 个弯角</span>' +
            (t.sprint ? '<span class="chip solid sprint">冲刺赛周末</span>' : '') +
            archChip(t.archetype) +
          '</div>' +
          '<p class="td-intro">' + esc(t.intro) + '</p>' +
        '</div>' +

        '<section style="margin-top:26px">' +
          '<div class="td-main">' +
            '<div>' +
              '<div class="map-card">' +
                '<div id="stage"></div>' +
                '<div class="map-tools">' +
                  '<button class="fchip" data-sec="" aria-pressed="true">全部赛段</button>' +
                  ['S1', 'S2', 'S3'].map(function (s, i) {
                    return '<button class="fchip" data-sec="' + s + '" aria-pressed="false">' +
                      '<span class="dot" style="background:var(--s' + (i + 1) + ');display:inline-block"></span> ' +
                      'Sector ' + (i + 1) + '</button>';
                  }).join('') +
                  '<button class="fchip legend-toggle" id="lg" aria-expanded="false">图例</button>' +
                '</div>' +
                '<ul class="legend" id="legend" hidden>' + legendItems(S.map_legend) + '</ul>' +
              '</div>' +
              '<p class="panel-hint" style="border:0;padding-top:8px">点击地图上的弯角气泡查看解析；' +
                '键盘可用 ← → 逐个弯角浏览。</p>' +
            '</div>' +
            '<aside class="panel" id="panel" aria-live="polite"></aside>' +
          '</div>' +
        '</section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">Data</span><h2>赛道规格与负荷</h2></div></div>' +
          specBlock(t) + '</section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">Sectors</span><h2>三大赛段拆解</h2></div></div>' +
          '<div class="sectors">' + t.sectors.map(function (s, i) {
            return '<div class="sector" style="--sc:var(--s' + (i + 1) + ')">' +
              '<h3>Sector ' + (i + 1) + ' · ' + esc(s.title) + '</h3>' +
              '<div class="rng">T' + s.rng[0] + ' — T' + s.rng[1] + ' · 共 ' + s.corners.length + ' 个弯角</div>' +
              '<p>' + esc(s.text) + '</p>' +
              '<div style="margin-top:12px"><button class="fchip" data-jump="' + s.id + '">在地图上高亮</button></div>' +
            '</div>';
          }).join('') + '</div></section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">Corners</span><h2>弯角解析</h2></div>' +
          '<span class="chip">' + t.corner_groups.length + ' 组</span></div>' +
          '<div class="clist" id="clist">' + t.corner_groups.map(function (g, i) {
            return '<button class="crow" data-g="' + i + '">' +
              '<span class="code">' + esc(g.cs) + '<i>' + (g.sector || '') + '</i></span>' +
              '<span><h4>' + esc(g.name) + '</h4><p>' + esc(g.text) + '</p></span></button>';
          }).join('') + '</div></section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">2026</span><h2>新规下的调校与看点</h2></div></div>' +
          '<div class="cols-2">' +
            '<div class="note"><b>关键调校</b><br>' + esc(t.setup_2026) + '</div>' +
            '<div class="note green"><b>新手看点</b><br>' + esc(t.watch) + '</div>' +
          '</div></section>' +

        '<div class="pager">' +
          (prev ? '<a href="#/track/' + prev.id + '"><span>上一站 ' + esc(prev.round) + '</span><b>' + esc(prev.circuit_zh) + '</b></a>' : '<span></span>') +
          (next ? '<a class="next" href="#/track/' + next.id + '"><span>下一站 ' + esc(next.round) + '</span><b>' + esc(next.circuit_zh) + '</b></a>' : '<span></span>') +
        '</div>';

      function legendItems(items) {
        var marks = {
          '赛段配色（中线）': '<span style="display:block;height:4px;border-radius:2px;background:linear-gradient(90deg,var(--s1) 0 33%,var(--s2) 0 66%,var(--s3) 0)"></span>',
          '圆圈里的数字': '<span style="display:inline-block;width:16px;height:16px;border-radius:50%;border:1.5px solid #0d0d14;background:#f7f4f1"></span>',
          '红色虚线段': '<span style="display:block;height:0;border-top:3px dashed var(--straight)"></span>',
          '绿色圆点（两点一组）': '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--overtake)"></span>',
          '黄色圆点 + SPEED TRAP': '<span style="display:inline-block;width:12px;height:12px;border-radius:50%;background:var(--s2)"></span>',
          '黑白方格': '<span style="display:block;height:12px;background:repeating-conic-gradient(#0d0d14 0 25%,#f7f4f1 0 50%) 0 0/6px 6px"></span>'
        };
        return items.map(function (x) {
          return '<li><span class="k">' + (marks[x.item] || '') + '</span><span><b>' + esc(x.item) + '</b> — ' + esc(x.text) + '</span></li>';
        }).join('');
      }

      function specBlock(t) {
        var m = t.metrics;
        var rec = t.record
          ? '<div class="spec"><div class="lab">圈速纪录</div><div class="val">' + esc(t.record.time) +
            '</div><div class="sub">' + esc(t.record.driver) + ' · ' + t.record.year + '</div></div>'
          : '<div class="spec"><div class="lab">圈速纪录</div><div class="val"><small>指南未收录</small></div>' +
            '<div class="sub">本站无官方数据章节</div></div>';
        var lr = (t.corners.left == null) ? ('地图按 ' + t.corners.total + ' 个编号弯绘制（官方未公布左右分配）') :
          (t.corners.left + ' 左 / ' + t.corners.right + ' 右');
        return '<div class="spec-grid">' +
            '<div class="spec"><div class="lab">单圈长度</div><div class="val">' + t.length_km.toFixed(3) +
              ' <small>km</small></div><div class="sub">' + t.laps + ' 圈 · 全程约 ' +
              (t.length_km * t.laps).toFixed(1) + ' km</div></div>' +
            '<div class="spec"><div class="lab">弯角数量</div><div class="val">' + t.corners.total +
              ' <small>个</small></div><div class="sub">' + esc(lr) + '</div></div>' +
            rec +
            '<div class="spec"><div class="lab">正赛距离</div><div class="val">' +
              Math.round(t.length_km * t.laps) + ' <small>km</small></div><div class="sub">' + esc(t.dates) + '</div></div>' +
          '</div>' +
          '<div class="meters" style="margin-top:16px">' +
            meter('全油门比例', '<div class="bar s3"><i style="width:' + m.throttle_pct + '%"></i></div>' +
              '<div class="lab"><span>踩满油门的时间占比</span><b>' + m.throttle_pct + '%</b></div>', true) +
            meter('下压力设定', '<div class="bar s1"><i style="width:' + (m.downforce[1] * 20) + '%"></i></div>' +
              '<div class="lab"><span>' + esc(m.downforce[0]) + '</span>' + pips(m.downforce[1]) + '</div>', true) +
            meter('制动负荷', '<div class="bar acc"><i style="width:' + (m.braking[1] * 20) + '%"></i></div>' +
              '<div class="lab"><span>' + esc(m.braking[0]) + '</span>' + pips(m.braking[1]) + '</div>', true) +
            meter('轮胎磨损', '<div class="bar s2"><i style="width:' + (m.tyre_wear[1] * 20) + '%"></i></div>' +
              '<div class="lab"><span>' + esc(m.tyre_wear[0]) + '</span>' + pips(m.tyre_wear[1]) + '</div>', true) +
          '</div>';
      }
      function meter(title, body, labelAfter) {
        return '<div class="meter"><div class="lab"><b style="color:var(--text)">' + esc(title) + '</b></div>' + body + '</div>';
      }

      /* ---- wiring ---- */
      var panel = document.getElementById('panel');
      var map = AAMap.create(t, document.getElementById('stage'), { onPick: showGroup });
      var sel = { g: null, n: null };

      function showGroup(gi, n) {
        sel = { g: gi, n: n };
        Array.prototype.forEach.call(document.querySelectorAll('.crow'), function (row) {
          row.classList.toggle('on', gi != null && +row.dataset.g === gi);
        });
        if (gi == null) { transitionPanel(n); return; }
        var g = t.corner_groups[gi];
        var sec = t.sectors.filter(function (s) { return s.id === g.sector; })[0];
        var order = t.corner_groups.map(function (x, i) { return i; });
        panel.innerHTML = '<div class="panel-kicker">弯角解析' + (sec ? ' · Sector ' + sec.id.slice(1) : '') + '</div>' +
          '<h3>' + esc(g.name) + '</h3>' +
          '<div class="codes">' + g.codes.map(function (c) {
            var h = map.byCode[c];
            return '<span class="chip solid ' + ((h && h.sector) || '').toLowerCase() + '">T' + esc(c) + '</span>';
          }).join('') + '</div>' +
          '<p>' + esc(g.text) + '</p>' +
          (sec ? '<p class="panel-hint">所在赛段：Sector ' + sec.id.slice(1) + ' · ' + esc(sec.title) +
                 '<br>' + esc(sec.text) + '</p>' : '') +
          '<div class="panel-nav"><button id="pnav-prev">← 上一组</button><button id="pnav-next">下一组 →</button></div>';
        var gi2 = order.indexOf(gi);
        document.getElementById('pnav-prev').disabled = gi2 <= 0;
        document.getElementById('pnav-next').disabled = gi2 >= order.length - 1;
        document.getElementById('pnav-prev').onclick = function () { jumpGroup(order[gi2 - 1]); };
        document.getElementById('pnav-next').onclick = function () { jumpGroup(order[gi2 + 1]); };
      }
      function hintPanel() {
        panel.innerHTML = '<div class="panel-kicker">怎么用</div><h3>点一个弯角试试</h3>' +
          '<p>地图上的每个数字都是一个可点击的弯角。选中后会在这里显示它的位置、所属赛段和解析。</p>' +
          '<p class="panel-hint">这一站共有 ' + t.corner_groups.length + ' 组弯角解析、' + t.hotspots.length + ' 个编号弯角。</p>';
      }
      function transitionPanel(n) {
        var h = map.byCode[n];
        if (!h) { hintPanel(); return; }
        var sec = t.sectors.filter(function (s) { return s.id === h.sector; })[0];
        panel.innerHTML = '<div class="panel-kicker">弯角定位' + (sec ? ' · Sector ' + sec.id.slice(1) : '') + '</div>' +
          '<h3>T' + esc(h.n) + ' · 未单列解析的弯角</h3>' +
          '<div class="codes"><span class="chip solid ' + String(h.sector).toLowerCase() + '">T' + esc(h.n) + '</span></div>' +
          '<p>这个编号在地图上独立标注，也已为你点亮，但本站的逐弯解析以“弯角组”为单位，它没有落进任何一组的文字卡片里，' +
          '所以这里只显示它的坐标与所属赛段，不额外编造技术结论。</p>' +
          (sec ? '<p class="panel-hint">所在赛段：Sector ' + sec.id.slice(1) + ' · ' + esc(sec.title) +
                 '<br>' + esc(sec.text) + '</p>' : '') +
          '<p class="panel-hint">用键盘 ← → 可以按顺序跳过整圈 ' + t.hotspots.length + ' 个编号弯角，或在下方列表挑选有解析的 ' + t.corner_groups.length + ' 组。</p>';
      }
      function jumpGroup(gi) {
        var g = t.corner_groups[gi];
        if (!g) return;
        map.pick(gi, g.codes[0]);
        var row = document.querySelector('.crow[data-g="' + gi + '"]');
        if (row) row.scrollIntoView({ block: 'center', behavior: 'smooth' });
      }

      document.getElementById('clist').addEventListener('click', function (e) {
        var row = e.target.closest('.crow');
        if (row) jumpGroup(+row.dataset.g);
      });
      Array.prototype.forEach.call(view.querySelectorAll('[data-jump]'), function (b) {
        b.addEventListener('click', function () {
          var tools = view.querySelector('.map-tools');
          var target = tools.querySelector('[data-sec="' + b.dataset.jump + '"]');
          if (target) target.click();
          document.querySelector('.map-card').scrollIntoView({ block: 'center', behavior: 'smooth' });
        });
      });

      /* sector highlight buttons */
      var tools = view.querySelector('.map-tools');
      tools.addEventListener('click', function (e) {
        var b = e.target.closest('[data-sec]');
        if (!b) return;
        Array.prototype.forEach.call(tools.querySelectorAll('[data-sec]'), function (x) {
          x.setAttribute('aria-pressed', String(x === b));
        });
        map.setSector(b.dataset.sec || null);
      });
      var lg = document.getElementById('lg');
      lg.addEventListener('click', function () {
        var box = document.getElementById('legend');
        var open = box.hasAttribute('hidden');
        if (open) { box.removeAttribute('hidden'); } else { box.setAttribute('hidden', ''); }
        lg.setAttribute('aria-expanded', String(open));
      });

      /* keyboard: ← → through corners */
      function onKey(e) {
        if (e.target.matches('input, select, textarea')) return;
        if (e.key === 'ArrowRight') { map.step(1); e.preventDefault(); }
        if (e.key === 'ArrowLeft') { map.step(-1); e.preventDefault(); }
      }
      document.addEventListener('keydown', onKey);
      window.__aaCleanup = function () { document.removeEventListener('keydown', onKey); };

      hintPanel();
      if (focus) {
        var gi = t.corner_groups.findIndex(function (g) {
          return g.cs.replace(/^T/, '') === focus || g.codes.indexOf(focus) >= 0;
        });
        if (gi >= 0) {
          var g = t.corner_groups[gi];
          map.pick(gi, focus);
          showGroup(gi, focus);
        }
      }
    }).catch(fail);
  }

  /* ============================================================
     GUIDE
     ============================================================ */
  function pageGuide() {
    loading();
    AA.season().then(function (S) {
      markNav('guide');
      setTitle('新手指南');
      var cats = ['全部'].concat(S.glossary.map(function (g) { return g.cat; })
        .filter(function (v, i, a) { return a.indexOf(v) === i; }));

      view.innerHTML = '' +
        '<div class="hero fade" style="padding-bottom:6px">' +
          '<span class="eyebrow">Beginner guide · 2026</span>' +
          '<h1>三分钟搞懂 2026 的新规则</h1>' +
          '<p class="lede" style="margin-top:14px">2026 是 F1 规则大改的一年。下面这五条解释了你在新赛季转播里' +
          '会反复听到的名词，也解释了为什么每条赛道的取舍变得不一样。</p>' +
        '</div>' +
        '<section style="margin-top:26px">' +
          S.rules.map(function (r, i) {
            return '<div class="acc" data-open="' + (i === 0) + '">' +
              '<button aria-expanded="' + (i === 0) + '"><span class="t">' + esc(r.title) + '</span>' +
              '<span class="s">' + esc(r.short) + '</span><span class="caret">›</span></button>' +
              '<div class="body"><p>' + esc(r.body) + '</p></div></div>';
          }).join('') +
        '</section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">How to read</span><h2>怎么看一张赛道地图</h2></div></div>' +
          '<div class="tbl-wrap"><table class="tbl"><thead><tr><th style="width:180px">图上元素</th><th>含义与用途</th></tr></thead><tbody>' +
          S.map_legend.map(function (x) {
            return '<tr><td><b>' + esc(x.item) + '</b></td><td>' + esc(x.text) + '</td></tr>';
          }).join('') + '</tbody></table></div></section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">What to watch</span><h2>2026 观赛三个着力点</h2></div></div>' +
          '<div class="sectors">' + S.watch_tips.map(function (x, i) {
            return '<div class="sector" style="--sc:var(--s' + ((i % 3) + 1) + ')"><h3>' + esc(x.title) + '</h3>' +
              '<div class="rng">Tip ' + (i + 1) + '</div><p>' + esc(x.text) + '</p></div>';
          }).join('') + '</div></section>' +

        '<section><div class="sec-head"><div><span class="eyebrow">Glossary</span><h2>术语速查</h2></div></div>' +
          '<div class="filters" id="gfilter">' + cats.map(function (c, i) {
            return '<button class="fchip" data-c="' + esc(c) + '" aria-pressed="' + (i === 0) + '">' + esc(c) + '</button>';
          }).join('') + '</div>' +
          '<div class="tbl-wrap"><table class="tbl"><thead><tr><th style="width:150px">术语</th>' +
          '<th style="width:190px">英文</th><th>含义</th></tr></thead><tbody id="gtbody"></tbody></table></div></section>';

      var tbody = document.getElementById('gtbody');
      function draw(cat) {
        tbody.innerHTML = S.glossary.filter(function (g) {
          return cat === '全部' || g.cat === cat;
        }).map(function (g) {
          return '<tr><td><b>' + esc(g.term) + '</b></td><td style="color:var(--muted)">' + esc(g.en) +
            '</td><td>' + esc(g.text) + '</td></tr>';
        }).join('');
      }
      document.getElementById('gfilter').addEventListener('click', function (e) {
        var b = e.target.closest('.fchip');
        if (!b) return;
        Array.prototype.forEach.call(this.querySelectorAll('.fchip'), function (x) {
          x.setAttribute('aria-pressed', String(x === b));
        });
        draw(b.dataset.c);
      });
      draw('全部');

      Array.prototype.forEach.call(view.querySelectorAll('.acc > button'), function (b) {
        b.addEventListener('click', function () {
          var acc = b.parentNode;
          var open = acc.getAttribute('data-open') === 'true';
          acc.setAttribute('data-open', String(!open));
          b.setAttribute('aria-expanded', String(!open));
        });
      });
    }).catch(fail);
  }

  /* ============================================================
     COMPARE
     ============================================================ */
  function pageCompare(ids) {
    loading();
    AA.season().then(function (S) {
      markNav('compare');
      setTitle('赛道对比');
      var chosen = (ids && ids.length ? ids : ['monza', 'monaco', 'suzuka']).slice(0, 3);
      // 选择框固定为三个：分享链接里不足三条时用未选中的赛道补齐
      var fallbacks = ['monza', 'monaco', 'suzuka', 'baku', 'silverstone'];
      while (chosen.length < 3) {
        var spare = fallbacks.filter(function (x) { return chosen.indexOf(x) < 0; })[0] ||
          S.tracks.filter(function (t) { return chosen.indexOf(t.id) < 0; })[0].id;
        chosen.push(spare);
      }
      var byId = {};
      S.tracks.forEach(function (t) { byId[t.id] = t; });

      view.innerHTML = '' +
        '<div class="hero fade" style="padding-bottom:0"><span class="eyebrow">Compare</span>' +
        '<h1>把两三站放在一起看</h1>' +
        '<p class="lede" style="margin-top:12px">同一条赛道在不同规则下的取舍完全不同。选 2-3 站，' +
        '直接比较长度、弯角数量与三项负荷，理解“为什么每站的设定不一样”。</p></div>' +
        '<section style="margin-top:22px"><div class="picker" id="picker"></div><div class="cmp" id="cmp"></div></section>';

      var picker = document.getElementById('picker');
      var cmp = document.getElementById('cmp');

      function options(sel, i) {
        return '<select data-i="' + i + '" aria-label="第 ' + (i + 1) + ' 条赛道">' +
          S.tracks.map(function (t) {
            return '<option value="' + t.id + '"' + (t.id === sel ? ' selected' : '') + '>' +
              t.flag + ' ' + esc(t.circuit_zh) + '</option>';
          }).join('') + '</select>';
      }
      function sync() {
        picker.innerHTML = chosen.map(options).join('') +
          '<a class="chip" href="#/compare/' + chosen.join(',') + '">生成可分享链接</a>';
        Promise.all(chosen.map(function (id) { return AA.track(id); })).then(function (list) {
          cmp.innerHTML = list.map(col).join('');
        });
      }
      function maxOf(key) {
        return Math.max.apply(null, list_cache.map(function (t) { return key(t); }));
      }
      var list_cache = [];
      function col(t) {
        return '<div class="cmp-col"><div class="top"><a href="#/track/' + t.id + '">' +
          '<img src="' + AA.url(t.map.thumb) + '" alt="' + esc(t.circuit_zh) + '"></a></div>' +
          '<div class="nm"><h3>' + t.flag + ' ' + esc(t.circuit_zh) + '</h3>' +
          '<div class="tcard-sub">' + esc(t.round) + ' · ' + esc(t.kind) + '</div></div>' +
          '<dl>' +
          row('单圈长度', t.length_km.toFixed(3) + ' km', t.length_km / 7.004 * 100, 'var(--s3)') +
          row('弯角数', t.corners.total + ' 个', t.corners.total / 27 * 100, 'var(--s1)') +
          row('比赛圈数', String(t.laps), t.laps / 78 * 100, 'var(--s2)') +
          row('全油门', t.metrics.throttle_pct + '%', t.metrics.throttle_pct, 'var(--s3)') +
          row('下压力', esc(t.metrics.downforce[0]), t.metrics.downforce[1] * 20, 'var(--s1)') +
          row('制动负荷', esc(t.metrics.braking[0]), t.metrics.braking[1] * 20, 'var(--straight)') +
          row('轮胎磨损', esc(t.metrics.tyre_wear[0]), t.metrics.tyre_wear[1] * 20, 'var(--s2)') +
          '<div class="row"><dt>流派</dt><dd style="text-align:left">' + archChip(t.archetype) + '</dd></div>' +
          '</dl></div>';
      }
      function row(label, val, w, color) {
        return '<div class="row"><dt>' + label + '</dt><dd>' + val + '</dd>' +
          '<div style="grid-column:1/-1"><div class="bar"><i style="width:' + Math.min(100, w).toFixed(0) +
          '%;background:' + color + '"></i></div></div></div>';
      }
      picker.addEventListener('change', function (e) {
        if (e.target.tagName !== 'SELECT') return;
        chosen[+e.target.dataset.i] = e.target.value;
        sync();
      });
      sync();
    }).catch(fail);
  }

  /* ============================================================
     DATA / SOURCES
     ============================================================ */
  function pageData() {
    loading();
    AA.season().then(function (S) {
      markNav('data');
      setTitle('数据说明');
      var d = S.data_sources;
      view.innerHTML = '' +
        '<div class="hero fade" style="padding-bottom:0"><span class="eyebrow">Method · 更新于 ' + esc(d.updated) + '</span>' +
        '<h1>数据从哪里来，哪里可能有出入</h1></div>' +
        '<section style="margin-top:22px"><div class="sec-head"><div><h2>来源</h2></div></div>' +
          '<div class="tbl-wrap"><table class="tbl"><tbody>' + d.items.map(function (x) {
            return '<tr><td style="width:38%"><b>' + esc(x.src) + '</b></td><td>' + esc(x.used) + '</td></tr>';
          }).join('') + '</tbody></table></div></section>' +
        '<section><div class="sec-head"><div><h2>需要知道的边界</h2></div></div>' +
          '<div class="clist">' + d.notes.map(function (n) {
            return '<div class="note" style="width:100%">' + esc(n) + '</div>';
          }).join('') + '</div></section>' +
        '<section><div class="sec-head"><div><h2>怎么自己加一条赛道</h2></div></div>' +
          '<div class="cols-2"><div class="note"><b>只改数据，不改代码</b><br>' +
          '把新地图放进 <code>assets/maps/</code>，按同样格式在 <code>data/tracks/</code> 增加一个 JSON：' +
          'hotspots 里的 x/y 是弯角气泡中心相对图片宽高的百分比，corner_groups 用 codes 数组把弯角编号和文字对应起来。' +
          '最后在 <code>data/season.json</code> 的 tracks 列表补一条索引即可。</div>' +
          '<div class="note blue"><b>坐标怎么来的</b><br>' +
          '本项目的弯角坐标由 <code>tools/</code> 下的脚本从地图自动识别（数字气泡定位），' +
          '再逐站核对编号连续性后生成。仓库保留了脚本，方便你换新地图时重新提取。</div></div></section>';
    }).catch(fail);
  }

  /* ============================================================
     ROUTER
     ============================================================ */
  function route() {
    if (window.__aaCleanup) { window.__aaCleanup(); window.__aaCleanup = null; }
    var h = location.hash.replace(/^#\/?/, '');
    var parts = h.split('/').filter(Boolean);
    window.scrollTo(0, 0);
    if (!parts.length) return pageHome();
    if (parts[0] === 'track' && parts[1]) return pageTrack(parts[1], parts[2] || null);
    if (parts[0] === 'guide') return pageGuide();
    if (parts[0] === 'compare') return pageCompare(parts[1] ? parts[1].split(',') : null);
    if (parts[0] === 'data') return pageData();
    view.innerHTML = '<section class="err fade" style="margin-top:60px"><h2>没找到这个页面</h2>' +
      '<p>地址 <code>#/' + esc(h) + '</code> 不存在。</p><p><a class="chip solid" style="background:var(--s2)" href="#/">回到赛历总览</a></p></section>';
    setTitle('页面不存在');
  }
  window.addEventListener('hashchange', route);
  route();
})();
