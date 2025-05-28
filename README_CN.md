
# TRADER PRO v2.0 - 终端交易工具集

**TRADER PRO** 是一款基于命令行的交易工具，提供点数盈亏计算器、风控强平计算器等模块，适用于交易员、分析师、策略开发者快速使用与测试。

---

## 功能模块

| 模块名称                | 功能描述                                                |
|-------------------------|----------------------------------------------------------|
| 点数盈亏计算器          | 输入开/平仓价格、方向、参数，计算盈亏（含手续费）        |
| 风控强平计算器          | 输入保证金、动态权益与风险阈值，计算强平临界点与当前风险 |
| ASCII LOGO              | 打印带有艺术字的 `TRADER PRO` 终端欢迎界面               |

---

## 项目结构

```
trader-pro/
├── module/
│   ├── calculate_points.py   # 点数计算模块
│   └── risk_control.py       # 风控计算模块
├── main.py                   # 主程序（语言选择 + 菜单）
├── README_CN.md              # 中文说明文档
├── README_EN.md              # English Documentation
```

---

## 使用方法

1. 安装 Python（建议版本 >= 3.8）：
```bash
python --version
```

2. 下载本项目：
```bash
git clone https://github.com/win0x42/trader-pro.git
cd trader-pro
```

3. 运行主程序：
```bash
python main.py
```

---

## 作者信息

- 作者：Simon
- 职业：软件运维工程师
- 关键词：终端交易计算工具、盈亏分析、风险模型

---

## License

本项目采用 MIT 开源协议，允许修改、使用和二次开发。
