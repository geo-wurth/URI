sapo = list(map(int, input().split()))
canos = list(map(int, input().split()))

def game():
    for i in range(1, len(canos)):
        if abs(canos[i] - canos[i-1]) > sapo[0]:
            return 'GAME OVER'
    return 'YOU WIN'

print(game())
