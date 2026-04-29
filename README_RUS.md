# Python Performance Benchmarks

Практический проект, демонстрирующий влияние различных подходов в Python на **скорость выполнения** и **потребление памяти**.

Проект построен на реальных измерениях, а не предположениях:

- `timeit` — измерение времени выполнения
- `resource` — анализ использования памяти
- `termgraph` — визуализация результатов в терминале

---

## Перед началом

### 1. Установка зависимостей

```bash
pip install termgraph
```

---

### 2. Загрузка датасета

Для теста чтения файлов используется датасет [MovieLens](https://grouplens.org/datasets/movielens/).

Что нужно сделать:

1. Скачать архив (`ml-25m`)
2. Распаковать
3. Взять файл:

```text
ratings.csv
```

> Размер файла ~678 MB — он не включён в репозиторий

Поместите его в:

```text
data/ratings.csv
```

---

## Что исследуется в проекте

### Фильтрация email

Сравнение подходов:

- loop
- list comprehension
- map
- filter

### Сумма квадратов

Сравнение:

- loop
- reduce

### Counter vs ручная реализация

Сравнение:

- dict (ручной подсчёт)
- collections.Counter
- поиск топ-10 элементов

### Чтение файлов

Сравнение:

- readlines (загрузка в память)
- generator (ленивое чтение)

---

## Структура проекта

```text
python-performance-benchmarks/
├── benchmarks/        # логика бенчмарков
├── data/              # данные для графиков (.dat)
├── results/           # результаты бенчмарков
├── scripts/           # вспомогательные скрипты
├── utils/             # сохранение результатов
├── main.py            # точка входа
├── requirements.txt
└── README.md
```

---

## Установка

```bash
git clone <repo>
cd python-performance-benchmarks

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Использование

### Запуск всех бенчмарков

```bash
sh scripts/run_all.sh
```

---

### Запуск по отдельности

```bash
# фильтрация email
python3 main.py email 1000000

# сумма квадратов
python3 main.py squares 1000000 5

# counter
python3 main.py counter

# чтение файла
python3 main.py file ordinary data/ratings.csv
python3 main.py file generator data/ratings.csv
```

---

## Подготовка данных для графиков

```bash
python3 scripts/build_termgraph.py
```

---

## Визуализация

```bash
sh scripts/visualize.sh email_filtering.dat
sh scripts/visualize.sh sum_squares.dat
sh scripts/visualize.sh counter_benchmark.dat
sh scripts/visualize.sh file_reading.dat
```

> Требуется установленный `termgraph`

## Результаты и анализ

Ниже представлены результаты измерений.

## Фильтрация и email

![Email Filtering](screenshots/email_filtering.png)

**Вывод:**

- `list comprehension` — самый быстрый способ  

- `loop` немного медленнее  

- `filter` и `map` значительно уступают  

Причина: list comprehension реализован на уровне C и имеет меньше накладных расходов.

---

## Counter Benchmark

![Counter Benchmark](screenshots/counter_benchmark.png)

**Вывод:**

- `collections.Counter` быстрее ручной реализации  

- `most_common()` эффективнее сортировки  

Причина: встроенные структуры оптимизированы на уровне Python/C.

---

## Counter Benchmark

![File Reading](screenshots/file_reading.png)

**Вывод:**

- генераторы используют **в десятки раз меньше памяти**

- при этом могут работать быстрее или сопоставимо

Причина: данные обрабатываются по мере чтения, без загрузки в память.

---

## Сумма квадратов

![Sum of Squares](screenshots/sum_squares.png)

**Вывод:**

- обычный `loop` быстрее `reduce`

Причина: `reduce` создаёт дополнительные вызовы функций (overhead).

---

## Основные выводы

- встроенные инструменты Python обычно быстрее ручных реализаций
- list comprehension быстрее обычных циклов
- генераторы существенно экономят память
- reduce может быть медленнее из-за накладных расходов
- производительность нужно измерять, а не угадывать

---

## Зависимости

```text
termgraph
```

---

## Примечания

Данный проект выполнен в рамках обучения и использован в качестве пет проекта.
