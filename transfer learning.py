import os
import shutil
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam


# ============= НАСТРОЙКИ =============
DATASET_PATH = "dataset"  # исходная папка
WORK_PATH = "work_dataset"  # временная папка, создаётся автоматически

N_TEST = 20   # количество изображений из каждого класса для теста
M_TRAIN = 35  # количество изображений из каждого класса для обучения

IMAGE_SIZE = (384, 384)
BATCH_SIZE = 8
# =====================================


# ======================================================
# 1. ПОДГОТОВКА ВРЕМЕННОЙ ПАПКИ С РУЧНЫМ ОГРАНИЧЕНИЕМ N
# ======================================================

def prepare_limited_dataset():
    if os.path.exists(WORK_PATH):
        shutil.rmtree(WORK_PATH)
    os.makedirs(WORK_PATH)

    for subset in ["train", "test"]:
        os.makedirs(os.path.join(WORK_PATH, subset))

    classes = os.listdir(os.path.join(DATASET_PATH, "train"))

    for cls in classes:
        # создаём папки
        os.makedirs(os.path.join(WORK_PATH, "train", cls))
        os.makedirs(os.path.join(WORK_PATH, "test", cls))

        # исходные файлы
        train_files = os.listdir(os.path.join(DATASET_PATH, "train", cls))
        test_files = os.listdir(os.path.join(DATASET_PATH, "test", cls))

        # перемешиваем
        random.shuffle(train_files)
        random.shuffle(test_files)

        # берём вручную указанное количество файлов
        selected_train = train_files[:M_TRAIN]
        selected_test = test_files[:N_TEST]

        # копируем в рабочую папку
        for f in selected_train:
            shutil.copy(
                os.path.join(DATASET_PATH, "train", cls, f),
                os.path.join(WORK_PATH, "train", cls, f)
            )

        for f in selected_test:
            shutil.copy(
                os.path.join(DATASET_PATH, "test", cls, f),
                os.path.join(WORK_PATH, "test", cls, f)
            )

    print("Рабочий датасет подготовлен!")
    print(f"Используется {M_TRAIN} изображений на класс для обучения.")
    print(f"Используется {N_TEST} изображений на класс для тестирования.\n")


# Создаём рабочий датасет
prepare_limited_dataset()


# ======================================================
# 2. ЗАГРУЗКА ДАННЫХ
# ======================================================

train_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    WORK_PATH + "/train",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=True
)

test_data = train_datagen.flow_from_directory(
    WORK_PATH + "/test",
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    shuffle=False
)

num_classes = train_data.num_classes


# ======================================================
# 3. ПОСТРОЕНИЕ МОДЕЛИ
# ======================================================

base_model = MobileNetV2(
    weights="imagenet", include_top=False, input_shape=IMAGE_SIZE + (3,)
)
base_model.trainable = False

x = GlobalAveragePooling2D()(base_model.output)
output = Dense(num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer=Adam(1e-3),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)


# ======================================================
# 4. ТОЧНОСТЬ ДО ОБУЧЕНИЯ
# ======================================================

loss_before, acc_before = model.evaluate(test_data, verbose=0)
print(f"\nТочность ДО обучения: {acc_before * 100:.2f}%\n")


# ======================================================
# 5. ОБУЧЕНИЕ
# ======================================================

model.fit(train_data, epochs=5, verbose=1)


# ======================================================
# 6. ТОЧНОСТЬ ПОСЛЕ ОБУЧЕНИЯ
# ======================================================

loss_after, acc_after = model.evaluate(test_data, verbose=0)
print(f"\nТочность ПОСЛЕ обучения: {acc_after * 100:.2f}%")
print(f"Изменение точности: {(acc_after - acc_before) * 100:.2f}%\n")
