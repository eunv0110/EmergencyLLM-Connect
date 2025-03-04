import pandas as pd
import sqlite3
from datetime import datetime

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

#=========================================================Setting=======================================================#
DBName = 'em.db'

def Set_DBName(name, path=None):
    global DBName
    if(path):
        DBName = path + name + '.db'
    else:
        DBName = name + '.db'

#==========================================================Log==========================================================#

#==================================로그 삽입
def Log_Insert(inputText, lat, lng, em_class, hos1, addr1, tel1, hos2, addr2, tel2, hos3, addr3, tel3):
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS log (
            datetime TEXT PRIMARY KEY,
            input_text TEXT NOT NULL,
            input_latitude REAL NOT NULL,
            input_longitude REAL NOT NULL,
            em_class INTEGER NOT NULL,
            hospital_1 TEXT NOT NULL,
            addr_1 TEXT NOT NULL,
            tel_1 TEXT NOT NULL,
            hospital_2 TEXT NOT NULL,
            addr_2 TEXT NOT NULL,
            tel_2 TEXT NOT NULL,
            hospital_3 TEXT NOT NULL,
            addr_3 TEXT NOT NULL,
            tel_3 TEXT NOT NULL
            )
        ''')
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute('''
            INSERT INTO log (datetime, input_text, input_latitude, input_longitude, em_class, 
                             hospital_1, addr_1, tel_1, hospital_2, addr_2, tel_2, 
                             hospital_3, addr_3, tel_3) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (dt, inputText, lat, lng, em_class, hos1, addr1, tel1, hos2, addr2, tel2, hos3, addr3, tel3))
        conn.commit()

    except Exception as e:
        return f"An error occurred: {e}"
    
    finally:
        if conn:
            conn.close()

#==================================가장 오래된 로그 기록부터 삭제
def Log_DeleteOldest():
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM log 
            WHERE datetime = (SELECT MIN(datetime) FROM log)
        ''')
        conn.commit()
    except Exception as e:
        return f"An error occurred: {e}"
    finally:
        if conn:
            conn.close()
            
            
#==================================로그 검색
def Log_FindByDate(start_date, end_date, start_time=None, end_time=None):
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()

        if not (start_date and end_date):
            return "모든 날짜 입력 필드는 반드시 필요함"

        if start_time and end_time:
            start_date_time = f"{start_date} {start_time}:00"
            end_date_time = f"{end_date} {end_time}:59"
        else:
            start_date_time = f"{start_date} 00:00:00"
            end_date_time = f"{end_date} 23:59:59"

        cursor.execute(
            "SELECT * FROM log WHERE datetime BETWEEN ? AND ?", 
            (start_date_time, end_date_time)
        )
        
        results = cursor.fetchall()
        if not results:
            return "검색 결과 없음"
        
        column_names = [description[0] for description in cursor.description]
        df = pd.DataFrame(results, columns=column_names)
        return df
    
    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if conn:
            conn.close()
            
            

#==========================================================Board==========================================================#

#==================================게시글 작성
def Post_Write(ID, PW, TitleText, BodyText):
    try:
        if len(ID) > 8 | len(ID) < 2:
            return "ID는 2 ~ 8자 내외여야 합니다."
        if len(PW) > 12 | len(PW) < 4:
            return "PW는 4 ~ 12자 내외여야 합니다."
        
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS board (
            postID INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            userID TEXT NOT NULL,
            userPW TEXT NOT NULL,
            title TEXT NOT NULL,
            body TEXT NOT NULL
        )
        ''')
        
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor.execute('''
            INSERT INTO board (datetime, userID, userPW, title, body) 
            VALUES (?, ?, ?, ?, ?)
            ''', (dt, ID, PW, TitleText, BodyText))
        conn.commit()
        return "글 작성 완료됨"

    except Exception as e:
        return f"An error occurred: {e}"
    
    finally:
        if conn:
            conn.close()
            
