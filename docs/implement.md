# 実装方法
## 前提知識
### ディレクトリ構造
ディレクトリ構造は以下のようになっています。
```sh
.
├── Dockerfile # PythonアプリのDockerfile
├── compose.yaml # Pythonアプリ, DB, adminerのcompose.yml
├── backend
│   ├── domain # サーバーにおけるメインのデータ型
│   ├── handler # ルーティング
│   ├── repository # DB操作
│   └── __main__.py
```

### 使用しているライブラリ
#### FastAPI
[FastAPI documentation](https://fastapi.tiangolo.com/)

#### tinyDB
[tinyDB documentation](https://tinydb.readthedocs.io/en/latest/)
[tinyDBを使ってみよう](https://scrapbox.io/PythonOsaka/TinyDB%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%81%BF%E3%82%88%E3%81%86)

#### uvicorn
[uvicorn documentation](https://www.uvicorn.org/)

## APIの新規実装
順不同で
- `backend/handler`にルーティング＆処理を記述する
- (DB操作があれば)`backend/repository/{model名}.py`に記述し、`backend/handler/{group名}.py`に呼び出し処理を記述する

と変更すると新たなAPIが実装できます。
