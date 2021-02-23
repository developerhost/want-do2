# place
s_x, s_y = map(int, input().split()) 

# move
d_f, d_r, d_b, d_l = map(int, input().split())
N = int(input())


EC = [list(map(str, input().split())) for _ in range(N)]
# [x,y]への移動方向
move = {'N': {'F': [0, d_f], 'R': [d_r, 0], 'L': [-d_l, 0], 'B': [0, -d_b]},
        'E': {'F': [d_f, 0], 'R': [0, -d_r], 'L': [0, d_l], 'B': [-d_b, 0]},
        'W': {'F': [-d_f, 0], 'R': [0, d_r], 'L': [0, -d_l], 'B': [d_b, 0]},
        'S': {'F': [0, -d_f], 'R': [-d_r, 0], 'L': [d_l, 0], 'B': [0, d_b]}
        }
direction_change = {'N': {'F': 'N', 'R': 'E', 'L': 'W', 'B': 'S'},
                    'E': {'F': 'E', 'R': 'S', 'L': 'N', 'B': 'W'},
                    'W': {'F': 'W', 'R': 'N', 'L': 'S', 'B': 'E'},
                    'S': {'F': 'S', 'R': 'W', 'L': 'E', 'B': 'N'}
                    }
direction = 'N'
ans = [s_x, s_y]
for e, c in EC:
    if e == 'm':
        mx, my = move[direction][c]
        ans[0] += mx
        ans[1] += my
    else:
        direction = direction_change[direction][c]
print(*ans)