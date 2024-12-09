import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)  # 随机生成1到100之间的数字
    attempts = 0

    print("欢迎来到猜数字游戏！")
    print("我已经选择了一个1到100之间的数字。你能猜到它是什么吗？")

    while True:
        user_guess = input("请输入你的猜测（或输入'退出'以结束游戏）：")
        
        if user_guess.lower() == '退出':
            print("感谢参与游戏！再见！")
            break
        
        attempts += 1
        
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("请输入一个有效的数字！")
            continue

        if user_guess < number_to_guess:
            print("太小了！再试一次。")
        elif user_guess > number_to_guess:
            print("太大了！再试一次。")
        else:
            print(f"恭喜你！你猜对了，数字是 {number_to_guess}。")
            print(f"你总共猜了 {attempts} 次。")
            break

if __name__ == "__main__":
    guess_number_game()
