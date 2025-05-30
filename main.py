import os
import sys
import subprocess

os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(lang):
    input("\n按下 Enter 返回菜单..." if lang == 'zh' else "\nPress Enter to return to menu...")

def print_ascii_logo():
    print(r"""
  _______ _____            _____  ______ _____      _____  _____   ____  
 |__   __|  __ \     /\   |  __ \|  ____|  __ \    |  __ \|  __ \ / __ \ 
    | |  | |__) |   /  \  | |  | | |__  | |__) |   | |__) | |__) | |  | |
    | |  |  _  /   / /\ \ | |  | |  __| |  _  /    |  ___/|  _  /| |  | | 
    | |  | | \ \  / ____ \| |__| | |____| | \ \    | |    | | \ \| |__| |
    |_|  |_|  \_\/_/    \_\_____/|______|_|  \_\   |_|    |_|  \_\\____/  v2.0

                Terminal Trading Toolkit by Simon
""")

def select_language():
    clear_screen()
    print("Select Language / 请选择语言:")
    print()
    print("[1] English")
    print("[2] 中文")
    print()
    choice = input("Enter number / 请输入编号: ").strip()
    return 'en' if choice == '1' else 'zh'

def main_menu():
    lang = select_language()
    while True:
        clear_screen()
        print_ascii_logo()
        print("*******************************************************")
        print()

        if lang == 'zh':
            print("请选择模块：")
            print()
            print("  [1] 点数盈亏计算器")
            print("  [2] 风控强平计算器")
            print("  [0] 退出")
            print()
            choice = input("请输入选项编号：").strip()
        else:
            print("Select a module:")
            print()
            print("  [1] Profit Calculator")
            print("  [2] Risk Control Calculator")
            print("  [0] Exit")
            print()
            choice = input("Enter your choice: ").strip()

        print()
        print("*******************************************************")

        if choice == '1':
            clear_screen()
            print_ascii_logo()
            print("*******************************************************")
            print()
            subprocess.run(["python", "module/calculate_points.py", lang])
            pause(lang)
        elif choice == '2':
            clear_screen()
            print_ascii_logo()
            print("*******************************************************")
            print()
            subprocess.run(["python", "module/risk_control.py", lang])
            pause(lang)
        elif choice == '0':
            print("感谢使用，再见！" if lang == 'zh' else "Thank you, goodbye!")
            break
        else:
            print("无效输入，请重新输入。" if lang == 'zh' else "Invalid input, please try again.")
            pause(lang)

if __name__ == "__main__":
    main_menu()
