
import sys

def calculate_points(open_price, close_price, position):
    if position in ('buy', 'b'):
        return close_price - open_price
    elif position in ('sell', 's'):
        return open_price - close_price
    else:
        raise ValueError("请输入 buy(b) 或 sell(s)" if lang == 'zh' else "Please enter buy(b) or sell(s)")

def calculate_point_value(tick_size, contract_size):
    return tick_size * contract_size

def calculate_profit_usd(points, point_value, usd_rate):
    return points * point_value / usd_rate

def calculate_total_fee(per_lot_fee, lots=1, sides=2):
    return per_lot_fee * lots * sides

if __name__ == "__main__":
    lang = sys.argv[1] if len(sys.argv) > 1 else 'zh'

    try:
        print("*** 点数盈亏计算工具（含手续费） ***" if lang == 'zh' else "*** Profit Calculator (with Fees) ***")

        # Basic input
        open_price = float(input("请输入开仓价：" if lang == 'zh' else "Enter open price: "))
        close_price = float(input("请输入平仓价：" if lang == 'zh' else "Enter close price: "))
        position = input("请输入方向 buy(b) 或 sell(s)：" if lang == 'zh' else "Enter direction buy(b) or sell(s): ").strip().lower()

        # Contract parameters
        contract_size = float(input("请输入合约乘数：" if lang == 'zh' else "Enter contract size: "))
        tick_size = float(input("请输入最小变动单位：" if lang == 'zh' else "Enter tick size: "))
        usd_rate = float(input("请输入本币兑美元汇率：" if lang == 'zh' else "Enter local currency to USD rate: "))

        # Fee settings
        per_lot_fee = float(input("请输入每手手续费（美元）：" if lang == 'zh' else "Enter fee per lot (USD): "))
        lots = int(input("请输入交易手数：" if lang == 'zh' else "Enter number of lots: "))

        # Calculations
        points = calculate_points(open_price, close_price, position)
        point_value = calculate_point_value(tick_size, contract_size)
        gross_profit_usd = calculate_profit_usd(points, point_value, usd_rate)
        total_fee_usd = calculate_total_fee(per_lot_fee, lots)
        net_profit = gross_profit_usd - total_fee_usd

        # Output
        print("\n--- 计算结果 ---" if lang == 'zh' else "\n--- Results ---")
        print(f"{'点数变动' if lang == 'zh' else 'Point Difference'}: {points:.4f}")
        print(f"{'每点价格（本币）' if lang == 'zh' else 'Point Value (Local Currency)'}: {point_value:.4f}")
        print(f"{'总盈亏（USD）' if lang == 'zh' else 'Gross Profit (USD)'}: {gross_profit_usd:.2f}")
        print(f"{'手续费（双边，总共）' if lang == 'zh' else 'Total Fee (USD, round trip)'}: {total_fee_usd:.2f}")
        print(f"{'净盈亏（USD）' if lang == 'zh' else 'Net Profit (USD)'}: {net_profit:.2f}")

    except Exception as e:
        print(f"❌ 发生错误：{e}" if lang == 'zh' else f"❌ Error occurred: {e}")
