# Transfer Learning Project

## Описание
Учебный проект по **Transfer Learning** с использованием модели **MobileNetV2**, предобученной на **ImageNet**.  
Цель проекта — классификация изображений на несколько классов (например, различные виды мячей: american_football, baseball, basketball, billiard_ball, bowling_ball).

Проект выполняет следующие шаги:
1. Подготовка рабочего датасета с ограничением количества изображений на класс;
2. Загрузка данных с помощью `ImageDataGenerator`;
3. Создание модели на основе MobileNetV2 (без верхнего слоя);
4. Тестирование точности модели **до обучения**;
5. Обучение модели на небольшом наборе данных;
6. Тестирование точности **после обучения** и сравнение с исходной.

## Структура проекта (читать на вкладке Code)
│ 
├─ dataset/ # Исходные изображения 
  │ 
  ├─ TEST
    |
    ├─ american_football 
    ├─ baseball 
    ├─ basketball 
    ├─ billiard_ball 
    └─ bowling_ball
  ├─ TRAIN
    |
    ├─ american_football 
    ├─ baseball 
    ├─ basketball 
    ├─ billiard_ball 
    └─ bowling_ball
├─ work_dataset/ # Временная папка с выбранными изображениями, создается скриптом, по структуре не отличается от папки dataset 
├─ transfer_learning.py # Основной скрипт проекта 
├─ README.md # Этот файл 
├─ requirements.txt # Зависимости проекта 
└─ .gitignore # Игнорируемые файлы и папки (локальные и временные)

## Требования
- Python 3.8+  
- TensorFlow 2.11+  
- NumPy >=1.23.0  
- Pillow >=9.0.0  

Все зависимости указаны в файле `requirements.txt`.

## Как запустить
#### Клонировать репозиторий
git clone https://github.com/username/project.git
cd project

#### Создать виртуальное окружение
python -m venv .venv

#### Активировать виртуальное окружение (ниже приведены команды для Windows)
.venv\Scripts\activate

#### Установить зависимости
pip install -r requirements.txt

#### Убедиться, что dataset содержит подкаталоги train и test с изображениями по классам

#### Запустить скрипт
python transfer_learning.py



После запуска скрипт выведет точность модели до и после обучения, а также изменение точности.
