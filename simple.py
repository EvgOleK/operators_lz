import math

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    
    limit = int(math.sqrt(number))
    for d in range(2, limit + 1):
        if number % d == 0:
            return False
    
    return True


def main() -> None:
        print("Введите число для проверки на простоту.")
        raw = input()
        number = int(raw)

        if not (1 <= number <= 25):
            print("n вне допустимого диапазона [1, 25].")
            return 0;

        print("Число простое" if is_prime(number) else "Число составное")


if __name__ == "__main__":
    main()