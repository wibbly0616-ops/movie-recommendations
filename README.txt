電影推薦網站：Flask + Jinja2 templates

本專案目前只是程式碼，尚未部署，也尚未產生正式 URL。
每筆電影有 title、genre、reason 三個欄位。

檔案：
app.py：Flask 後端與三筆電影範例
requirements.txt：部署所需套件
render.yaml：Render Blueprint 設定（free 方案；實際可用性以帳號為準）
templates/index.html：繁體中文首頁與響應式 CSS

Windows 本機執行（僅需安裝 Flask；Gunicorn 在 Render 的 Linux 環境使用）：
1. 在專案資料夾開啟 cmd。
2. py -m venv .venv
3. .venv\Scripts\activate
4. python -m pip install "Flask>=3.1,<4.0"
5. python app.py
6. 開啟 http://127.0.0.1:5000
7. 停止時按 Ctrl+C。

不在電腦安裝 Python 的部署方法：
1. 解壓縮專案。
2. 在 GitHub 建立 repository，例如 movie-recommendations。
3. 將 app.py、requirements.txt、render.yaml、README.txt 和 templates 資料夾
   上傳至 repository 根目錄。不要多包一層 movie-recommendations 資料夾。
4. 登入 Render，New > Web Service，連接上述 repository。
5. Language 選 Python 3。
6. Build Command：pip install -r requirements.txt
7. Start Command：gunicorn app:app --bind 0.0.0.0:$PORT
8. Instance Type 若有 Free 可選，選 Free；不要誤選付費方案。
9. 部署成功後，打開服務頁顯示的 onrender.com 網址。
10. 確認標題、三張電影卡片與手機版排版正常，再將該網址放入作業。

部署說明來源：https://render.com/docs/deploy-flask
若使用 Blueprint，可直接讓 Render 讀取 render.yaml。

作業文件提醒：檔名依老師要求 HW2_學號.doc。
包含部署網址、實際使用的 Prompt、以及四項實際操作心得。
尚未成功部署前，不要填入自編網址；心得應記錄自己真正遇到的情況。
