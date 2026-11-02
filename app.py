from flask import Flask, render_template

app = Flask(__name__)

# 每筆電影包含作業要求的三個欄位；修改這裡即可更新首頁。
movies = [
    {"title": "腦筋急轉彎", "genre": "動畫", "reason": "把快樂、悲傷與成長變成一場冒險。適合想用溫柔的故事，重新認識自己情緒的時候觀看。"},
    {"title": "星際效應", "genre": "科幻", "reason": "從宇宙探索談到時間與親情。推薦給喜歡宏大場景，也喜歡在故事結束後繼續思考的人。"},
    {"title": "神隱少女", "genre": "奇幻動畫", "reason": "跟著千尋走進陌生世界，看見勇氣、善意與成長。細膩的畫面讓每次重看都有新的發現。"},
]

@app.get("/")
def index():
    # 將 Python 資料交給 templates 資料夾中的 Jinja2 模板。
    return render_template("index.html", movies=movies)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    # 本機測試用；Render 以 Gunicorn 啟動，不使用此開發伺服器。
    app.run(host="127.0.0.1", port=5000)
