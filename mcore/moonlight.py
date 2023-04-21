from ultralytics import YOLO
from .cpaddle import PaddleModel
from ultralytics.yolo.utils.plotting import Annotator
import cv2
import os

model_path = os.path.join(os.path.dirname(__file__), 'models','best.pt')


class MoonLight:
    def __init__(self):
        self.model = YOLO(model_path)
        self.ocr_model = PaddleModel()

    def detect(self, img):
        results = self.model.predict(img)
        
        for r in results:
            annotator = Annotator(img)
            
        boxes = r.boxes
        number_plates = []
        
        for box in boxes:
            b = box.xyxy[0].int() 
            print("bounding box: ", b)
            number_plate = self.ocr_model.detect(img[b[1]:b[3], b[0]:b[2]])
            number_plates.append(number_plate)
            annotator.box_label(b, str(number_plate))
        
        frame = annotator.result()  
        cv2.imwrite("frame.jpg", frame)
        
        return frame, number_plates

    
