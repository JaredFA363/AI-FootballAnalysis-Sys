from ultralytics import YOLO

model = YOLO('yolov8m')

#Object detection in video
results = model.predict('InputVideos/test-1.mp4', save=True)
print(results[0])
print('=====================')
for boundBox in results[0].boxes:
    print(boundBox)