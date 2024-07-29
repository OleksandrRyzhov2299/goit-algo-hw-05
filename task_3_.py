import os
import timeit

# Функції для алгоритмів пошуку підрядка
def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    bad_char = [-1] * 256
    for i in range(m):
        bad_char[ord(pattern[i])] = i
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char[ord(text[s + j])])
    return -1

def kmp_search(text, pattern):
    def compute_lps_array(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps_array(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t += q
    return -1

# Перевірка існування файлів
if not os.path.exists('article1.txt'):
    print("Файл 'article1.txt' не знайдено.")
else:
    with open('article1.txt', 'r', encoding='utf-8') as file:
        text1 = file.read()

if not os.path.exists('article2.txt'):
    print("Файл 'article2.txt' не знайдено.")
else:
    with open('article2.txt', 'r', encoding='utf-8') as file:
        text2 = file.read()

# Підрядки для пошуку
substring_existing = "example"
substring_non_existing = "nonexistent"

# Вимірювання часу для статті 1 (якщо файл існує)
if 'text1' in locals():
    time_boyer_moore_existing_1 = timeit.timeit(lambda: boyer_moore(text1, substring_existing), number=1000)
    time_boyer_moore_non_existing_1 = timeit.timeit(lambda: boyer_moore(text1, substring_non_existing), number=1000)

    time_kmp_existing_1 = timeit.timeit(lambda: kmp_search(text1, substring_existing), number=1000)
    time_kmp_non_existing_1 = timeit.timeit(lambda: kmp_search(text1, substring_non_existing), number=1000)

    time_rabin_karp_existing_1 = timeit.timeit(lambda: rabin_karp(text1, substring_existing), number=1000)
    time_rabin_karp_non_existing_1 = timeit.timeit(lambda: rabin_karp(text1, substring_non_existing), number=1000)

    print(f"Стаття 1, існуючий підрядок: Боєра-Мура: {time_boyer_moore_existing_1}, Кнута-Морріса-Пратта: {time_kmp_existing_1}, Рабіна-Карпа: {time_rabin_karp_existing_1}")
    print(f"Стаття 1, неіснуючий підрядок: Боєра-Мура: {time_boyer_moore_non_existing_1}, Кнута-Морріса-Пратта: {time_kmp_non_existing_1}, Рабіна-Карпа: {time_rabin_karp_non_existing_1}")

# Вимірювання часу для статті 2 (якщо файл існує)
if 'text2' in locals():
    time_boyer_moore_existing_2 = timeit.timeit(lambda: boyer_moore(text2, substring_existing), number=1000)
    time_boyer_moore_non_existing_2 = timeit.timeit(lambda: boyer_moore(text2, substring_non_existing), number=1000)

    time_kmp_existing_2 = timeit.timeit(lambda: kmp_search(text2, substring_existing), number=1000)
    time_kmp_non_existing_2 = timeit.timeit(lambda: kmp_search(text2, substring_non_existing), number=1000)

    time_rabin_karp_existing_2 = timeit.timeit(lambda: rabin_karp(text2, substring_existing), number=1000)
    time_rabin_karp_non_existing_2 = timeit.timeit(lambda: rabin_karp(text2, substring_non_existing), number=1000)

    print(f"Стаття 2, існуючий підрядок: Боєра-Мура: {time_boyer_moore_existing_2}, Кнута-Морріса-Пратта: {time_kmp_existing_2}, Рабіна-Карпа: {time_rabin_karp_existing_2}")
    print(f"Стаття 2, неіснуючий підрядок: Боєра-Мура: {time_boyer_moore_non_existing_2}, Кнута-Морріса-Пратта: {time_kmp_non_existing_2}, Рабіна-Карпа: {time_rabin_karp_non_existing_2}")