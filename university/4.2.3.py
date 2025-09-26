import random
import matplotlib.pyplot as plt

LOW, HIGH = 0, 100
N_VALUES = HIGH - LOW + 1
N_TRIALS = 1000


def smart_ai(secret, low=LOW, high=HIGH):
    c = 0
    lo, hi = low, high
    while lo <= hi:
        c += 1
        mid = (lo + hi) // 2
        if mid == secret:
            return c
        elif mid < secret:
            lo = mid + 1
        else:
            hi = mid - 1
    return c


def dumb_ai(secret, low=LOW, high=HIGH):
    c = 0
    remaining = list(range(low, high + 1))
    while True:
        c += 1
        g = random.choice(remaining)
        if g == secret:
            return c
        remaining.remove(g)


def simulate(n_trials=N_TRIALS):
    means_smart = []
    means_dumb = []
    for secret in range(LOW, HIGH + 1):
        s_sum = 0
        d_sum = 0
        for _ in range(n_trials):
            s_sum += smart_ai(secret)
            d_sum += dumb_ai(secret)
        means_smart.append(s_sum / n_trials)
        means_dumb.append(d_sum / n_trials)
    return means_smart, means_dumb


def print_text_hist(means_smart, means_dumb):
    for i, (ms, md) in enumerate(zip(means_smart, means_dumb)):
        print(f"[{i}] " + "*" * int(round(ms)))
        print(f"[{i}] " + "-" * int(round(md)))


def plot_curves(means_smart, means_dumb):
    x = list(range(LOW, HIGH + 1))
    plt.figure(figsize=(10, 5))
    plt.plot(x, means_smart, label="IA intelligente (dichotomie)")
    plt.plot(x, means_dumb, label="IA aléatoire (sans remise)")
    plt.xlabel("Nombre secret")
    plt.ylabel("Nombre moyen d'essais")
    plt.title(
        f"Moyenne des essais pour chaque nombre secret ({N_TRIALS} parties/valeur)"
    )
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    means_smart, means_dumb = simulate()
    print_text_hist(means_smart, means_dumb)
    plot_curves(means_smart, means_dumb)
    print(f"Moyenne globale IA intelligente ≈ {sum(means_smart) / N_VALUES:.2f}")
    print(f"Moyenne globale IA aléatoire ≈ {sum(means_dumb) / N_VALUES:.2f}")
