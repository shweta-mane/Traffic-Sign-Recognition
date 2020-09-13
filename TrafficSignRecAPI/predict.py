from tensorflow.keras.models import load_model
from PIL import Image
import numpy
from flask_cors import CORS
import flask
import io 
import numpy as np

app = flask.Flask(__name__) 
CORS(app)
model = None

@app.route('/')
def hello():
    return 'Hello World!'

class_indices = {0:'0',1:'1',2:'10',3:'11',4:'12',5:'13',6:14,7:'15',8:'16',9:'17',10:'18',11:'19'
,12:'2',13:'20',14:'21',15:'22',16:'23',17:'24',18:'25',19:'26',20:'27',21:'28',22:'29',23:'3',24:'30'
,25:'31',26:'32',27:'33',28:'34',29:'35',30:'36',31:'37',32:'38',33:'39',34:'4',35:'40',36:'41',37:'42'
,38:'5',39:'6',40:'7',41:'8',42:'9'}

classes = { 1:'Speed limit (20km/h)',
            2:'Speed limit (30km/h)', 
            3:'Speed limit (50km/h)', 
            4:'Speed limit (60km/h)', 
            5:'Speed limit (70km/h)', 
            6:'Speed limit (80km/h)', 
            7:'End of speed limit (80km/h)', 
            8:'Speed limit (100km/h)', 
            9:'Speed limit (120km/h)', 
            10:'No passing', 
            11:'No passing veh over 3.5 tons', 
            12:'Right-of-way at intersection', 
            13:'Priority road', 
            14:'Yield', 
            15:'Stop', 
            16:'No vehicles', 
            17:'Veh > 3.5 tons prohibited', 
            18:'No entry', 
            19:'General caution', 
            20:'Dangerous curve left', 
            21:'Dangerous curve right', 
            22:'Double curve', 
            23:'Bumpy road', 
            24:'Slippery road', 
            25:'Road narrows on the right', 
            26:'Road work', 
            27:'Traffic signals', 
            28:'Pedestrians', 
            29:'Children crossing', 
            30:'Bicycles crossing', 
            31:'Beware of ice/snow',
            32:'Wild animals crossing', 
            33:'End speed + passing limits', 
            34:'Turn right ahead', 
            35:'Turn left ahead', 
            36:'Ahead only', 
            37:'Go straight or right', 
            38:'Go straight or left', 
            39:'Keep right', 
            40:'Keep left', 
            41:'Roundabout mandatory', 
            42:'End of no passing', 
            43:'End no passing veh > 3.5 tons' }

def prepare_image(image): 
    if image.mode != "RGB": 
        image = image.convert("RGB")

    image = image.resize((32,32))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    image = image.astype("float32") / 255.0
      
    return image

@app.route("/trafficsignrecapi/predict", methods =["POST"]) 
def predict(): 
    data = {} 
  
    if flask.request.method == "POST": 
        if flask.request.files.get("image"): 
           
            image = flask.request.files["image"].read() 
            image = Image.open(io.BytesIO(image)) 

            image = prepare_image(image) 
            
            pred = model.predict_classes([image])[0]
            pred_prob = model.predict(image)
            x=max(pred_prob)
            y=max(x)
           
            print('pred prob', y)

            class_id = int(class_indices[pred])
            image_class = classes[class_id+1]
            

            data["image_class"] = image_class
            data["prob"] = str(y)
  
    return flask.jsonify(data)

if __name__ == "__main__": 
    print("Loading  model and starting Flask server...") 
    model = load_model('TrafficSignRecModel.h5')
    app.run(host='0.0.0.0', port=80)



