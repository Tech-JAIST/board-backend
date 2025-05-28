from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os
from datetime import datetime

app = FastAPI()

# フロントエンドとの通信を許可する（Step 4 で詳しくやる）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番では限定すべき
    allow_methods=["*"],
    allow_headers=["*"],
)

# 投稿のデータ形式（例：{"name": "ユーザー", "content": "こんにちは"}）
class Post(BaseModel):
    name: str
    content: str

# 投稿の保存先ファイル
DATA_FILE = "posts.json"

# ファイルから投稿を読み出す
def load_posts():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

# ファイルに投稿を保存する
def save_posts(posts):
    with open(DATA_FILE, "w") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

# 投稿一覧を返す
@app.get("/posts")
def get_posts():
    return load_posts()

# 新しい投稿を受け取る
@app.post("/posts")
def add_post(post: Post):
    posts = load_posts()
    new_post = {
        "id": len(posts) + 1,
        "name": post.name,
        "content": post.content,
        "created_at": datetime.now().isoformat()
    }
    posts.append(new_post)
    save_posts(posts)
    return {"message": "投稿を受け付けました", "post": new_post}
