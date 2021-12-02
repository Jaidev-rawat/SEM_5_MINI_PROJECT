from flask import Flask,render_template,request

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os
import numpy as np
import math
from PIL import Image

app = Flask(__name__)
app.secret_key = "5"

app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
model=load_model(r'static/back.h5')
categories=[['aloo_mix','86 cal per 100 gram'],['aloo_tikki','144 cal per piece'],['banana','89 cal per 100 gram'],['bhindi_masala','112 calories in 100 grams'],['burger','300 calories in normal burger'],
['chai','100 calories per cup'],['chana_masala','320 calories per cup'],['chapatti','70 calories per chapatti'],['chole_bhature','500 calories per plate'],['dahi_vada','200 calories per plate'],
['dal_makhani','270 calories per cup'],['dal_tadka','211 calories per cup'],['eggs','60 calories per egg'],['fried_rice','228 calories per cup'],['gulab jamun','200 calories per piece'],['halwa','400 calories per katori'],['icecream','170 calories per scoop'],
['idli','50 calories per piece'],['jalebi','60 calories per piece'],['kaathi_rolls','150 calories per roll'],['kadhi_pakoda','150 calories per katori'],
['mangoes','270 calories per fruit'],['masala_dosa','250 calories per plate'],['meduvada','100 calories per vada'],['momos','40 calories per momo'],['naan','100 calories per piece'],['noodles','130 calories per katori'],['oranges','78 calories per fruit'],
['paani_puri','15 calories per piece'],['pakode','20 calories per piece'],['paneer','120 calories per katori'],['pav_bhaji','350 calories per plate'],['pizza','500 calories per pizza'],['poori','50 calories per poori'],['rasgulla','70 calories per piece'],
['refreshing_drink','30 calories per glass'],['rice','120 calories  per katori'],['samosa','150 calories per piece'],['tandoori chicken','200 calories per piece'],['toast','58 calories per piece']]
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload',methods=["POST"])
def upload():
    if request.method=="POST":

        img=request.files["file"]
        img = Image.open(img).convert("RGB")
        im = img.resize((224, 224))
        #if save
        #filename=secure_filename(img.filename)
        #img.save(filename)
        #img=image.load_img(filename,target_size=(224,224))
        

        my_dict ={}
        x=image.img_to_array(im)
        x=x/255
        #y= np.expand_dims(x, axis=0)
        images = np.vstack([[x]])
        classes = model.predict(images, batch_size=1)
        i=0
        for k in classes[0]:
            m=float(f"{k:20f}")
    
            m=m*100
            m=round(m, 1)
            if i<40:
                my_dict[i]=m
            i=i+1
        #print(my_dict)
        markdict=my_dict
        mt = sorted(markdict.items(), key=lambda x:x[1],reverse=True)
        flist=[mt[0][1],categories[mt[0][0]][0],categories[mt[0][0]][1],mt[1][1],categories[mt[1][0]][0],categories[mt[1][0]][1],mt[2][1],categories[mt[2][0]][0],categories[mt[2][0]][1],
        mt[3][1],categories[mt[3][0]][0],categories[mt[3][0]][1],mt[4][1],categories[mt[4][0]][0],categories[mt[4][0]][1],mt[5][1],categories[mt[5][0]][0],categories[mt[5][0]][1]]
        
        
        
        
        
        return render_template("display.html",y=flist)
if __name__ == ('__main__'):
    app.run(host="0.0.0.0",port=8088,debug=True)
