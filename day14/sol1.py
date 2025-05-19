with open('input14.txt', 'r') as f:
    reader = f.read().strip().split('\n')
robots=[]
for line in reader:
    robot = {}
    raw_p, raw_v = line.split()
    raw_p = raw_p[2:]
    x_p, y_p = [int(num) for num in raw_p.split(',')]
    robot['p'] = (x_p, y_p)
    raw_v = raw_v[2:]
    v_x, v_y = [int(num) for num in raw_v.split(',')]
    robot['v'] = (v_x, v_y)
    robots.append(robot)

print(robots)

W = 6
H = 10
end_time = 5
def update_position(robot):
    x, y = robot['p']
    v_x, v_y = robot['v']
    x, y = x + v_x, y + v_y
    if x > W:
        x = x - W
    if x < 0:
        x = W + x
    if y > H:
        y = y - H
    if y < 0:
        y = H + y

    return (x,y)

def run(end_time):
    for _ in range(end_time):
        for robot in robots:
            new_p = update_position(robot)
            robot['p'] = new_p
e_r = {'p': (2,4), 'v':(2,-3)}
print(update_position(e_r))
e_r['p'] = update_position(e_r)
print(update_position(e_r))
e_r['p'] = update_position(e_r)
print(update_position(e_r))
e_r['p'] = update_position(e_r)
print(update_position(e_r))
e_r['p'] = update_position(e_r)

