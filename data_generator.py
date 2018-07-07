# encoding=utf-8
import json
import os
import jieba
import numpy as np
import keras
from keras.preprocessing.image import (ImageDataGenerator, load_img, img_to_array)
from keras.utils import Sequence

from config import batch_size, img_rows, img_cols, max_token_length, vocab
from config import train_folder, train_annotations_filename, train_image_folder
from config import valid_folder, valid_annotations_filename, valid_image_folder


class DataGenSequence(Sequence):
    def __init__(self, usage):
        self.usage = usage

        if usage == 'train':
            annotations_path = os.path.join(train_folder, train_annotations_filename)
            self.image_folder = train_image_folder
        else:
            annotations_path = os.path.join(valid_folder, valid_annotations_filename)
            self.image_folder = valid_image_folder

        with open(annotations_path, 'r') as f:
            self.samples = json.load(f)

        np.random.shuffle(self.samples)

        self.data_generator = ImageDataGenerator(rotation_range=40,
                                                 width_shift_range=0.2,
                                                 height_shift_range=0.2,
                                                 shear_range=0.2,
                                                 zoom_range=0.2,
                                                 horizontal_flip=True,
                                                 fill_mode='nearest')
        self.words = list(vocab.keys())

    def __len__(self):
        return int(np.ceil(len(self.samples) / float(batch_size)))

    def __getitem__(self, idx):
        i = idx * batch_size

        length = min(batch_size, (len(self.samples) - i))
        batch_x = []
        batch_y = np.empty((length, max_token_length, 1), dtype=np.int32)

        for i_batch in range(length):
            sample = self.samples[i]
            image_id = sample['image_id']
            img_path = os.path.join(self.image_folder, image_id)
            img = load_img(img_path, target_size=(img_rows, img_cols))
            img_array = img_to_array(img)
            img_array = self.data_generator.random_transform(img_array)
            img_array = keras.applications.resnet50.preprocess_input(img_array)
            image_input = np.array(img_array[0])

            caption = sample['caption']
            c = caption[0]
            seg_list = jieba.cut(c)
            text_input = np.zeros((max_token_length, 1), dtype=np.int32)
            target = np.zeros((max_token_length, 1), dtype=np.int32)
            # Ignore the UNK word
            token_list = []
            for word in enumerate(seg_list):
                if word in self.words:
                    token_list.append(word)

            for index, word in enumerate(token_list):
                position = self.words.index(word)
                target[index] = position
                text_input[index + 1] = position

            batch_x.append([text_input, image_input])
            batch_y[i_batch, :, :] = target

            i += 1

        return batch_x, batch_y

    def on_epoch_end(self):
        np.random.shuffle(self.samples)


def train_gen():
    return DataGenSequence('train')


def valid_gen():
    return DataGenSequence('valid')
