def main() -> None:
        
        print("Введите 3 числа через пробел (первый элемент прогрессии b, множитель прогрессии q и номер последнего элемента n).")
        raw = input()
        parts = raw.split()
        if len(parts) != 3:
            print("Ожидалось три значения: b q n в одной строке.")
            return 0;

        firstElem = int(parts[0])
        progressionMult = int(parts[1])
        lastElem = int(parts[2])

        if not (-10000 <= firstElem <= 10000):
            print("b вне допустимого диапазона [-10000, 10000].")
            return 0;
        if not (1 <= progressionMult <= 50):
            print("q вне допустимого диапазона [1, 50].")
            return 0;
        if not (2 <= lastElem <= 100):
            print("n вне допустимого диапазона [2, 100].")
            return 0;

        if progressionMult == 1:
            result = firstElem * lastElem
        else:
            result = firstElem * ((progressionMult ** lastElem) - 1) / (progressionMult - 1)

        print("Сумма прогрессии =", int(result))

if __name__ == "__main__":
    main()
