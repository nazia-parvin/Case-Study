import os 
import json
#to read from the folder
path_to_json_files = '/Users/macbook/Downloads/CaseStudy/sampleJson'
#get all JSON file names as a list
json_file_names = [filename for filename in os.listdir(path_to_json_files)if filename.endswith('.json')]

for json_file_name in json_file_names:
    #joins various path components
    with open(os.path.join(path_to_json_files, json_file_name)) as json_file:
        json_text = json.load(json_file)
        print(json_file_name, json_text)


#to merge the (Pos_0.png.json,Pos_10010.png.json, Pos_10492.png.json) files
        
file_list = [ 
    '/Users/macbook/Downloads/CaseStudy/sampleJson/pos_0.png.json', 
    '/Users/macbook/Downloads/CaseStudy/sampleJson/pos_10010.png.json',
    '/Users/macbook/Downloads/CaseStudy/sampleJson/pos_10492.png.json'
]
all_data_dict = []
for json_file in file_list:
       with open(json_file,'r+') as file:
           #First we load existing data into a dict.
           file_data = json.load(file)
           for obj in file_data['objects']:
            if('classTitle' in obj.keys()):
              print(obj['classTitle'])
              if(obj['classTitle'].lower()) == 'vehicle':
                obj['classTitle'] = 'Car'
              elif(obj['classTitle']).lower() == 'license plate':
                 obj['classTitle'] = 'number'
           all_data_dict.append(file_data)
with open("/Users/macbook/Downloads/CaseStudy/combined_data.json", 'w') as outfile:# save to json file
        json.dump(all_data_dict, outfile)           