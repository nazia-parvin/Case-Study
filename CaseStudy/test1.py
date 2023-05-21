import json
filename = '/Users/macbook/Downloads/CaseStudy/sampleJson/pos_10010.png.json'
f = open(filename, 'r')
data = json.load(f)
list = []

formatted_json = [{
        "dataset_name": "pos_10010.png",
        "image_link": "",
        "annotation_type": "image",
        "annotation_objects": {
            "vehicle": {
                "presence": 0,
                "bbox": []
            },
            "license_plate": {
                "presence": 0,
                "bbox": []
            }
        },
        "annotation_attributes": {
            "vehicle": {
                "Type": None,
                "Pose": None,
                "Model": None,
                "Make": None,
                "Color": None
            },
            "license_plate": {
                "Difficulty Score": None,
                "Value": None,
                "Occlusion": None
            }
        }
}]
Vehicle_bbox = []
License_bbox = []
with open("/Users/macbook/Downloads/CaseStudy/formatted_pos_10010.png.json", "a") as file:
    json.dump(formatted_json, file, indent = 4)