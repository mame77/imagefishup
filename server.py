import cv2
import datetime
import numpy as np
from flask import Flask,render_template,request
app=Flask(__name__)


@app.route('/',methods=["GET","POST"])
def sizeUp():
    img_dir="static/fish.imgs/"
    img_path=None
    out_path=None
    if request.method == 'POST':
        try:
            #POSTにより受信した画像を読み込む
            stream = request.files['img'].stream
            img_array = np.asarray(bytearray(stream.read()),dtype=np.uint8)

            #画像が格納されていれば、後段の処理に進む
            if not len(img_array)==0:
                img = cv2.imdecode(img_array,1)

                #ファイル名を現在時刻とし「static/fish.imgs/に保存する」
                dt_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                img_path = img_dir + dt_now + ".jpg"
                out_path = img_dir + dt_now + "_sizeup" + ".jpg"
                cv2.imwrite(img_path, img)
            else:
                #画像が格納されていなければNoneを設定する
                img_path=None
                out_path=None
        except Exception as e:
            #エラー処理
            print('エラー発生')
            print(e)
            img_path=None
            out_path=None
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)