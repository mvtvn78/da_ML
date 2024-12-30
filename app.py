from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
loaded_model = None
# Tải mô hình từ file
with open('./model/xgmodel', 'rb') as f:
    loaded_model = pickle.load(f)
    print("Đã load mô hình thành công")

#Main route
@app.route("/predict", methods=["POST"])
def predict():
     if request.method == 'POST':
            checkbox_values = [0]*86
            for i in range(86):
                getCheckBox =  request.form.get(f'check{i}', '0') 
                valueCheckBox = 0 if getCheckBox =='0' else 1
                checkbox_values[i] = valueCheckBox
            
            for index,value in enumerate(checkbox_values):
                 print(index,value,end=' ',sep=":")
            prediction=loaded_model.predict([checkbox_values])
            print()
            print("Dự đoán: ", prediction[0])
            return render_template("predict.html",pred=prediction[0])
     else:
         pass
@app.route('/')
def index():
    return render_template('index.html')
#
if __name__ == '__main__':
    app.run(debug=True)