
import os
import json
import glob

def modify_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    labels_to_modify = [
        "Single_Solid_Yellow_Line", "Single_Solid_White_Line",
        "Single_Stripe_Yellow_Line", "Single_Stripe_White_Line",
        "Double_Solid_Yellow_Line", "Double_Solid_White_Line",
        "Double_Combined_White_Line", "Double_Combined_Yellow_Line",
        "Short_Dashed_White_Line", "Speed_Bump",
        "Stop_Line", "No_Parking_Road_Side_Red", "Short_Parking_Road_Side_Yellow"
    ]

    def modify_points(shape):
        if len(shape['points']) > 2:
            if shape['label'] in labels_to_modify:
                shape['points'].extend(reversed(shape['points'][1:-1]))
        

    if 'shapes' in data:
        for shape in data['shapes']:
            modify_points(shape)

        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)

directory_path = os.getcwd()
json_files = glob.glob(os.path.join(directory_path, '*.json'))

for json_file in json_files:
    modify_json_file(json_file)
