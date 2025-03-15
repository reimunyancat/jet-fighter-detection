# jet-fighter-detection

This project uses the YOLOv8 model to detect jet fighters, specifically the SU-34 and F-16, in aerial images and videos. It has been trained to accurately identify these two types of fighter jets in various conditions.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Results](#results)
- [License](#license)

## Introduction

This project builds a system to detect SU-34 and F-16 fighter jets using the YOLOv8 (You Only Look Once) object detection model. YOLOv8 is the latest version of the YOLO model, known for its fast and efficient object detection capabilities. This model can detect fighter jets in real-time from aerial imagery or video streams.

## Features

- **YOLOv8-based Object Detection:** Trained YOLOv8 model for detecting SU-34 and F-16 fighter jets.
- **Real-time Detection:** Can process images and videos in real-time to detect fighter jets.
- **Tested on Various Aerial Images:** The model is capable of detecting SU-34 and F-16 jets in different environments and angles.

## Installation

To set up this project on your local machine, follow the steps below:

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/jet-fighter-detection.git
    cd jet-fighter-detection
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the main script:**

    To start detecting fighter jets in real-time from your monitor, run the following command:

    ```bash
    python main.py
    ```

2. **What happens when you run the script:**
   - The script will capture the video feed from your screen.
   - It will then use the YOLOv8 model to detect SU-34 and F-16 fighter jets.
   - When a fighter jet is detected, it will be highlighted with an overlay on the screen.
   - The system runs in real-time, providing immediate feedback as jets are detected.

3. **Exit the script:**
   - To stop the detection and exit the script, simply close the terminal or press `Ctrl+C`.

## Dataset

The dataset used to train the model includes images of **SU-34** and **F-16** fighter jets. You can download the dataset from Roboflow using the following command:

```bash
curl -L "https://universe.roboflow.com/ds/YsyiQRYD5D?key=TbbcBQyDOy" > roboflow.zip; unzip roboflow.zip; rm roboflow.zip
```
This will download and extract the dataset. The dataset contains various labeled images of SU-34 and F-16 jets in different environments and angles.


## Results

The results are not satisfactory yet because the dataset is absolutely insufficient. We plan to supplement it and upload it later.


## License
This project is licensed under the [MIT License](LICENSE).
