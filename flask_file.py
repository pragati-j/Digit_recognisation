from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        file=request.get_data()
        convertImage

    return render_template('upload.html')

if __name__=="__main__":
    app.run(debug=True)
