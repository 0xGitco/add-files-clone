
for i in range(10):
    with open(f'file{i+1}.txt', 'w+') as w:
        w.write(f'This is file {i+1}.')