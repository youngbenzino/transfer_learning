
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

## Структура проекта
<img width="1056" height="527" alt="image" src="https://github.com/user-attachments/assets/52189a1f-7e25-46b7-9841-788b7ec1242b" />

## Требования
- Python  
- TensorFlow  
- NumPy  
- Pillow  

Все зависимости указаны в файле `requirements.txt`.

## Инструкция по запуску для Windows
#### 1) Клонировать репозиторий
git clone https://github.com/youngbenzino/transfer_learning.git

cd transfer_learning


#### 2) Создать виртуальное окружение
python -m venv .venv


#### 3) Активировать виртуальное окружение (ниже приведены команды для Windows)
.venv\Scripts\activate


#### 4) Установить зависимости
pip install -r requirements.txt


#### 5) Убедиться, что dataset содержит подкаталоги train и test с изображениями по классам


#### 6) Запустить скрипт
python transfer_learning.py


#### После запуска скрипт выведет точность модели до и после обучения, а также изменение точности.
