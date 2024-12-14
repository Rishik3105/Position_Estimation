# Pose Detection using OpenCV and MediaPipe 💃⛷

Welcome to the **Pose Detection** project! 📏 This project uses **OpenCV** and **MediaPipe** to detect human body poses in real-time from a webcam feed. It's a great demonstration of real-time landmark tracking and computer vision techniques! ✨

---

## 🌟 Key Features
- ⚡ **Real-Time Pose Detection**: Detect human pose landmarks in real-time.
- 🌿 **Landmark Visualization**: Visualize pose landmarks and connections on the live video feed.
- ⏰ **FPS Counter**: Monitor real-time performance with the frames-per-second (FPS) display.
- ✨ **Customizable Design**: Easily modify line colors, thickness, and circle radius.
- 💡 **User-Friendly Interface**: Press `q` to exit the live video stream.

---

## 🔧 Technologies Used

- **Python** ✨
- **OpenCV** 🏋️
- **MediaPipe** ⛷
- **Real-Time Video Processing** 🛠️

---

## 📚 Code Overview

The project captures video from your webcam and processes it using MediaPipe's Pose detection module. Pose landmarks (33 in total) are drawn on the detected person in real-time with custom styles for circles and connecting lines.

### Key Code Sections:
1. **Capture Video**: OpenCV handles video input using `cv.VideoCapture`.
2. **Pose Detection**: MediaPipe processes each video frame for pose landmarks.
3. **FPS Calculation**: Monitor the system performance using FPS.
4. **Landmark Drawing**: Draw pose landmarks and connections using custom styles.

---

## 🛠️ Installation

To run this project, ensure you have the following dependencies installed:

```bash
pip install opencv-python mediapipe
```

---

## 👨‍💻 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pose-detection
   cd pose-detection
   ```
2. Run the script:
   ```bash
   python pose_detection.py
   ```
3. Press **`q`** to exit the video stream.

---

## 🎥 Demo

Watch the project in action:

<img src="https://via.placeholder.com/600x300.png?text=Pose+Detection+Demo" alt="Pose Detection Demo GIF" width="600px" />

---

## 🎉 Output

The project will display:
1. Real-time pose landmarks with lines (green) and circles (red).
2. FPS displayed at the top-left corner.

---

## 🛡 Customization

You can tweak the following settings in the code:

```python
# Customize drawing styles
line_spec = mpdraw.DrawingSpec(color=(0, 255, 0), thickness=3)  # Line color: Green
circle_spec = mpdraw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=5)  # Circle color: Red
```

---

## 🛠️ Troubleshooting

- **Camera feed not available**: Ensure your webcam is connected and working.
- **Low FPS**: Try reducing video resolution for better performance.

---

## 💡 Ideas for Improvement
Feel free to enhance the project with the following ideas:
- Add a **recording feature** to save pose-detected videos.
- Integrate **gesture recognition** using detected pose landmarks.
- Optimize for performance using multi-threading or GPU support.

---

## 📢 Let's Stay Connected!

📧 [Email](mailto:nimmanirishik@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/nimmani-rishik-66b632287)  
🐝 [GitHub](https://github.com/yourusername)  
📷 [Instagram](https://instagram.com/rishik_3142)

---

## 💪 Contributing

Contributions are always welcome! Feel free to fork this repository and submit a pull request. ✨

---

## 🌟 Acknowledgments

Thanks to **MediaPipe** and **OpenCV** for providing the tools that make this project possible. 📊

---

## 📜 License

This project is licensed under the MIT License © Nimmani Rishik.

---

### 👋 Thank You!

Hope you enjoy using this project! If you like it, please give it a ⭐ **star** and share it with others. 💙

---

