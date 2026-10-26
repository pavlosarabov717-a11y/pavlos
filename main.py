from flask import Flask#eto biblioteka dlia sosdania saitov
import random#bibliotecka dlia randoma
app = Flask(__name__)#peremenoia veb servera

code = """ 
    <h1>Добро пожаловать в Brawl Stars</h1>
    <p>Эта игра для друзей. В ней можно сражаться. Можно играть в нее одному. </p>
    <i>Цель игры:</i>
    <b>Получить много кубков и накопить кристаллы и выбить бравлеров</b>
    <img src="https://tse2.mm.bing.net/th/id/OIP.UpaFsvzLWll6j6EBEwlE9QHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3" width=500px heigth=400px>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRfJ697krUbyA6aaJrdigfu5_bmtHWuVYNt_Km6I1UpkpiFePiThqak240X&s=10" alt = "картинки нет" width=500px height=400px>
"""

@app.route("/")#sosdania morshyta
def main_page():
    return code

app.run(debug=True)
