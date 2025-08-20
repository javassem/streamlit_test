# sqlite3 설치 필요없음

import sqlite3

# 데이타베이스 연결 ( 파일로 저장됨 )
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 테이블 생성
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
        id  INTEGER PRIMARY KEY AUTOINCREMENT
        ,name TEXT NOT NULL
        ,age INTEGER NOT NULL
    )
''')

# 데이타 입력
cursor.execute('''INSERT INTO users(name,age) VALUES('홍길동',30)''')
cursor.execute('''INSERT INTO users(name,age) VALUES('박길동',22)''')
conn.commit()

# 데이타 조회
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
for row in rows:
    print(row)

# 연결 종료
conn.close()
