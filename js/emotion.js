const video = document.getElementById("video");
const emotionResult = document.getElementById("emotion-result");

// Load models from Face-API.js
async function loadModels() {
    await faceapi.nets.tinyFaceDetector.loadFromUri("https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/");
    await faceapi.nets.faceExpressionNet.loadFromUri("https://raw.githubusercontent.com/justadudewhohacks/face-api.js/master/weights/");
    startVideo();
}

// Start the webcam video stream
function startVideo() {
    navigator.mediaDevices.getUserMedia({ video: {} })
        .then((stream) => {
            video.srcObject = stream;
        })
        .catch((err) => console.error("Error accessing webcam:", err));
}

// Run emotion detection in real-time
video.addEventListener("play", async () => {
    const canvas = faceapi.createCanvasFromMedia(video);
    document.body.append(canvas);
    const displaySize = { width: video.width, height: video.height };
    faceapi.matchDimensions(canvas, displaySize);

    setInterval(async () => {
        const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceExpressions();
        
        if (detections.length > 0) {
            let emotions = detections[0].expressions;
            let topEmotion = Object.keys(emotions).reduce((a, b) => emotions[a] > emotions[b] ? a : b);
            emotionResult.innerText = `Emotion Detected: ${topEmotion}`;
        } else {
            emotionResult.innerText = "No face detected!";
        }
    }, 1000);
});

// Load models and start
loadModels();
