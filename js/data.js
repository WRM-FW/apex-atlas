/* ApexAtlas · data access
   All paths are resolved relative to the deployed directory so the site works
   both at a domain root and under a username.github.io/repo/ sub-path. */
(function (global) {
  'use strict';

  function baseUrl() {
    var p = location.pathname;
    if (p.charAt(p.length - 1) === '/') return p;
    return p.slice(0, p.lastIndexOf('/') + 1);
  }
  var BASE = baseUrl();

  function url(rel) {
    return BASE + String(rel).replace(/^\.?\//, '');
  }

  var cache = {};
  function getJSON(rel) {
    if (cache[rel]) return cache[rel];
    cache[rel] = fetch(url(rel), { cache: 'force-cache' })
      .then(function (r) {
        if (!r.ok) throw new Error('HTTP ' + r.status + ' · ' + rel);
        return r.json();
      })
      .catch(function (e) {
        delete cache[rel];
        e.message = (e instanceof TypeError)
          ? '无法读取 ' + rel + '（本地预览请通过 HTTP 打开，见 README）'
          : e.message;
        throw e;
      });
    return cache[rel];
  }

  function season() { return getJSON('data/season.json'); }
  function track(id) { return getJSON('data/tracks/' + id + '.json'); }

  var esc = function (s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
  };

  function km(n) { return Number(n).toFixed(3).replace(/0+$/, '').replace(/\.$/, '') + ' km'; }
  function pct(n) { return n + '%'; }

  global.AA = {
    BASE: BASE, url: url, season: season, track: track,
    esc: esc, km: km, pct: pct
  };
})(window);
