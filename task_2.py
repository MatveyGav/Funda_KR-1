def fib_gen():
    pred_last, last = 0, 1
    while True:
        yield pred_last
        pred_last, last = last, pred_last + last

gen = fib_gen()
