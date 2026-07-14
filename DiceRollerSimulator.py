from flask import Flask, render_template_string
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

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Dice Rolling Simulator</title>
    <style>
        body{
            font-family:Arial;
            text-align:center;
            background:linear-gradient(to right,#4facfe,#00f2fe);
            color:white;
            margin-top:60px;
        }

        .box{
            background:white;
            color:black;
            width:400px;
            margin:auto;
            padding:30px;
            border-radius:15px;
            box-shadow:0 0 10px gray;
        }

        .dice{
            font-size:120px;
        }

        button{
            padding:10px 25px;
            font-size:20px;
            background:orange;
            color:white;
            border:none;
            border-radius:10px;
            cursor:pointer;
        }

        button:hover{
            background:darkorange;
        }
    </style>
</head>

<body>

<div class="box">
<h1>🎲 Dice Roller 🎲</h1>

<div class="dice">{{ face }}</div>

<h2>You rolled: {{ number }}</h2>

<form>
<button type="submit">Roll Again</button>
</form>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    number = random.randint(1, 6)
    return render_template_string(
        html,
        number=number,
        face=dice[number]
    )

if __name__ == "__main__":
    app.run(debug=True)
