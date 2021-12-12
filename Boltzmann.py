import random
from matplotlib import pyplot as plt

N = 100 #人数
M = 1000 #猜拳次数
score_board = {} #计分
for i in range(N):
    score_board[i] = 0

def finger_guess(pair):
    global score_board
    result = [-1,0,1] #两个人，胜负平概率相等
    k = random.choice(result)
    if k == 0:
        return 0
    elif k == -1:
        if score_board[pair[0]]==0:
            score_board[pair[1]] += 1
            return 0
        else:
            score_board[pair[1]] += 1
            score_board[pair[0]] -= 1
            return 0
    elif k == 1:
        if score_board[pair[1]]==0 :
            score_board[pair[0]] += 1
            return 0
        else:
            score_board[pair[0]] += 1
            score_board[pair[1]] -= 1
            return 0
K=score_board.keys()
for i in range(M):
    pair = random.sample(K,2)
    finger_guess(pair)

distribution = {}
for i in score_board.keys():
    try:
        distribution[score_board[i]] += 1
    except:
        distribution[score_board[i]] = 1
score_board = {}
x=[]
y=[]
for i in list(distribution.keys()):
    x.append(i)
    y.append(distribution[i]/N)

plt.scatter(x,y)
plt.show()