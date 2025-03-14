from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

model.train(
    data="data.yaml",
    epochs=100,
    batch=32,
    imgsz=640,
    workers=4,
    device="cuda:1"
)

results = model.val()
print(results)
model.save("model/best.pt")