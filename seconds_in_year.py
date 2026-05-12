#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
計算一年有幾秒的程式
"""

# 方法一：直接計算
def seconds_in_year_basic():
    """簡單計算：365天 × 24小時 × 60分鐘 × 60秒"""
    seconds = 365 * 24 * 60 * 60
    return seconds


# 方法二：考慮閏年
def seconds_in_year_with_leap():
    """平均一年秒數（考慮閏年）"""
    # 平年：365天，閏年：366天
    # 平均：(365*3 + 366) / 4 = 365.25天
    seconds = 365.25 * 24 * 60 * 60
    return seconds


# 方法三：使用 datetime 模組
def seconds_in_year_datetime():
    """使用 datetime 計算"""
    from datetime import datetime, timedelta
    
    start = datetime(2024, 1, 1)
    end = datetime(2025, 1, 1)
    difference = end - start
    
    return difference.total_seconds()


if __name__ == "__main__":
    print("=" * 50)
    print("一年有多少秒？")
    print("=" * 50)
    
    # 方法一
    result1 = seconds_in_year_basic()
    print(f"\n方法一（基本計算）:")
    print(f"365天 × 24小時 × 60分鐘 × 60秒 = {result1:,.0f} 秒")
    
    # 方法二
    result2 = seconds_in_year_with_leap()
    print(f"\n方法二（考慮閏年平均值）:")
    print(f"365.25天 × 24小時 × 60分鐘 × 60秒 = {result2:,.0f} 秒")
    
    # 方法三
    result3 = seconds_in_year_datetime()
    print(f"\n方法三（2024年實際秒數，閏年）:")
    print(f"2024年1月1日 到 2025年1月1日 = {result3:,.0f} 秒")
    
    print("\n" + "=" * 50)
