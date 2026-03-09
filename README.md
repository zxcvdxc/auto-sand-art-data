# 自动沙画图案库 | Auto Sand Art Patterns

🏖️ **200 个数学生成的沙画图案**，可用于 Oasis Mini、Sisyphus 等自动沙画装置。

## 🎨 在线预览

访问 [GitHub Pages](https://你的用户名.github.io/auto-sand-art-data/) 查看所有图案的在线预览。

## 📊 图案统计

| 类型 | 数量 | 说明 |
|------|------|------|
| 利萨如曲线 | 30 | Lissajous curves，不同频率比的正弦波组合 |
| 螺旋 | 10 | Archimedean spiral，阿基米德螺旋 |
| 玫瑰曲线 | 20 | Rose curves，极坐标下的花瓣图案 |
| 曼陀罗 | 15 | Mandala patterns，对称放射状图案 |
| 万花尺 | 25 | Spirograph，齿轮滚动的轨迹 |
| 圆 Packing | 10 | Circle packing，多个圆的排列组合 |
| 龙形曲线 | 10 | Dragon curve，分形折线 |
| 叶序螺旋 | 10 | Phyllotaxis，向日葵种子排列模式 |
| 谐振仪 | 10 | Harmonograph，多摆运动的叠加 |
| 随机组合 | 60 | 随机参数生成的混合图案 |

**总计：200 个图案**

## 📁 文件格式

### THR 格式说明
```
# 文件名
# 点数: 1000

0.500000,0.500000
0.502000,0.501000
0.504000,0.503000
...
```

- 每行包含 `x,y` 坐标
- 坐标归一化到 0-1 范围
- x: 水平位置 (0=左, 1=右)
- y: 垂直位置 (0=下, 1=上)

## 🚀 使用方法

### 直接下载
1. 进入 `thr-files/` 目录
2. 下载需要的 `.thr` 文件
3. 导入到你的沙画装置

### 批量下载
```bash
git clone https://github.com/你的用户名/auto-sand-art-data.git
cd auto-sand-art-data/thr-files
```

## 🛠️ 生成新图案

```bash
cd src
python3 generate_patterns.py
```

可以修改脚本参数生成更多图案：
- 调整 `num_points` 改变点数密度
- 修改参数范围生成不同变体
- 添加新的图案算法

## 📝 技术说明

### 图案生成算法

1. **利萨如曲线**
   ```python
   x = sin(a * t + δ)
   y = sin(b * t)
   ```

2. **玫瑰曲线**
   ```python
   r = cos(k * θ)
   x = r * cos(θ)
   y = r * sin(θ)
   ```

3. **万花尺**
   ```python
   x = (R-r)*cos(t) + d*cos((R-r)*t/r)
   y = (R-r)*sin(t) - d*sin((R-r)*t/r)
   ```

4. **叶序螺旋**
   ```python
   r = sqrt(n/N)
   θ = n * 137.5°  # 黄金角
   ```

## 📦 项目结构

```
auto-sand-art-data/
├── README.md              # 项目说明
├── index.html             # 展示网站
├── thr-files/             # 200 个 THR 图案文件
├── src/                   # 源代码
│   └── generate_patterns.py
└── docs/                  # 文档
```

## 🎯 适用设备

- ✅ Oasis Mini
- ✅ Sisyphus Table
- ✅ 自制沙画装置
- ✅ 任何支持 THR/G-code 的沙画机

## 📜 许可证

MIT License - 可自由使用、修改、分发

## 🤝 贡献

欢迎提交新的图案！可以通过：
1. 修改 `generate_patterns.py` 添加新算法
2. 手动创建 THR 文件
3. 分享你的原创图案

---

Made with ❤️ and mathematics
