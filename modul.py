import random
import matplotlib.pyplot as plt


def get_uniform_distribution(a, b):
    rand_number = random.randint(a, b)
    #return (b - a) * rand_number + a
    return rand_number


def simulation(a, b, n):
    return [get_uniform_distribution(a, b) for _ in range(n)]


def build_plot(numbers):
    plt.hist(numbers, bins=5, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.xlabel('Значення')
    plt.ylabel('Частота')
    plt.title('Гістограма рівномірного розподілу')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    a = 5
    b = 10
    n = 2500


    random_numbers = simulation(a, b, n)
    build_plot(random_numbers)

