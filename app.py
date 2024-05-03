from flask import Flask, render_template, request, flash, jsonify
from db import db
import google.generativeai as genai

app = Flask(__name__)

@app.route('/')
def index():
    data = db.readdata()
    return render_template("index.html",name=data.name, top=data.top, bottom=data.bottom, others=data.others)

def execute_prompt(prompt):
    api_key="AIzaSyB1gjKQMpLKeL6ED2Pyqlry8OWZHlgfxdw"
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text

@app.route('/suggest', methods=['GET','POST'])
def suggest():
    data = db.readdata()
    output = "" 
    if request.method == 'POST':
        occasion = request.form.get('occasion')
        style = request.form.get('style')
        colleaguedetails = request.form.get('colleaguedetails')
        otherinfo = request.form.get('otherinfo')
        if otherinfo == "":
            prompt = f"Hey, I am {data.name} and a {data.occupation} by profession,  I am going out with one of my colleagues whose information is provided here: {colleaguedetails}. I have these clothes in my inventory: {data.top} for topwear, {data.bottom} for bottomwear and {data.others} as shoes and accessories. I am going to a {occasion} along with my colleague. Suggest me the best outfit with accessories and shoes for me based on my inventory which I provided to you. I am willing to wear {style} style clothes."
        else:
            prompt = f"Hey, I am {data.name} and a {data.occupation} by profession,  I am going out with one of my colleagues whose information is provided here: {colleaguedetails}. I have these clothes in my inventory: {data.top} for topwear, {data.bottom} for bottomwear and {data.others} as shoes and accessories. I am going to a {occasion} along with my colleague. Suggest me the best outfit with accessories and shoes for me based on my inventory which I provided to you. I am willing to wear {style} style clothes. Here is some other important information which you need to take care of while suggesting me the outfits: {otherinfo}."
        output = execute_prompt(prompt=prompt)
        output = output.replace("**","")
    return render_template('output.html', suggestions=output)     


@app.route('/updatewardrobe', methods=['POST','GET'])
def updatewardrobe():
    if request.method == 'POST':
        top = request.form.get('top')
        bottom = request.form.get('bottom')
        others = request.form.get('others')
        flag=db.updatewardrobe(top, bottom, others)
        if flag == True:
            return render_template('index.html', output="Wardrobe Updated Successfully")
        else:
            return render_template('index.html', output="Some error occoured. Kindly try after some time.")
    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
