from sqlalchemy import create_engine
from main import Base, Item
import os

# データベース接続設定
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# DBのテーブル作成
Base.metadata.create_all(bind=engine)
