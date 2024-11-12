

def filter_logs():
    # commands = ["pipe2", "dup2", "openat", "close", "clone"]
    commands = ["pipe2", "close"]
    logs = []
    with open('pipeline_log.txt', 'r') as file:
        f = file.readlines()
    
    for i, line in enumerate(f):
        for c in commands:
            if c in line:
                l = f"{i} {line}"
                logs.append(l)

    return logs

    


if __name__ == "__main__":
    with open("res.txt", 'w') as file:
        for l in filter_logs():
            print(l, file=file)