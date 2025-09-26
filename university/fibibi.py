def fibo(n: int, mem=None) -> int:
    if mem is None:
        mem = {}
    if n <= 1:
        return n
    if n in mem:
        return mem[n]
    mem[n] = fibo(n - 1, mem) + fibo(n - 2, mem)
    return mem[n]


memo = {1: [1]}


def syracuse(n):
    if n in memo:
        return memo[n]
    if n % 2 == 0:
        seq = [n] + syracuse(n // 2)
    else:
        seq = [n] + syracuse(3 * n + 1)
    memo[n] = seq
    return seq


if __name__ == "__main__":
    import time

    n = int(input("n: "))
    start = time.time()
    print(fibo(n))
    print(len(str((fibo(n)))))
    end = time.time()
    print(end - start)


def fibo_fast(n: int) -> int:
    def _fd(k: int) -> tuple[int, int]:
        if k == 0:
            return (0, 1)
        a, b = _fd(k // 2)
        c = a * ((b << 1) - a)
        d = a * a + b * b
        if k & 1:
            return (d, c + d)
        return (c, d)

    return _fd(n)[0]
