from ultralytics import YOLO

model = YOLO(r"C:/Unihack2025/ObDetector/venv/runs/detect/trainFaraLateral/weights/best.pt")

results = model.train(
    data="config.yaml",
    epochs=200,
    imgsz=960,
    batch=16,
    device=0,
    workers=8,
    cache=True,
    patience=30,
    optimizer="AdamW",
    lr0=0.001,
    weight_decay=0.0005,
    cos_lr=True,
    close_mosaic=10,
    plots=True,
    amp=True
)

metrics = model.val()
print(metrics)
