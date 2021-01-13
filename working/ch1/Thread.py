import threading


def sum(low, high):
    total = 0
    for i in range(low, high):
        total += i
    print("SubThread", total)

    t = threading.Thread(target=sum, args=1000000)
    t.start()


print("Main Thread")
