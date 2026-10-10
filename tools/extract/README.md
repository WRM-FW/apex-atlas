# 弯角坐标提取与数据生成流程

这些脚本把「赛道地图 PNG」变成站点用的 JSON 与图片资产。它们只在维护时使用，不会被部署。
所有脚本都**只读**原始地图，输出写到 `_work/` 或站点目录，不会覆盖素材。

## 依赖

```bash
pip install pillow numpy scipy
```

## 输入约定

原始地图放在一个目录里（脚本里的 `SRC` / `MAPS` 常量），文件名形如
`01_Australia_Melbourne.png`。地图需满足：

* 弯角编号是画面中**最小的独立文字块**（1–3 个字符，如 `9`、`14`、`20A`）；
* 赛道中线按赛段着色（本项目的两套配色见 `detect_v3.py` 的 `SECTOR_COLORS`）；
* 背景透明。

## 步骤

| 顺序 | 脚本 | 作用 | 输出 |
| --- | --- | --- | --- |
| 1 | `detect_v3.py` | 识别数字气泡：按亮度分离墨迹 → 连通域 → 按尺寸/分辨率归一化筛选 → 聚类成编号 | `_work/out/<地图名>.json`（候选点 + 最近赛段色） |
| 2 | `sheet2.py` | 为每个候选点生成带**十字准星**的放大核对图 | `_work/out/sheets2/*_sheet2.png` |
| 3 | 人工 | 读准星下的数字，把 `候选序号 → 弯角编号` 写进 `labels.json`（非弯角填 `null`） | `labels.json` |
| 4 | `validate_labels.py` | 校验每站编号构成连续 `1..N`，并提示跨度过大的相邻弯角（通常是长直道，正常） | 控制台 |
| 5 | `build_geometry.py` | 像素坐标换算成**百分比坐标**；同时导出 1600px 与 640px WebP 地图 | `data/corners/*.json`、`assets/maps/*.webp` |
| 6 | `build_data.py` | 把 `content_*.py` 的文字与几何合并成站点数据，并检查文字里引用的弯角是否都存在 | `data/tracks/*.json`、`data/season.json` |
| 7 | `build_dim.py` | 按赛段颜色生成压暗遮罩（赛段高亮用），先做去噪再膨胀到路面宽度 | `assets/dim/<id>_<S#>.webp` |

`overlay2.py` 是排错工具：把候选序号画回地图上，用来确认漏检/误检的位置。

## 两套地图风格

`detect_v3.py` 里的 `STYLE_B` 元组列出「深色气泡 + 白色数字」的文件前缀，其余按
「白色气泡 + 深色数字」处理。新地图若属于另一套风格，把这个前缀加进去即可；
若出现第三套配色，需要扩写 `SECTOR_COLORS`。

## 站点内容在哪里

`content_a.py` … `content_d.py` 按赛站分组存放中文文案（简介、赛段、弯角解析、调校要点），
`content_season.py` 存放赛季概览、新规、流派分类、图例、术语表与数据说明。
改完执行 `python build_data.py <站点目录>` 重新生成 JSON。
