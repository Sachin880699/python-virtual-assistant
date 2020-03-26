with open('command.txt') as f:
    lines = [line.rstrip() for line in f]
    print(lines)
    command = lines.index('what is your name')

with open('answer.txt') as f:
    lines = [line.rstrip() for line in f]
    print(command)
    print(lines[command])
