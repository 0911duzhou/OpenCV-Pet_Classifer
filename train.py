# -*- coding: utf-8 -*-
# @File: train.py
# @Author: 嘟粥yyds
# @Time: 2023/08/25

import tensorflow as tf
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping, ReduceLROnPlateau, TensorBoard
from data import train_db, dev_db
import models
import settings

# 从models文件中导入模型
model = models.my_densenet()

# 创建 TensorBoard 回调对象
tensorboard_callback = TensorBoard(log_dir='logs', histogram_freq=1, write_graph=True, write_images=True)

# 配置优化器、损失函数、以及监控指标
model.compile(tf.keras.optimizers.Adam(settings.LEARNING_RATE), loss=tf.keras.losses.categorical_crossentropy,
              metrics=['accuracy'])

# 在每个epoch结束后尝试保存模型参数，只有当前参数的val_accuracy比之前保存的更优时，才会覆盖掉之前保存的参数
model_check_point = ModelCheckpoint(filepath=settings.MODEL_PATH, monitor='val_accuracy',
                                    save_best_only=True)

# 创建早停回调对象
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# 创建学习率减少回调对象
lr_decay = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=3, min_lr=1e-6)

# 使用tf.keras的高级接口进行训练
model.fit(train_db, epochs=settings.TRAIN_EPOCHS, validation_data=dev_db,
          callbacks=[model_check_point, early_stopping, lr_decay, tensorboard_callback])
