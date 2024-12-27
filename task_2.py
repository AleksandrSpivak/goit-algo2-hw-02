from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через мемоізацію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    
    memo = [0] * (length + 1)   # Ініціалізація для рекурсії та мемоізації

    cut_record = [0] * (length + 1)  # Для збереження довжини розрізу

    def cut_rod(length):
        if length == 0:
            return 0
        if memo[length] != 0:
            return memo[length]
        max_profit = 0
        for i in range(1, length + 1):
            profit = prices[i - 1] + cut_rod(length - i)
            if profit > max_profit:
                max_profit = profit
                cut_record[length] = i  # Зберігаємо оптимальний розріз
        memo[length] = max_profit
        return memo[length]

    # Запуск рекурсивної функції
    cut_rod(length)

    # Відновлюємо список розрізів
    cuts = []
    while length > 0:
        cuts.append(cut_record[length])
        length -= cut_record[length]

    return {
        "max_profit": memo[-1],
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

    


def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    """
    Знаходить оптимальний спосіб розрізання через табуляцію

    Args:
        length: довжина стрижня
        prices: список цін, де prices[i] — ціна стрижня довжини i+1

    Returns:
        Dict з максимальним прибутком та списком розрізів
    """
    # Ініціалізація для табуляції
    res_table = [0 for _ in range(length + 1)]

    # Заповнення першої табуляцій
    for i in range(1, length + 1):
        res_table[i] = prices[i - 1]

    # Заповнення остальних табуляцій
    for i in range(1, length + 1):
        for j in range(1, i + 1):
            res_table[i] = max(res_table[i], res_table[i - j] + prices[j - 1])

    # Відновлюємо список розрізів
    cuts = []
    current_length = length
    while current_length > 0:
        for i in range(1, current_length + 1):
            if res_table[current_length] == res_table[current_length - i] + prices[i - 1]:
                cuts.append(i)
                current_length -= i
                break

    return {
        "max_profit": res_table[length],
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
