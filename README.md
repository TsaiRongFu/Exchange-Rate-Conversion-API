## API 實作測驗

### API伺服器

* 確保正確安裝[Python](https://www.python.org/ftp/python/3.12.0/python-3.12.0-amd64.exe)
* git clone 專案
* 開啟terminal切換至專案底下
* terminal輸入 `pip install -r requirements.txt` 安裝套件
* terminal啟動API伺服器 `python main.py`
* 開啟瀏覽器做簡易測式-Flask預設port5000
    - http://127.0.0.1:5000/convert?source=USD&target=JPY&amount=$1,525

### 單元測試

* 開啟terminal切換至專案底下
* terminal輸入 `python unit_test.py`
* 查看最終執行結果

#### <font color=red>Flask非正式API工具開發環境，為求快速開發所以使用此套件，正式伺服器會選用Django做開發</font>