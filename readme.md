# Порівняння ефективності алгоритмів пошуку підрядка

## Опис завдання
Порівняти ефективність алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів (стаття 1, стаття 2). Використовуючи `timeit`, виміряти час виконання кожного алгоритму для двох видів підрядків: одного, що дійсно існує в тексті, та іншого — вигаданого.

## Результати експерименту

### Стаття 1
- Існуючий підрядок ("Література"):
  - Боєра-Мура: `time_boyer_moore_existing_1`
  - Кнута-Морріса-Пратта: `time_kmp_existing_1`
  - Рабіна-Карпа: `time_rabin_karp_existing_1`

- Неіснуючий підрядок ("nonexistent"):
  - Боєра-Мура: `time_boyer_moore_non_existing_1`
  - Кнута-Морріса-Пратта: `time_kmp_non_existing_1`
  - Рабіна-Карпа: `time_rabin_karp_non_existing_1`

### Стаття 2
- Існуючий підрядок ("Література"):
  - Боєра-Мура: `time_boyer_moore_existing_2`
  - Кнута-Морріса-Пратта: `time_kmp_existing_2`
  - Рабіна-Карпа: `time_rabin_karp_existing_2`

- Неіснуючий підрядок ("nonexistent"):
  - Боєра-Мура: `time_boyer_moore_non_existing_2`
  - Кнута-Морріса-Пратта: `time_kmp_non_existing_2`
  - Рабіна-Карпа: `time_rabin_karp_non_existing_2`

### Висновки
- Найшвидший алгоритм для статті 1:
  - Існуючий підрядок: [назва алгоритму]
  - Неіснуючий підрядок: [назва алгоритму]

- Найшвидший алгоритм для статті 2:
  - Існуючий підрядок: [назва алгоритму]
  - Неіснуючий підрядок: [назва алгоритму]

- Найшвидший алгоритм в цілому:
  - Існуючий підрядок: [назва алгоритму]
  - Неіснуючий підрядок: [назва алгоритму]