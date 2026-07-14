from flask import Flask, jsonify, render_template_string
import random

app = Flask(__name__)

dice = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

rolls = 0

html = """
<!DOCTYPE html>
<html>
<head>
<title>🎲 Dice Roller</title>

<style>

body{
    margin:0;
    font-family:Arial,Helvetica,sans-serif;
    background:linear-gradient(135deg,#667eea,#764ba2);
    display:flex;
    justify-content:center;
    align-items:center;
    height:100vh;
}

.container{

    width:420px;
    padding:30px;
    border-radius:20px;
    background:rgba(255,255,255,.15);
    backdrop-filter:blur(15px);
    text-align:center;
    color:white;
    box-shadow:0px 10px 25px rgba(0,0,0,.3);

}

h1{
    font-size:38px;
}

#dice{

    font-size:130px;
    transition:0.5s;

}

button{

    padding:15px 35px;
    font-size:20px;
    border:none;
    border-radius:10px;
    background:#ff9800;
    color:white;
    cursor:pointer;
    transition:.3s;

}

button:hover{

    background:#ff6f00;
    transform:scale(1.05);

}

#number{

    font-size:30px;
    margin-top:20px;

}

#count{

    margin-top:15px;
    font-size:18px;

}

</style>

</head>

<body>

<div class="container">

<h1>🎲 Dice Roller 🎲</h1>

<div id="dice">{{face}}</div>

<h2 id="number">You rolled : {{number}}</h2>

<p id="count">Total Rolls : {{count}}</p>

<button onclick="rollDice()">Roll Dice</button>

</div>

<script>

function rollDice(){

document.getElementById("dice").style.transform="rotate(360deg)";

fetch('/roll')

.then(response=>response.json())

.then(data=>{

setTimeout(function(){

document.getElementById("dice").innerHTML=data.face;

document.getElementById("number").innerHTML="You rolled : "+data.number;

document.getElementById("count").innerHTML="Total Rolls : "+data.count;

document.getElementById("dice").style.transform="rotate(0deg)";

},300);

});

}

</script>

</body>

</html>
"""

@app.route("/")
def home():

    global rolls

    rolls += 1

    number = random.randint(1,6)

    return render_template_string(
        html,
        number=number,
        face=dice[number],
        count=rolls
    )

@app.route("/roll")
def roll():

    global rolls

    rolls += 1

    number = random.randint(1,6)

    return jsonify({
        "number":number,
        "face":dice[number],
        "count":rolls
    })

if __name__=="__main__":
    app.run(debug=True)
