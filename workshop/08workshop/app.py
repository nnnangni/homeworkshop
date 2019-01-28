from flask import Flask , render_template   
app = Flask(__name__)

@app.route("/dictionary/<string:word>")
def dictionary(word):
    dict = {'apple':'사과','banana':'바나나','melon':'멜론','cherry':'체리','orange':'오렌지'}
    # dict.get("apple") 가능
    
    # result = mydict.get(word)
    # if result:
    #     result = f"{word}은(는) {result}!"
    # else:
    #     result = f"{word}은(는) 단어장에 없는 단어입니다."
    
    # return result
    
    if word in dict:
        mean = dict[word]
    else:
        mean = "나만의 단어장에 없는 단어입니다."
    return render_template("dictionary.html",word=word, mean=mean)

    
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
    
