import os
import sys
import random
from flask import Flask, render_template, jsonify

# التعديل ده عشان لما تحوله لـ .exe يعرف يشوف الملفات
if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__)

# قائمة الجمل المتنوعة
sentences = [
    "البرمجة هي لغة العصر والمستقبل القريب.",
    "تعلم لغات البرمجة يفتح لك آفاقاً جديدة.",
    "الممارسة المستمرة تجعلك مبرمجاً محترفاً.",
    "السرعة والدقة هما مفتاح النجاح في هذا السباق.",
    "كل يوم هو فرصة جديدة لتعلم شيء مذهل.",
    "بايثون هي أسهل لغة لبناء تطبيقات الويب."
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_sentence')
def get_sentence():
    return jsonify({"text": random.choice(sentences)})

if __name__ == '__main__':
    # بورت 5000 ده اللي هنفتحه في المتصفح
    app.run(debug=True, port=5000)