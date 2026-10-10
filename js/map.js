/* ApexAtlas · interactive track map
   Places a clickable hotspot on every corner bubble of the supplied map.
   Coordinates are stored as percentages of the artwork, so the overlay stays
   aligned at any rendered size. */
(function (global) {
  'use strict';

  var SECTOR_NAME = { S1: 'Sector 1', S2: 'Sector 2', S3: 'Sector 3' };

  function create(track, mount, opts) {
    opts = opts || {};
    var byCode = {};
    track.hotspots.forEach(function (h) { byCode[h.n] = h; });

    mount.className = 'map-stage';
    mount.innerHTML = '';

    var img = document.createElement('img');
    img.className = 'base';
    img.src = AA.url(track.map.file);
    img.alt = track.circuit_zh + '赛道地图（含 ' + track.hotspots.length + ' 个弯角编号与三段赛段配色）';
    img.loading = 'lazy';
    mount.appendChild(img);

    var dim = document.createElement('img');
    dim.className = 'dim';
    dim.alt = '';
    dim.setAttribute('aria-hidden', 'true');
    mount.appendChild(dim);

    var tip = document.createElement('div');
    tip.className = 'map-tip';
    tip.setAttribute('aria-hidden', 'true');
    mount.appendChild(tip);

    var nodes = {};
    track.hotspots.forEach(function (h) {
      var b = document.createElement('button');
      b.type = 'button';
      b.className = 'hs';
      b.style.left = h.x + '%';
      b.style.top = h.y + '%';
      var g = h.group == null ? null : track.corner_groups[h.group];
      b.setAttribute('aria-label', '弯角 ' + h.n + (g ? '：' + g.name : ''));
      b.dataset.n = h.n;
      b.addEventListener('click', function () { pick(h.group, h.n); });
      b.addEventListener('mouseenter', function () { showTip(h, g); });
      b.addEventListener('focus', function () { showTip(h, g); });
      b.addEventListener('mouseleave', hideTip);
      b.addEventListener('blur', hideTip);
      mount.appendChild(b);
      nodes[h.n] = b;
    });

    function showTip(h, g) {
      tip.textContent = 'T' + h.n + (g ? ' · ' + g.name : '');
      tip.style.left = h.x + '%';
      tip.style.top = h.y + '%';
      tip.classList.add('on');
    }
    function hideTip() { tip.classList.remove('on'); }

    var current = { group: null, n: null };

    function pick(groupIdx, n) {
      current.group = groupIdx;
      current.n = n;
      Object.keys(nodes).forEach(function (k) {
        nodes[k].classList.remove('on', 'in-group');
      });
      if (groupIdx != null) {
        track.corner_groups[groupIdx].codes.forEach(function (c) {
          if (nodes[c]) nodes[c].classList.add('in-group');
        });
      }
      if (nodes[n]) nodes[n].classList.add('on');
      if (opts.onPick) opts.onPick(groupIdx, n);
    }

    /* jump to the previous / next corner on the map (arrow keys) */
    function step(dir) {
      var order = track.hotspots.map(function (h) { return h.n; });
      var i = current.n == null ? -1 : order.indexOf(current.n);
      i = (i + dir + order.length) % order.length;
      var h = track.hotspots[i];
      pick(h.group, h.n);
      if (nodes[h.n]) nodes[h.n].focus();
    }

    /* sector focus: prefer a pre-rendered dim layer, fall back to fading markers */
    var dimTried = {};
    function setSector(id) {
      if (!id) {
        mount.classList.remove('dimmed');
        dim.removeAttribute('src');
        Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove('off'); });
        return;
      }
      var key = track.id + '_' + id;
      if (dimTried[key] === false) {
        Object.keys(byCode).forEach(function (k) {
          var on = byCode[k].sector === id;
          nodes[k].classList.toggle('off', !on);
          nodes[k].classList.toggle('in-group', on);
        });
        mount.classList.remove('dimmed');
        return;
      }
      var src = AA.url('assets/dim/' + track.id + '_' + id + '.webp');
      dim.onload = function () {
        dimTried[key] = true;
        mount.classList.add('dimmed');
      };
      dim.onerror = function () {
        dimTried[key] = false;
        setSector(id);
      };
      dim.src = src;
    }

    function clearMarks() {
      Object.keys(nodes).forEach(function (k) { nodes[k].classList.remove('on', 'in-group', 'off'); });
      current = { group: null, n: null };
    }

    return {
      el: mount, pick: pick, step: step, setSector: setSector,
      clearMarks: clearMarks, nodes: nodes, byCode: byCode
    };
  }

  global.AAMap = { create: create, SECTOR_NAME: SECTOR_NAME };
})(window);
