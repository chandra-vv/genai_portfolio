# 🗄️ Text-to-SQL Studio

A **Streamlit** web application that lets you query your **MySQL** database using plain English. Powered by **Groq AI (LLaMA 3.3 70B)**, it automatically generates, runs, and even self-fixes SQL queries — no SQL knowledge required.

---

## ✨ Features

- 🧠 **Natural Language to SQL** — Type a question, get a SQL query instantly
- 🔧 **Auto-fix on Error** — If the query fails, the AI automatically corrects it
- 📋 **Schema Auto-discovery** — Reads all your MySQL tables and columns on startup
- 🕘 **Query History** — Last 10 queries kept in session with results
- 🎨 **Professional UI** — Clean light theme built with custom Streamlit CSS
- 🔒 **Read-only Safety** — AI is instructed to only generate SELECT statements
- ⚡ **Connection Pooling** — Stable MySQL connection pool prevents stale connection errors

---

## 🖥️ Screenshots

> _Add screenshots here after setup_

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| AI Model | Groq API — `llama-3.3-70b-versatile` |
| Database | MySQL (local via MySQL Workbench) |
| Language | Python 3.10+ |
| SQL Formatting | sqlparse |

---

## 📁 Project Structure

```
text2sql/
├── app.py               # Streamlit UI — main application
├── db.py                # MySQL connection pool, schema reader, query runner
├── llm.py               # Groq API calls — text-to-SQL and auto-fix
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (NOT committed to Git)
└── .env.example         # Template for environment variables
```

---

## ⚙️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text2sql.git
cd text2sql
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
# Groq AI Configuration
GROK_API_KEY=your_groq_api_key_here
GROK_MODEL=llama-3.3-70b-versatile

# MySQL Local Database
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=your_database_name
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_password
```

> 🔑 **Get your free Groq API key** at [console.groq.com](https://console.groq.com)

### 5. Run the application

```bash
streamlit run app.py
```

Open your browser at **http://localhost:8501**

---

## 🔑 Environment Variables

| Variable | Description | Example |
|---|---|---|
| `GROK_API_KEY` | Groq API key | `gsk_xxx...` |
| `GROK_MODEL` | Groq model to use | `llama-3.3-70b-versatile` |
| `MYSQL_HOST` | MySQL host | `localhost` |
| `MYSQL_PORT` | MySQL port | `3306` |
| `MYSQL_DATABASE` | Database / schema name | `analysis` |
| `MYSQL_USER` | MySQL username | `root` |
| `MYSQL_PASSWORD` | MySQL password | `your_password` |

---

## 🚀 Usage

1. Launch the app and confirm the **✅ Connected** status in the sidebar
2. View your database schema in the **📋 Database Schema** expander in the sidebar
3. Type your question in the text box, e.g.:
   - *"Show the top 10 customers by total order value"*
   - *"How many orders were placed last month?"*
   - *"List all products with stock below 50"*
4. Click **▶ Run** — the SQL is generated and executed instantly
5. If the query fails, the AI auto-fixes it (toggle with the checkbox)
6. Browse previous queries in the **Query History** section

---

## 🔒 Security Notes

- The AI is prompted to **only generate SELECT queries** — INSERT, UPDATE, DELETE, DROP are blocked at the prompt level
- **Never commit your `.env` file** — it is listed in `.gitignore`
- For production use, create a **dedicated read-only MySQL user** instead of using `root`

```sql
-- Create a read-only user for the app
CREATE USER 'text2sql_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT SELECT ON your_database.* TO 'text2sql_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## 🐛 Troubleshooting

| Error | Fix |
|---|---|
| `Access denied for user ''@'localhost'` | Check `MYSQL_USER` in `.env` — must be `MYSQL_USER` not `MYSQL_USERNAME` |
| `Unread result found` | Fixed by connection pooling — restart the app |
| `MySQL not running` | Start MySQL server via MySQL Workbench or Windows Services |
| `quota exceeded` (OpenAI error) | You're using an expired OpenAI key — switch to Groq (`GROK_API_KEY`) |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |

---

## 🗺️ Roadmap

- [ ] Auto-chart generation (Plotly) for numeric results
- [ ] Multi-turn conversation with query memory
- [ ] Persistent query history (SQLite)
- [ ] CSV / Excel export for results
- [ ] Authentication (login page)
- [ ] Docker deployment support

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io) — UI framework
- [Groq](https://groq.com) — Ultra-fast LLM inference
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) — Database driver
- [sqlparse](https://github.com/andialbrecht/sqlparse) — SQL formatting
