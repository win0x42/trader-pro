
import sys

def calculate_risk_and_liquidation():
    lang = sys.argv[1] if len(sys.argv) > 1 else 'zh'

    if lang == 'zh':
        print("*** 风控强平计算工具 ***")
    else:
        print("*** Risk Control and Liquidation Calculator ***")

    try:
        if lang == 'zh':
            margin = float(input("请输入当前占用保证金 (USD): "))
            equity = float(input("请输入当前动态权益 (USD): "))
            risk_limit = float(input("请输入设置的风险度阈值 (%)，如100或150: "))
        else:
            margin = float(input("Enter current margin used (USD): "))
            equity = float(input("Enter current dynamic equity (USD): "))
            risk_limit = float(input("Enter risk threshold (%) such as 100 or 150: "))
    except ValueError:
        print("输入无效，请输入数字。" if lang == 'zh' else "Invalid input, please enter numbers.")
        return

    current_risk = (margin / equity) * 100
    liquidation_equity = margin * (100 / risk_limit)

    print("\n--- 计算结果 ---" if lang == 'zh' else "\n--- Results ---")
    print(f"{'当前风险度' if lang == 'zh' else 'Current Risk Ratio'}: {current_risk:.2f}%")
    print(f"{'强平触发动态权益临界值' if lang == 'zh' else 'Liquidation Equity Threshold'}: USD {liquidation_equity:.2f}")

    if equity <= liquidation_equity:
        print("⚠️ 当前动态权益已达到或低于强平触发点，系统将强制平仓。" if lang == 'zh'
              else "⚠️ Current equity has reached or fallen below liquidation threshold. Forced liquidation will occur.")
    else:
        print("✅ 当前风险处于安全范围，无强平风险。" if lang == 'zh'
              else "✅ Risk level is safe. No liquidation risk.")

if __name__ == "__main__":
    calculate_risk_and_liquidation()
