import cv2
import os
import json

def annotate_all_images(processed_dir, annotated_dir, json_dir):
    os.makedirs(annotated_dir, exist_ok=True)
    os.makedirs(json_dir, exist_ok=True)

    # Initialize dictionaries for both AI-compatible and VIA-compatible annotations
    ai_annotations = []
    via_annotations = {}

    for f in os.listdir(processed_dir):
        if f.lower().endswith(('.jpg', '.png', '.jpeg')):  # Process image files
            path = os.path.join(processed_dir, f)
            img = cv2.imread(path)
            h, w = img.shape[:2]

            label = "tooth"
            new_filename = f"{os.path.splitext(f)[0]}_{label}.jpg"
            out_path = os.path.join(annotated_dir, new_filename)

            # Dummy annotation (green rectangle)
            x1, y1, x2, y2 = w // 4, h // 4, w * 3 // 4, h * 3 // 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imwrite(out_path, img)

            # AI-Compatible JSON: Collect image filename and bounding box for training
            ai_annotations.append({
                "filename": new_filename,
                "bounding_boxes": [
                    {
                        "x1": x1,
                        "y1": y1,
                        "x2": x2,
                        "y2": y2,
                        "label": label
                    }
                ]
            })

            # VIA-Compatible JSON: Prepare via format with regions and shape attributes
            via_annotations[new_filename] = {
                "filename": new_filename,
                "size": os.path.getsize(out_path),
                "regions": [
                    {
                        "shape_attributes": {
                            "name": "rect",
                            "x": x1,
                            "y": y1,
                            "width": x2 - x1,
                            "height": y2 - y1
                        },
                        "region_attributes": {
                            "label": label
                        }
                    }
                ]
            }

            print(f"Annotated and renamed: {new_filename}")

    # Save AI-compatible JSON
    ai_json_path = os.path.join(json_dir, "ai_annotations.json")
    with open(ai_json_path, 'w') as ai_jf:
        json.dump(ai_annotations, ai_jf, indent=4)

    # Save VIA-compatible JSON
    via_json_path = os.path.join(json_dir, "via_annotations.json")
    with open(via_json_path, 'w') as via_jf:
        json.dump(via_annotations, via_jf, indent=4)

    print("✅ Annotation complete and saved in JSON.")
