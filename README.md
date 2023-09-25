# Scrapy Parser Pep <sub> _a.k.a Парсер Пеп Правил_ </sub>

Данный проект предоставляет возможность парсить вводимые, завершенные или же в процессе разработки правила Pep. Его польза очевидна - за секунду вы можете получить **ВСЕ** актуальные правила Pep.

## Содержимое:

  [Инструкция по запуску.](#инструкия-по-запуску-проекта)

  [Примеры результатов работы.](#примеры-результатов-работы-программы)

  [Технологии](#технологии-)


## Инструкия по запуску проекта.

Для запуска данного проекта вам понадобится:
1. Развернуть и активировать виртуальное окружение проекта на версии 3.9:

   - Для Windows: 
     ```bash
     py -3.9 -m venv venv
     source venv/Scripts/activate
     ```
   - Для MacOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Для Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
2. Установить зависимости из файла `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

1. Запустить паучка:
    ```bash
    scrapy crawl pep
    ```

После выполнения программы будет создана папка **results**, в ней появятся 2 файла с актуальными Pep'ами. 

**Profit!**



## Примеры результатов работы программы:

```text
# results/pep_{time_now}.csv
number,name,status
0,Index of Python Enhancement Proposals (PEPs),Active
233,Python Online Help,Deferred
236,Back to the __future__,Final
232,Function Attributes,Final
```
```
# results/status_summary_{time_now}.csv
Статус,Количество

Active,32

Deferred,37

Final,276
```

## _Технологии :_
_[Scrapy](https://scrapy.org/), Python 3.9_