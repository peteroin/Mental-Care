# utils/dataset.py
import os
import cv2
from torch.utils.data import Dataset
from .transforms import train_transform, test_transform

EMOTIONS = {
    'angry': 0, 'disgust': 1, 'fear': 2, 'happy': 3,
    'neutral': 4, 'sad': 5, 'surprise': 6
}

class FERDataset(Dataset):
    def __init__(self, data_dir, transform='train'):
        self.images = []
        self.labels = []
        self.transform = train_transform if transform == 'train' else test_transform

        for emotion, label in EMOTIONS.items():
            path = os.path.join(data_dir, emotion)
            if not os.path.exists(path):
                continue
            for img_file in os.listdir(path):
                self.images.append(os.path.join(path, img_file))
                self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = cv2.imread(self.images[idx], cv2.IMREAD_GRAYSCALE)
        if self.transform:
            image = self.transform(image)
        return image, self.labels[idx]
