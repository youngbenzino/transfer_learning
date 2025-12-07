# Transfer Learning Project

## Описание
Учебный проект по **Transfer Learning** с использованием модели **MobileNetV2**, предобученной на **ImageNet**.  
Цель проекта — классификация изображений на несколько классов (например, различные виды мячей: american_football, baseball, basketball, billiard_ball, bowling_ball).

Проект реализует **transfer learning** с использованием предобученной модели **MobileNetV2**. Основные шаги:
- **Подготовка датасета** — формирование рабочего набора изображений с ограничением количества примеров на класс
- **Загрузка данных** — с помощью ImageDataGenerator для автоматической генерации батчей и аугментации изображений
- **Создание модели** — использование MobileNetV2 без верхнего (классификационного) слоя, чтобы адаптировать модель под свои классы
- **Тестирование исходной модели** — оценка точности предобученной модели на рабочем наборе данных до обучения
- **Обучение модели** — дообучение модели на небольшом наборе данных для адаптации к конкретной задаче

Оценка результатов — тестирование точности модели после обучения и сравнение с исходной.
## Требования
- Git
- Build Tools для Visual Studio
- Python  
- TensorFlow  
- NumPy  
- Pillow 

Все зависимости указаны в файле `requirements.txt`.

## Инструкция по запуску для Windows
### 1) Установить Git 2.52.0
https://github.com/git-for-windows/git/releases/download/v2.52.0.windows.1/Git-2.52.0-64-bit.exe

### 2) Установить Python 3.12.8
https://www.python.org/ftp/python/3.12.8/python-3.12.8-amd64.exe

### 3) Установить Build Tools для Visual Studio 2026
https://visualstudio.microsoft.com/ru/downloads/?q=build+tools#remote-tools-for-visual-studio-2026

#### 3.1) В установщике выбрать "Разработка классических приложений на C++"
#### 3.2) В появившихся справа сведениях об установке выбрать следующие пункты:
- Средства сборки MSVC для x64/x86
- Windows 11 SDK (будет работать и на Windows 10)
- Средства CMake C++ для Windows
- MSVC версии 143 — средства сборки С++ VS 2022 для x64/x86
#### 3.3) Нажать на "Установить"

### 4) Клонировать репозиторий
git clone https://github.com/youngbenzino/transfer_learning.git

### 5) Далее может потребоваться прохождение аутентификации на github

### 6) Перейти в директорию проекта
cd transfer_learning

### 7) Создать виртуальное окружение
python -m venv .venv

### 8) Разово разрешить скрипт в текущей сессии PowerShell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

### 9) Выбрать опцию "Да"

Y

### 10) Активировать виртуальное окружение
.venv\Scripts\activate

### 11) Установить зависимости
pip install -r requirements.txt

### 12) Запустить скрипт
python transfer_learning.py

### После запуска скрипт выведет точность модели до и после обучения, а также изменение точности.
