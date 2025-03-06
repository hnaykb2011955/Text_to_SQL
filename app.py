from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from Data_source_Determiner_agent import Datasourcedeterminer

import mysql.connector




app = Flask(__name__)


#Tạo đối tượng Data_source_determiner
data_source_determiner = Datasourcedeterminer()



# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("suriya7/t5-base-text-to-sql")
model = AutoModelForSeq2SeqLM.from_pretrained("suriya7/t5-base-text-to-sql")

# MySQL connection details
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "sales"
}

# Function to translate English query to SQL
def translate_to_sql_select(english_query):
    input_text = "translate English to SQL: " + english_query
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=100, truncation=True)
    outputs = model.generate(input_ids)
    sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return sql_query

# Function to execute SQL query on MySQL database
def execute_query(sql_query):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql_query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Route để hiển thị giao diện web
@app.route('/')
def home():
    return render_template('index.html')

# Route để xử lý truy vấn từ giao diện web
@app.route('/query', methods=['POST'])
def handle_query():
    english_query = request.form.get("query")

    if not english_query:
        return jsonify({"error": "No query provided"}), 400

    # Xác định nguồn dữ liệu (MySQL hoặc CSV)
    sources = data_source_determiner.determine_source(english_query)
    
    if 'mysql' in sources:
        # Chuyển đổi truy vấn tiếng Anh sang SQL
        sql_query = translate_to_sql_select(english_query)
        # Thực thi truy vấn trên MySQL
        results = execute_query(sql_query)
    else:
        # Xử lý truy vấn trên CSV (chưa được triển khai)
        results = []  

    return render_template('index.html', query=english_query, sql_query=sql_query, results=results)


if __name__ == '__main__':
    app.run(debug=True)