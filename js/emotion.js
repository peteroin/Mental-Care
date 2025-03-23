const video = document.getElementById("video");
const emotionResult = document.getElementById("emotion-result");

// Load models from local directory
async function loadModels() {
    const modelPath = "../models"; // Adjust if needed
    await faceapi.nets.tinyFaceDetector.loadFromUri(modelPath);
    await faceapi.nets.faceExpressionNet.loadFromUri(modelPath);
    startVideo();
}

// Start webcam
function startVideo() {
    navigator.mediaDevices.getUserMedia({ video: true })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((err) => console.error("Error accessing webcam:", err));
}

// Real-time emotion detection
video.addEventListener("play", async () => {
    const canvas = faceapi.createCanvasFromMedia(video);
    video.parentNode.append(canvas);

    const displaySize = { width: video.videoWidth, height: video.videoHeight };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
        const detections = await faceapi
            .detectAllFaces(video, new faceapi.TinyFaceDetectorOptions())
            .withFaceExpressions();
        
        const ctx = canvas.getContext("2d");
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        faceapi.draw.drawDetections(canvas, detections);
        faceapi.draw.drawFaceExpressions(canvas, detections);

        if (detections.length > 0) {
            let emotions = detections[0].expressions;
            let topEmotion = Object.keys(emotions).reduce((a, b) => emotions[a] > emotions[b] ? a : b);
            emotionResult.innerText = `Emotion Detected: ${topEmotion}`;
        } else {
            emotionResult.innerText = "No face detected!";
        }
    }, 1000);
});

// Load models and start everything
loadModels();
