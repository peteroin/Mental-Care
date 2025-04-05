# predict.py
import cv2
import torch
from models.resnet18_emotion import create_resnet18_model
from utils.transforms import test_transform
from utils.dataset import EMOTIONS

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def load_model(model_path):
    model = create_resnet18_model()
    checkpoint = torch.load(model_path, map_location=device)
    model.load_state_dict(checkpoint['model_state_dict'])
    model.to(device)
    model.eval()
    return model

def predict_emotion(image_path, model):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    image = test_transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        emotion = list(EMOTIONS.keys())[predicted.item()]
        return emotion

# Example usage
if __name__ == "__main__":
    model = load_model("best_model.pth")
    print(predict_emotion("data/fer2013/test/angry/PrivateTest_88305.png", model))
