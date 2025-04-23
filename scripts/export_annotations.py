import json
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime

def json_to_csv(json_path):
    with open(json_path) as f:
        data = json.load(f)
    
    records = []
    for img_data in data['_via_img_metadata'].values():
        for region in img_data['regions']:
            records.append({
                'image': img_data['filename'],
                'tooth_id': region['region_attributes'].get('ToothID'),
                'condition': region['region_attributes'].get('Condition'),
                'x_points': ';'.join(map(str, region['shape_attributes']['all_points_x'])),
                'y_points': ';'.join(map(str, region['shape_attributes']['all_points_y']))
            })
    
    df = pd.DataFrame(records)
    output_path = json_path.replace('.json', '_annotations.csv')
    df.to_csv(output_path, index=False)
    return output_path

def json_to_coco(json_path):
    # Implement COCO format conversion here
    pass

if __name__ == '__main__':
    import sys
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'annotations/via_project.json'
    print(f"Annotations exported to: {json_to_csv(input_file)}")