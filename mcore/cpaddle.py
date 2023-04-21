from paddleocr import PaddleOCR

class PaddleModel:
    def __init__(self):
        self.ocr_model = PaddleOCR(lang='en')

    def detect(self, img):
        result = self.ocr_model.ocr(img)
        texts = [res[1][0] for res in result[0]]
        
        if len(texts) == 0:
            return "Unknown"

        return texts[0]
        

        

