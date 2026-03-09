#!/usr/bin/env python3
"""
数学图案生成器
生成 200 个 THR 格式的沙画图案
"""

import os
import math
import random
from pathlib import Path

class PatternGenerator:
    def __init__(self, output_dir="thr-files"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.generated = 0
        
    def save_pattern(self, name, points):
        """保存图案到 THR 文件"""
        filepath = self.output_dir / f"{name}.thr"
        with open(filepath, 'w') as f:
            f.write(f"# {name}\n")
            f.write(f"# Points: {len(points)}\n\n")
            for x, y in points:
                f.write(f"{x:.6f},{y:.6f}\n")
        self.generated += 1
        return filepath
    
    def lissajous(self, a, b, delta, num_points=1000):
        """利萨如曲线"""
        points = []
        for i in range(num_points):
            t = 2 * math.pi * i / num_points
            x = 0.5 + 0.4 * math.sin(a * t + delta)
            y = 0.5 + 0.4 * math.sin(b * t)
            points.append((x, y))
        return points
    
    def spiral(self, turns=5, num_points=1000):
        """阿基米德螺旋"""
        points = []
        for i in range(num_points):
            t = turns * 2 * math.pi * i / num_points
            r = 0.4 * i / num_points
            x = 0.5 + r * math.cos(t)
            y = 0.5 + r * math.sin(t)
            points.append((x, y))
        return points
    
    def rose(self, n, d, num_points=1000):
        """玫瑰曲线"""
        points = []
        k = n / d
        for i in range(num_points):
            t = 2 * math.pi * d * i / num_points
            r = 0.4 * math.cos(k * t)
            x = 0.5 + r * math.cos(t)
            y = 0.5 + r * math.sin(t)
            points.append((x, y))
        return points
    
    def circle_packing(self, num_circles=20):
        """圆 Packing"""
        points = []
        for i in range(num_circles):
            angle = 2 * math.pi * i / num_circles
            for j in range(50):
                t = 2 * math.pi * j / 50
                r = 0.05 + 0.02 * i
                cx = 0.5 + 0.3 * math.cos(angle)
                cy = 0.5 + 0.3 * math.sin(angle)
                x = cx + r * math.cos(t)
                y = cy + r * math.sin(t)
                points.append((x, y))
        return points
    
    def mandala(self, symmetry=8, layers=5):
        """曼陀罗图案"""
        points = []
        for layer in range(layers):
            r = 0.1 + 0.08 * layer
            for i in range(symmetry * 20):
                angle = 2 * math.pi * i / (symmetry * 20)
                # 添加花瓣形状
                petal = abs(math.sin(symmetry * angle))
                r_eff = r * (0.8 + 0.2 * petal)
                x = 0.5 + r_eff * math.cos(angle)
                y = 0.5 + r_eff * math.sin(angle)
                points.append((x, y))
        return points
    
    def spirograph(self, R, r, d, num_points=2000):
        """万花尺图案"""
        points = []
        for i in range(num_points):
            t = 10 * math.pi * i / num_points
            x = 0.5 + 0.4 * ((R - r) * math.cos(t) + d * math.cos((R - r) * t / r))
            y = 0.5 + 0.4 * ((R - r) * math.sin(t) - d * math.sin((R - r) * t / r))
            points.append((x, y))
        return points
    
    def dragon_curve(self, iterations=12):
        """龙形曲线"""
        # 简化版本，使用折线
        points = [(0.5, 0.5)]
        x, y = 0.5, 0.5
        angle = 0
        step = 0.02
        
        for i in range(min(iterations * 100, 2000)):
            angle += random.choice([-math.pi/2, math.pi/2])
            x += step * math.cos(angle)
            y += step * math.sin(angle)
            x = max(0.1, min(0.9, x))
            y = max(0.1, min(0.9, y))
            points.append((x, y))
        return points
    
    def phyllotaxis(self, n=500):
        """叶序螺旋（向日葵图案）"""
        points = []
        golden_angle = math.pi * (3 - math.sqrt(5))
        for i in range(n):
            r = 0.4 * math.sqrt(i / n)
            theta = i * golden_angle
            x = 0.5 + r * math.cos(theta)
            y = 0.5 + r * math.sin(theta)
            points.append((x, y))
        return points
    
    def harmonograph(self, num_points=2000):
        """谐振仪图案"""
        points = []
        f1, f2, f3, f4 = 2.01, 3.02, 3.03, 2.04
        p1, p2, p3, p4 = 0, 0, math.pi/2, math.pi/3
        d1, d2, d3, d4 = 0.0005, 0.0005, 0.0005, 0.0005
        
        for i in range(num_points):
            t = i * 0.1
            x = 0.5 + 0.4 * (math.sin(f1 * t + p1) * math.exp(-d1 * t) + 
                             math.sin(f2 * t + p2) * math.exp(-d2 * t))
            y = 0.5 + 0.4 * (math.sin(f3 * t + p3) * math.exp(-d3 * t) + 
                             math.sin(f4 * t + p4) * math.exp(-d4 * t))
            points.append((x, y))
        return points
    
    def generate_all(self, target=200):
        """生成所有图案"""
        print(f"开始生成 {target} 个图案...")
        
        # 1. 利萨如曲线 (30个)
        params = [(2,3,0), (3,4,0), (3,5,0), (4,5,0), (5,6,0),
                  (2,3,math.pi/4), (3,4,math.pi/4), (3,5,math.pi/4),
                  (2,3,math.pi/2), (3,4,math.pi/2), (5,4,0), (7,5,0),
                  (5,8,0), (6,7,0), (7,8,0), (8,9,0), (9,10,0),
                  (3,7,0), (4,7,0), (5,7,0), (2,5,0), (3,8,0),
                  (4,9,0), (5,9,0), (6,11,0), (7,9,0), (8,11,0),
                  (5,12,0), (7,12,0), (11,13,0)]
        for a, b, delta in params[:30]:
            points = self.lissajous(a, b, delta)
            self.save_pattern(f"lissajous_{a}_{b}_{int(delta*100)}", points)
            if self.generated >= target:
                return
        
        # 2. 螺旋 (10个)
        for turns in range(3, 13):
            points = self.spiral(turns=turns)
            self.save_pattern(f"spiral_{turns}turns", points)
            if self.generated >= target:
                return
        
        # 3. 玫瑰曲线 (20个)
        rose_params = [(2,1), (3,1), (4,1), (5,1), (6,1), (7,1), (8,1),
                       (3,2), (4,3), (5,2), (5,3), (5,4), (6,5), (7,2),
                       (7,3), (7,4), (7,5), (7,6), (8,3), (8,5)]
        for n, d in rose_params:
            points = self.rose(n, d)
            self.save_pattern(f"rose_{n}_{d}", points)
            if self.generated >= target:
                return
        
        # 4. 曼陀罗 (15个)
        for sym in [3, 4, 5, 6, 7, 8, 9, 10, 12, 16, 20, 24, 32, 48, 64]:
            points = self.mandala(symmetry=sym)
            self.save_pattern(f"mandala_{sym}fold", points)
            if self.generated >= target:
                return
        
        # 5. 万花尺 (25个)
        spiro_params = [(5,3,2), (7,3,2), (8,5,3), (10,3,1), (10,6,2),
                        (12,5,3), (12,7,2), (15,7,3), (15,8,3), (16,9,4),
                        (20,7,3), (20,9,4), (21,13,5), (24,11,4), (30,11,4),
                        (30,13,5), (40,11,4), (40,13,5), (60,13,5), (60,17,7),
                        (72,17,7), (84,19,8), (100,21,9), (120,23,10), (144,25,11)]
        for R, r, d in spiro_params:
            points = self.spirograph(R, r, d)
            self.save_pattern(f"spirograph_{R}_{r}_{d}", points)
            if self.generated >= target:
                return
        
        # 6. 圆 Packing (10个)
        for n in [5, 6, 7, 8, 9, 10, 12, 15, 18, 20]:
            points = self.circle_packing(num_circles=n)
            self.save_pattern(f"circles_{n}", points)
            if self.generated >= target:
                return
        
        # 7. 龙形曲线 (10个)
        for i in range(10):
            points = self.dragon_curve(iterations=10+i)
            self.save_pattern(f"dragon_{i+1}", points)
            if self.generated >= target:
                return
        
        # 8. 叶序螺旋 (10个)
        for n in [200, 300, 400, 500, 600, 700, 800, 900, 1000, 1200]:
            points = self.phyllotaxis(n=n)
            self.save_pattern(f"phyllotaxis_{n}", points)
            if self.generated >= target:
                return
        
        # 9. 谐振仪 (10个)
        for i in range(10):
            points = self.harmonograph()
            self.save_pattern(f"harmonograph_{i+1}", points)
            if self.generated >= target:
                return
        
        # 10. 随机组合 (60个)
        patterns = [
            lambda: self.lissajous(random.randint(2,10), random.randint(3,10), random.random()*math.pi),
            lambda: self.spiral(turns=random.randint(3,10)),
            lambda: self.rose(random.randint(2,8), random.randint(1,5)),
            lambda: self.mandala(symmetry=random.randint(3,20)),
            lambda: self.phyllotaxis(n=random.randint(300,1000)),
        ]
        
        for i in range(60):
            pattern_func = random.choice(patterns)
            points = pattern_func()
            self.save_pattern(f"random_{i+1}", points)
            if self.generated >= target:
                return
        
        print(f"✓ 已生成 {self.generated} 个图案")

if __name__ == "__main__":
    gen = PatternGenerator("../thr-files")
    gen.generate_all(200)
    print(f"\n总计生成: {gen.generated} 个图案")
