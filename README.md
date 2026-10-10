# ApexAtlas · 2026 F1 赛道新手手册

用 2026 赛季官方风格赛道地图，带 F1 新手逐弯看懂每条赛道的布局、赛段特性与关键数据。

**在线地址：** https://wrm-fw.github.io/apex-atlas/

纯前端静态站点：原生 HTML / CSS / JavaScript + JSON 数据，没有构建步骤、没有后端。

---

## 1. 这个站点做什么

| 页面 | 地址 | 内容 |
| --- | --- | --- |
| 赛历总览 | `#/` | 24 张赛道地图卡片，可按四大流派筛选、按名称/国家/城市搜索 |
| 赛道详情 | `#/track/<id>` | 可点击弯角热点的地图、赛段高亮、规格与负荷数据、三大赛段拆解、逐组弯角解析 |
| 新手指南 | `#/guide` | 2026 五项新规、怎么读一张赛道地图、观赛三个着力点、术语速查表 |
| 赛道对比 | `#/compare` | 任选 2–3 站并排比较长度、弯角数、全油门比例与三项负荷 |
| 数据说明 | `#/data` | 数据来源、口径差异说明、如何自己新增赛道 |

核心交互：**地图上每个弯角气泡都是一个按钮**，点击后右侧面板给出该弯（或该组弯）的解析与所属赛段；
`←` `→` 方向键可逐个弯角浏览；点击 Sector 1/2/3 会把该赛段"打亮"、其余部分压暗（预生成的透明遮罩层）。

## 2. 目录结构

```
index.html              单页外壳（hash 路由）
css/app.css             设计系统与全部组件样式
js/data.js              路径解析 + JSON 加载缓存
js/map.js               赛道地图交互组件（热点 / 提示 / 赛段遮罩）
js/app.js               路由与五个页面
data/season.json        赛历索引、新规、流派分类、图例、术语表、数据说明
data/tracks/<id>.json   每站一个文件：规格 + 赛段 + 弯角解析 + 热点坐标
assets/maps/            赛道地图 WebP（1600px）与缩略图（640px）
assets/dim/             每站每赛段的压暗遮罩层（赛段高亮用）
tools/check_site.py     发布前校验（CI 每次都会跑）
tools/extract/          弯角坐标自动提取与数据生成脚本（维护用，不部署）
```

## 3. 本地预览

浏览器不允许 `file://` 读取 JSON，所以要用一个本地服务器：

```bash
cd apex-atlas
python -m http.server 8080
# 浏览器打开 http://localhost:8080
```

发布前自检（可选，CI 会自动执行）：

```bash
python tools/check_site.py .
```

## 4. 部署到 GitHub Pages（人工审核后发布）

发布流程是 **Pull Request 审核 → 合并 main → 自动部署**，任何改动都必须先经过人工 review 才会上线。

### 4.1 一次性准备（本仓库已完成）

1. 仓库 Settings → Pages → **Build and deployment → Source: GitHub Actions**。
   命令行等价操作：
   ```bash
   gh api -X PATCH repos/WRM-FW/apex-atlas/pages -f build_type=workflow
   ```
2. 分支保护，确保 `main` 只能通过 PR 修改、且必须有 1 个审核通过：
   ```bash
   gh api -X PUT repos/WRM-FW/apex-atlas/branches/main/protection \
     -H "Accept: application/vnd.github+json" \
     -f required_status_checks=null -f enforce_admins=false \
     -f 'required_pull_request_reviews.required_approving_review_count=1' \
     -f restrictions=null
   ```
3. （可选，再加一道人工闸门）Settings → Environments → `github-pages` →
   Required reviewers → 添加审核人。这样即使代码被合并，部署仍需有人点 **Approve**。

### 4.2 日常更新

```bash
git checkout -b update/<改动主题>
# ... 改数据或代码 ...
git add -A && git commit -m "update: ..."
git push -u origin update/<改动主题>
gh pr create --fill          # 或到 GitHub 网页上创建 PR
```

PR 打开后 Actions 会自动跑 `check → build → deploy`，并在部署任务里生成一个**临时预览地址**
（Deploy preview，仅自己和仓库成员可见，保留 30 天）。审核通过、合并到 `main` 后，同一套产物
才会正式发布到 `https://wrm-fw.github.io/apex-atlas/`。

### 4.3 路径适配说明

站点可能部署在 `username.github.io/repo-name/` 这样的二级子路径下，因此：

* 所有资源都用**相对路径**；`js/data.js` 里的 `AA.url()` 会按当前页面路径推导出站点根目录，
  再拼接 `data/`、`assets/` 路径。
* 路由使用 **hash 模式**（`#/track/monza`），刷新、直接粘贴链接、前进后退都不会 404，
  也不需要任何服务端 rewrite 规则。
* `tools/check_site.py` 会在 CI 中扫描任何以 `/` 开头的绝对路径并让构建失败，防止回归。

## 5. 维护：新增或修改一条赛道

### 只改内容
直接编辑 `data/tracks/<id>.json`：赛段文字、弯角解析、规格数字都是普通字段。
新增一个弯角解析组时，在 `corner_groups` 里加一项，并把对应弯角编号写进 `codes` 数组
（`codes` 必须与 `hotspots[].n` 一致，否则地图高亮对不上）。改完提 PR 即可。

### 换一张新地图 / 加一条新赛道
`tools/extract/` 保留了本项目提取弯角坐标的完整流程（详见 `tools/extract/README.md`）：

```
detect_v3.py      从 PNG 中识别弯角编号气泡 → _tools/out/*.json
sheet2.py         生成带十字准星的编号核对图，用于人工确认编号
validate_labels.py校验每站编号是否构成连续的 1..N
build_geometry.py 输出百分比坐标热点 + 压缩地图 WebP
build_data.py     合并 content_*.py 的文字 → data/tracks/*.json
build_dim.py      生成赛段压暗遮罩层
```

提取脚本需要 `pillow`、`numpy`、`scipy`，且不修改原始图片。

## 6. 数据口径

见站点内「数据说明」页。要点：弯角编号与位置以官方风格地图为准（共 406 个热点，逐站核对编号连续性）；
规格与赛段文字来自《2026 赛季 F1 全赛道技术指南》；吉达站指南未收录，按普通赛道补录并标注；
马德里 Madring 指南记 20 弯，地图实为 22 弯并含 5A、20A，站点以地图编号为准。
