#!/usr/bin/env python3
"""
多样化图案生成器 v2
生成更多类型的沙画图案，不只是圆内轨迹
"""

import os
import math
import random
from pathlib import Path

class DiversePatternGenerator:
    def __init__(self, output_dir="../thr-files"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.generated = []
        
    def save_pattern(self, name, points):
        """保存图案到 THR 文件"""
        filepath = self.output_dir / f"{name}.thr"
        with open(filepath, 'w') as f:
            f.write(f"# {name}\n")
            f.write(f"# Points: {len(points)}\n\n")
            for x, y in points:
                f.write(f"{x:.6f},{y:.6f}\n")
        self.generated.append(name)
        return filepath
    
    def square_spiral(self, turns=10, num_points=1000):
        """方形螺旋"""
        points = []
        for i in range(num_points):
            t = i / num_points
            angle = turns * 2 * math.pi * t
            # 方形螺旋：结合正方形和螺旋
            side = int(4 * t * turns) % 4
            r = 0.4 * t
            if side == 0:
                x, y = r, -r + 2*r*t*4
            elif side == 1:
                x, y = r, r
            elif side == 2:
                x, y = -r, r
            else:
                x, y = -r, -r
            x = 0.5 + x
            y = 0.5 + y
            points.append((x, y))
        return points
    
    def square_grid(self, n_lines=10):
        """方形网格"""
        points = []
        step = 0.8 / n_lines
        # 水平线
        for i in range(n_lines + 1):
            y = 0.1 + i * step
            points.append((0.1, y))
            points.append((0.9, y))
            points.append((0.9, y))  # 重复以便连续
        # 垂直线
        for i in range(n_lines + 1):
            x = 0.1 + i * step
            points.append((x, 0.9))
            points.append((x, 0.1))
            points.append((x, 0.1))
        return points
    
    def zigzag(self, n_zigs=20):
        """之字形"""
        points = []
        for i in range(n_zigs * 2):
            x = 0.1 + 0.8 * i / (n_zigs * 2)
            y = 0.1 if i % 2 == 0 else 0.9
            points.append((x, y))
        return points
    
    def star(self, n_points=5, outer_r=0.4, inner_r=0.15):
        """星形"""
        points = []
        for i in range(n_points * 2):
            angle = math.pi * i / n_points - math.pi / 2
            r = outer_r if i % 2 == 0 else inner_r
            x = 0.5 + r * math.cos(angle)
            y = 0.5 + r * math.sin(angle)
            points.append((x, y))
        points.append(points[0])  # 闭合
        return points
    
    def heart(self, num_points=200):
        """心形"""
        points = []
        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            # 心形方程
            x = 16 * (math.sin(t) ** 3)
            y = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
            # 归一化
            x = 0.5 + x / 35
            y = 0.5 - y / 35
            points.append((x, y))
        return points
    
    def infinity_symbol(self, num_points=200):
        """无限符号 ∞"""
        points = []
        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            # 双纽线
            cos_t = math.cos(t)
            sin_t = math.sin(t)
            denom = 1 + sin_t ** 2
            x = cos_t / denom
            y = sin_t * cos_t / denom
            x = 0.5 + x * 0.4
            y = 0.5 + y * 0.4
            points.append((x, y))
        return points
    
    def wave_pattern(self, n_waves=5, n_points=500):
        """波浪图案"""
        points = []
        for i in range(n_points):
            x = i / n_points
            y = 0.5 + 0.3 * math.sin(n_waves * 2 * math.pi * x)
            points.append((x, y))
        return points
    
    def tree_fractal(self, x=0.5, y=0.9, angle=-math.pi/2, length=0.2, depth=6):
        """分形树"""
        points = []
        def draw_branch(x, y, angle, length, depth):
            if depth == 0:
                return
            x2 = x + length * math.cos(angle)
            y2 = y + length * math.sin(angle)
            points.append((x, y))
            points.append((x2, y2))
            # 递归两个分支
            draw_branch(x2, y2, angle - 0.3, length * 0.7, depth - 1)
            draw_branch(x2, y2, angle + 0.3, length * 0.7, depth - 1)
        
        draw_branch(x, y, angle, length, depth)
        return points
    
    def maze_pattern(self, size=10):
        """迷宫图案"""
        points = []
        cell_size = 0.8 / size
        # 简单的蛇形迷宫
        for row in range(size):
            y = 0.1 + row * cell_size
            if row % 2 == 0:
                points.append((0.1, y))
                points.append((0.9, y))
            else:
                points.append((0.9, y))
                points.append((0.1, y))
            # 添加垂直连接
            if row < size - 1:
                if row % 2 == 0:
                    points.append((0.9, y))
                    points.append((0.9, y + cell_size))
                else:
                    points.append((0.1, y))
                    points.append((0.1, y + cell_size))
        return points
    
    def constellation(self, n_stars=50):
        """星座/星空图案"""
        points = []
        stars = [(random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)) for _ in range(n_stars)]
        # 连线形成星座
        for i in range(len(stars) - 1):
            x1, y1 = stars[i]
            x2, y2 = stars[i + 1]
            points.append((x1, y1))
            points.append((x2, y2))
            # 偶尔返回上一个点，形成三角形
            if i > 0 and random.random() > 0.7:
                x0, y0 = stars[i - 1]
                points.append((x2, y2))
                points.append((x0, y0))
        return points
    
    def text_letter(self, letter='A', num_points=300):
        """简化字母轨迹（模拟）"""
        points = []
        letter_paths = {
            'A': [(0.3, 0.8), (0.5, 0.2), (0.7, 0.8), (0.6, 0.5), (0.4, 0.5)],
            'B': [(0.3, 0.2), (0.3, 0.8), (0.6, 0.8), (0.6, 0.5), (0.3, 0.5), (0.6, 0.5), (0.6, 0.2), (0.3, 0.2)],
            'C': [(0.7, 0.2), (0.3, 0.2), (0.3, 0.8), (0.7, 0.8)],
            'S': [(0.7, 0.2), (0.3, 0.2), (0.3, 0.5), (0.7, 0.5), (0.7, 0.8), (0.3, 0.8)],
            'X': [(0.3, 0.2), (0.7, 0.8), (0.5, 0.5), (0.3, 0.8), (0.7, 0.2)],
        }
        path = letter_paths.get(letter, letter_paths['A'])
        for x, y in path:
            points.append((x, y))
        return points
    
    def city_skyline(self, n_buildings=15):
        """城市天际线"""
        points = []
        x = 0.1
        for i in range(n_buildings):
            width = random.uniform(0.03, 0.08)
            height = random.uniform(0.2, 0.7)
            # 建筑左下
            points.append((x, 0.9))
            points.append((x, 0.9 - height))
            # 顶部
            points.append((x + width, 0.9 - height))
            # 右下
            points.append((x + width, 0.9))
            x += width + 0.01
        return points
    
    def random_walk(self, n_steps=1000):
        """随机漫步"""
        points = []
        x, y = 0.5, 0.5
        points.append((x, y))
        for _ in range(n_steps):
            angle = random.uniform(0, 2 * math.pi)
            step = 0.02
            x += step * math.cos(angle)
            y += step * math.sin(angle)
            x = max(0.05, min(0.95, x))
            y = max(0.05, min(0.95, y))
            points.append((x, y))
        return points
    
    def generate_diverse_set(self):
        """生成多样化图案集"""
        print("生成多样化图案集...")
        
        # 1. 方形图案
        for i in range(3, 12):
            points = self.square_spiral(turns=i)
            self.save_pattern(f"square_spiral_{i}", points)
        
        for n in [5, 8, 10, 15, 20]:
            points = self.square_grid(n_lines=n)
            self.save_pattern(f"square_grid_{n}", points)
        
        # 2. 之字形
        for n in [10, 15, 20, 30, 50]:
            points = self.zigzag(n_zigs=n)
            self.save_pattern(f"zigzag_{n}", points)
        
        # 3. 星形
        for n in [3, 4, 5, 6, 7, 8, 10, 12]:
            points = self.star(n_points=n)
            self.save_pattern(f"star_{n}point", points)
        
        # 4. 心形和无限符号
        points = self.heart()
        self.save_pattern("heart_shape", points)
        
        points = self.infinity_symbol()
        self.save_pattern("infinity_symbol", points)
        
        # 5. 波浪
        for n in [3, 5, 7, 10, 15]:
            points = self.wave_pattern(n_waves=n)
            self.save_pattern(f"wave_{n}", points)
        
        # 6. 分形树
        for depth in [4, 5, 6, 7]:
            points = self.tree_fractal(depth=depth)
            self.save_pattern(f"fractal_tree_d{depth}", points)
        
        # 7. 迷宫
        for size in [5, 8, 10, 12]:
            points = self.maze_pattern(size=size)
            self.save_pattern(f"maze_{size}x{size}", points)
        
        # 8. 星座
        for n in [20, 30, 40, 50]:
            points = self.constellation(n_stars=n)
            self.save_pattern(f"constellation_{n}", points)
        
        # 9. 字母
        for letter in ['A', 'B', 'C', 'S', 'X']:
            points = self.text_letter(letter=letter)
            self.save_pattern(f"letter_{letter}", points)
        
        # 10. 城市天际线
        for n in [10, 15, 20]:
            points = self.city_skyline(n_buildings=n)
            self.save_pattern(f"city_skyline_{n}", points)
        
        # 11. 随机漫步
        for i in range(1, 6):
            points = self.random_walk(n_steps=500 + i * 100)
            self.save_pattern(f"random_walk_{i}", points)
        
        print(f"✓ 已生成 {len(self.generated)} 个多样化图案")
        return self.generated

if __name__ == "__main__":
    gen = DiversePatternGenerator("../thr-files")
    patterns = gen.generate_diverse_set()
    print(f"\n总计: {len(patterns)} 个新图案")
    for p in patterns[:10]:
        print(f"  - {p}")
    print(f"  ... 和另外 {len(patterns) - 10} 个")
