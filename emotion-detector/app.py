from flask import Flask, request, jsonify
import cv2
import numpy as np
import torch
from torchvision import transforms
from PIL import Image
from models.resnet18_emotion import create_resnet18_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

EMOTIONS = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
model = create_resnet18_model(num_classes=7)
model.load_state_dict(torch.load("best_model.pth", map_location=device)['model_state_dict'])
model.eval().to(device)

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485], std=[0.229])
])

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img = Image.open(file.stream).convert('L')  # Convert to grayscale
    img = transform(img).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(img)
        _, pred = torch.max(output, 1)
        emotion = EMOTIONS[pred.item()]

    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)
