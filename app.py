from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# جمل متنوعة وجديدة
sentences = [
    "البرمجة هي لغة العصر والمستقبل القريب.",
    "الإصرار على النجاح هو أول خطوة في طريق القمة.",
    "تعلم لغات البرمجة يفتح لك آفاقاً جديدة في العمل.",
    "الممارسة المستمرة تجعلك مبرمجاً محترفاً وسريعاً.",
    "بايثون لغة سهلة وممتعة للمبتدئين والمحترفين."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sentence')
def get_sentence():
    # بيبعت جملة عشوائية للموقع
    return jsonify({"text": random.choice(sentences)})

if __name__ == '__main__':
    app.run(debug=True)