# models/resnet18_emotion.py
import torch.nn as nn
from torchvision.models import resnet18

def create_resnet18_model(num_classes=7):
    model = resnet18(weights='IMAGENET1K_V1')

    # Modify for grayscale input
    original_conv = model.conv1.weight.data
    model.conv1 = nn.Conv2d(1, 64, kernel_size=7, stride=2, padding=3, bias=False)
    model.conv1.weight.data = original_conv.mean(dim=1, keepdim=True)

    # Freeze layers
    for name, param in model.named_parameters():
        param.requires_grad = any(layer in name for layer in ['layer3', 'layer4', 'fc'])

    # Replace classifier
    model.fc = nn.Sequential(
        nn.Dropout(0.5),
        nn.Linear(model.fc.in_features, num_classes)
    )

    return model
