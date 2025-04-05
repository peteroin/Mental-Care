# train.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.optim.lr_scheduler import ReduceLROnPlateau
from models.resnet18_emotion import create_resnet18_model
from utils.dataset import FERDataset
import os

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_data = FERDataset("data/fer2013/train", transform='train')
val_data = FERDataset("data/fer2013/test", transform='val')

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
val_loader = DataLoader(val_data, batch_size=64, shuffle=False)

model = create_resnet18_model().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW([
    {'params': model.conv1.parameters(), 'lr': 1e-4},
    {'params': model.layer3.parameters(), 'lr': 3e-4},
    {'params': model.layer4.parameters(), 'lr': 5e-4},
    {'params': model.fc.parameters(), 'lr': 1e-3}
], weight_decay=0.01)

scheduler = ReduceLROnPlateau(optimizer, mode='min', factor=0.5, patience=2)

best_acc = 0
for epoch in range(15):
    model.train()
    correct = 0
    total = 0
    for imgs, labels in train_loader:
        imgs, labels = imgs.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(imgs)
        loss = criterion(outputs, labels)
        loss.backward()
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
        optimizer.step()

        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    acc = correct / total

    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for imgs, labels in val_loader:
            imgs, labels = imgs.to(device), labels.to(device)
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            val_loss += loss.item()

    scheduler.step(val_loss)
    print(f"Epoch {epoch+1}: Train Acc = {acc:.4f}, Val Loss = {val_loss:.4f}")

    if acc > best_acc:
        best_acc = acc
        torch.save({'model_state_dict': model.state_dict()}, "best_model.pth")
        print("✅ New best model saved!")

print("🎉 Training Complete")
