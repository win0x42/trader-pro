
# TRADER PRO v2.0 - Terminal Trading Toolkit

**TRADER PRO** is a command-line based toolkit for traders and analysts. It includes calculators for profit/loss points and liquidation risk management, helping you make quick trading decisions.

---

## Features

| Module Name              | Description                                                |
|--------------------------|------------------------------------------------------------|
| Profit Calculator        | Calculates gain/loss based on trade direction, price, fees |
| Risk Control Calculator  | Evaluates forced liquidation threshold based on equity     |
| ASCII Logo Output        | Displays an ASCII art logo of `TRADER PRO`                 |

---

## Project Structure

```
trader-pro/
├── module/
│   ├── calculate_points.py   # Profit calculator script
│   └── risk_control.py       # Risk control calculator
├── main.py                   # Entry script with language menu
├── README_CN.md              # 中文使用说明
├── README.md                 # English documentation
```

---

## How to Use

1. Install Python (version >= 3.8):
```bash
python --version
```

2. Clone this repository:
```bash
git clone https://github.com/win0x42/trader-pro.git
cd trader-pro
```

3. Run the application:
```bash
python main.py
```

---

## Author

- Author: Simon
- Role: Software Operation Engineer
- Keywords: Terminal Trading Tools, P&L Analysis, Risk Models, CLI Utilities
---

## License

This project is licensed under the MIT License. Free to use, modify and distribute.
