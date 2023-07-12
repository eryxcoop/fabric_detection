import cv2
from ultralytics import YOLO

cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

model = YOLO('yolo_model_prototype_6_covers_july23.pt')


def image_with_top_predictions(result, class_names):
    font = cv2.FONT_HERSHEY_SIMPLEX
    base_scale = 1.0
    color = (0, 255, 0)
    thickness = 1
    image = result.orig_img
    top_class_prediction_indices = result.probs.top5
    top_class_prediction_confidences = result.probs.top5conf
    for i in range(3):
        prediction_index = top_class_prediction_indices[i]
        prediction_class_name = class_names[prediction_index]
        prediction_confidence = top_class_prediction_confidences[i].item()
        text_for_prediction = f"{prediction_class_name}: {prediction_confidence:.2f}"
        size_for_prediction = base_scale / (i + 1)
        cv2.putText(image, text_for_prediction, (50, 50 + 20 * i), font, size_for_prediction, color, thickness)
    return image


while True:
    ret, img = cap.read()
    results = model.predict(img, device='cpu')
    class_names = results[0].names
    for result in results:
        image_to_show = image_with_top_predictions(result, class_names)
        cv2.imshow('Webcam', image_to_show)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
