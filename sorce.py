import random
import time

holdings = [-1, -1, -1, -1]

tail = 0
head = 0
holdingsCount = 0
holdingsLen = len(holdings)
jackpotRate = 0.01
fireGenRate = 0.4
fireHitRate = jackpotRate*fireGenRate
normalWaitCount = 3
fireWaitCount = 5

def getIsFire(holding):
    return (holding > 1-fireHitRate) or (fireHitRate > holding)

def getEggStr(isFire):
    return isFire and "🔥" or "🥚"

def printHoldings():
    print("| ", end="")
    for holding in holdings:
        isFire = getIsFire(holding)
        str = (holding == -1) and " " or getEggStr(isFire)
        print(str, end=" | ")

def getWaitCount(isFire):
    return isFire and fireWaitCount or normalWaitCount 

def getIsHit(holding):
    return jackpotRate > holding 

print("卵を獲得する場合は\"a\"、卵を剥く場合は\"f\"を押してください(qでゲーム終了)")

while True:
    command = input(">>> ")
    if command == "q": break

    if command == "a":
        if holdingsCount >= holdingsLen:
            print("卵でいっぱいです")
            continue
        # 卵を獲得する
        num = random.random()
        print(num)
        holdingsCount += 1
        holdings[head] = num
        head = (head + 1) % holdingsLen
        printHoldings()
    elif command == "f":
        if holdingsCount <= 0:
            print("卵がありません")
            continue
        # 卵を剥く
        num = holdings[tail]
        holdingsCount -= 1
        holdings[tail] = -1
        tail = (tail + 1) % holdingsLen
        isFire = getIsFire(num)
        eggStr = getEggStr(isFire)
        waitCount = getWaitCount(isFire)
        print(eggStr, end="\n")
        for i in range(waitCount):
            if normalWaitCount > i :
                print("ギュン", end="\n")
            else:
                print("ギュインギュイン!!!", end="\n")
            time.sleep(1)
        
        resultStr = getIsHit(num) and "あたり!!" or "はずれ"
        print("---\n",resultStr, "\n---")
        printHoldings()
    else:
        print("不正な入力です")
        continue
    print()
            
        
    
    











