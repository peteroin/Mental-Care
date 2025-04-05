# utils/transforms.py
from torchvision import transforms as T
from PIL import Image

train_transform = T.Compose([
    T.Lambda(lambda x: Image.fromarray(x)),
    T.Resize((224, 224)),
    T.RandomHorizontalFlip(),
    T.RandomRotation(10),
    T.ToTensor(),
    T.Normalize(mean=[0.485], std=[0.229])
])

test_transform = T.Compose([
    T.Lambda(lambda x: Image.fromarray(x)),
    T.Resize((224, 224)),
    T.ToTensor(),
    T.Normalize(mean=[0.485], std=[0.229])
])
