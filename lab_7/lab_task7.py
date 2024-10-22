lines = ['first', 'second', 'third']
with open('lab_task1.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')