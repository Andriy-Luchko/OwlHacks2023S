from flask import Flask, render_template
import os 
from flask import redirect, abort, request, url_for
from main import FindBestPath, VolunteersInEachCity
app = Flask(__name__)
picFolder = os.path.join('static', 'pics')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder

@app.route("/",methods = ['POST','GET'])
def GetInput():
    SampleSize=request.args.get('SampleSize')
    if request.args.get('HIV')=='on':
        return redirect(url_for("HIV",SampleSize=SampleSize))
    if request.args.get('CANCER')=='on':
        return redirect(url_for("CANCER",SampleSize=SampleSize))
    if request.args.get('alzheimers')=='on':
        return redirect(url_for("alzheimers",SampleSize=SampleSize))
    return render_template('index.html')
@app.route("/HIV/<SampleSize>")
def HIV(SampleSize):
    result = FindBestPath("HIV",int(SampleSize))
    dist=int(result[1])
    final = list(result)
    del final[1]
    VEC=VolunteersInEachCity(result,"HIV")
    return render_template("hiv.html",Path=final,dist=dist,VEC=VEC)
@app.route("/CANCER/<SampleSize>")
def CANCER(SampleSize):
    result = FindBestPath("CANCER",int(SampleSize))
    dist=int(result[1])
    final = list(result)
    del final[1]
    VEC=VolunteersInEachCity(result,"CANCER")
    return render_template("cancer.html",Path=final,dist=dist,VEC=VEC)
@app.route("/alzheimers/<SampleSize>")
def alzheimers(SampleSize):
    result = FindBestPath("ALZHEIMERS",int(SampleSize))
    dist=int(result[1])
    final = list(result)
    del final[1]
    VEC=VolunteersInEachCity(result,"ALZHEIMERS")
    return render_template("altz.html",Path=final,dist=dist,VEC=VEC)

app.run(host='localhost', port=5000)