#==================================게시글 삭제
def Post_DeleteSelected(postID, userPW):
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        cursor.execute("SELECT userPW FROM board WHERE postID = ?", (postID,))
        result = cursor.fetchone()
        
        if result is None:
            return f"{postID}번 게시글을 찾을 수 없음"
        
        stored_pw = result[0]
        if stored_pw != userPW:
            return "잘못된 비밀번호"

        cursor.execute("DELETE FROM board WHERE postID = ?", (postID,))
        conn.commit()
        return f"{postID}번 글 삭제 완료됨"

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if conn:
            conn.close()
            

#==================================게시글 검색
def Post_FindByText(category, InputText):
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        
        # CSS에서 카테고리 입력 값을 반드시 숫자로 넣어주어야 함 그럴 수 없다면 수정 작업 필요
        # 0번 : 작성자, 1번 : 게시글 제목, 2번 : 게시글 제목 + 내용
        if category == 0:
            cursor.execute("SELECT * FROM board WHERE userID LIKE ?", ('%' + InputText + '%',))
        elif category == 1:
            cursor.execute("SELECT * FROM board WHERE title LIKE ?", ('%' + InputText + '%',))
        elif category == 2:
            cursor.execute("SELECT * FROM board WHERE title LIKE ? OR body LIKE ?", 
                           ('%' + InputText + '%', '%' + InputText + '%'))
        else:
            return "카테고리 범위 초과함"
        
        if len(InputText) == 0:
            return "검색할 내용을 입력하세요"

        results = cursor.fetchall()
        if not results:
            return "검색 결과 없음"
        
        column_names = [description[0] for description in cursor.description]
        df = pd.DataFrame(results, columns=column_names)
        return df

    except Exception as e:
        return f"An error occurred: {e}"

    finally:
        if conn:
            conn.close()


def Log_Insert_2(inputText, lat, lng, em_class, hospitals):
    #병원의 수가 동적으로 변해도 로그를 기록할 수 있는 함수.
    
    try:
        conn = sqlite3.connect(DBName)
        cursor = conn.cursor()
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 동적으로 테이블 생성 (병원 정보 최대 10개 저장)
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS log (
            datetime TEXT PRIMARY KEY,
            input_text TEXT NOT NULL,
            input_latitude REAL NOT NULL,
            input_longitude REAL NOT NULL,
            em_class INTEGER NOT NULL
        )
        ''')

        # 병원 관련 컬럼 동적 생성 (최대 10개)
        existing_columns = [col[1] for col in cursor.execute("PRAGMA table_info(log)").fetchall()]
        for i in range(1, 11):  # 1부터 10까지
            if f"hospital_{i}" not in existing_columns:
                cursor.execute(f'''
                ALTER TABLE log 
                ADD COLUMN hospital_{i} TEXT DEFAULT NULL
                ''')
            if f"addr_{i}" not in existing_columns:
                cursor.execute(f'''
                ALTER TABLE log 
                ADD COLUMN addr_{i} TEXT DEFAULT NULL
                ''')
            if f"tel_{i}" not in existing_columns:
                cursor.execute(f'''
                ALTER TABLE log 
                ADD COLUMN tel_{i} TEXT DEFAULT NULL
                ''')

        # 기본 데이터
        log_data = [dt, inputText, lat, lng, em_class]

        # 병원 정보 추가
        for i in range(1, 11):
            if i <= len(hospitals):
                log_data.extend([hospitals[i - 1].get("name"), hospitals[i - 1].get("addr"), hospitals[i - 1].get("tel")])
            else:
                log_data.extend([None, None, None])  # 병원이 부족한 경우 NULL 추가

        # 동적 SQL 필드 및 값 생성
        columns = ['datetime', 'input_text', 'input_latitude', 'input_longitude', 'em_class']
        values_placeholders = ['?'] * len(log_data)

        for i in range(1, 11):
            columns.extend([f"hospital_{i}", f"addr_{i}", f"tel_{i}"])

        columns_str = ', '.join(columns)
        placeholders_str = ', '.join(values_placeholders)

        # SQL INSERT 실행
        cursor.execute(f'''
            INSERT INTO log ({columns_str})
            VALUES ({placeholders_str})
        ''', log_data)

        conn.commit()
        return "Log inserted successfully!"

    except Exception as e:
        return f"An error occurred: {e}"
    
    finally:
        if conn:
            conn.close()