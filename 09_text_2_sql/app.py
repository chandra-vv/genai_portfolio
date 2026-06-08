import os
import streamlit as st
import sqlparse
from dotenv import load_dotenv
from db import get_connection, get_schema, run_query
from llm import text_to_sql, fix_sql

load_dotenv()

st.set_page_config(page_title="Text-to-SQL | MySQL", page_icon="🗄️", layout="wide")

# ── Custom CSS Theme (Light Professional — Streamlit Gallery Style) ───────────
st.markdown("""
<style>
/* ── Google Font ── */
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600;700&display=swap');

/* ── Root & Background ── */
html, body, [class*="css"] {
    font-family: 'Source Sans Pro', sans-serif;
}
.stApp {
    background-color: #f5f7fa;
}

/* ── Hide default Streamlit chrome ── */
#MainMenu, footer { visibility: hidden; }
.block-container {
    padding-top: 0 !important;
    padding-bottom: 3rem;
    max-width: 1100px;
}

/* ── Top nav bar ── */
.topbar {
    background: #ffffff;
    border-bottom: 1px solid #e3e8ef;
    padding: 0.65rem 2rem;
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
    position: sticky;
    top: 0;
    z-index: 999;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}
.topbar .nav-title {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #6b7280;
}
.topbar .nav-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #2563eb;
    display: inline-block;
}

/* ── Page Header ── */
.page-header {
    padding: 2rem 0 1.5rem 0;
    border-bottom: 2px solid #e5e7eb;
    margin-bottom: 2rem;
}
.page-header h1 {
    font-size: 2rem;
    font-weight: 700;
    color: #111827;
    margin: 0 0 0.3rem 0;
}
.page-header p {
    color: #6b7280;
    font-size: 1rem;
    margin: 0;
}

/* ── Section label ── */
.section-label {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 1.8px;
    text-transform: uppercase;
    color: #2563eb;
    margin-bottom: 0.6rem;
    display: flex;
    align-items: center;
    gap: 6px;
}

/* ── White cards ── */
.card {
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 1.5rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}

/* ── Stats row ── */
.stat-row {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.stat-box {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 1rem 1.2rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.stat-box .stat-val {
    font-size: 1.6rem;
    font-weight: 700;
    color: #2563eb;
    line-height: 1;
}
.stat-box .stat-lbl {
    font-size: 0.78rem;
    color: #6b7280;
    margin-top: 4px;
    font-weight: 500;
}

/* ── Input Area ── */
.stTextArea textarea {
    background: #ffffff !important;
    border: 1.5px solid #d1d5db !important;
    border-radius: 6px !important;
    color: #111827 !important;
    font-family: 'Source Sans Pro', sans-serif !important;
    font-size: 0.97rem !important;
    padding: 0.75rem 1rem !important;
    transition: border-color 0.15s, box-shadow 0.15s;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
}
.stTextArea textarea:focus {
    border-color: #2563eb !important;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
}
.stTextArea label {
    color: #374151 !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.2px !important;
}

/* ── Run Button ── */
.stFormSubmitButton > button {
    background: #2563eb !important;
    color: white !important;
    border: none !important;
    border-radius: 6px !important;
    padding: 0.5rem 1.8rem !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    transition: background 0.15s, box-shadow 0.15s !important;
    box-shadow: 0 1px 3px rgba(37,99,235,0.3) !important;
}
.stFormSubmitButton > button:hover {
    background: #1d4ed8 !important;
    box-shadow: 0 4px 12px rgba(37,99,235,0.35) !important;
}

/* ── Checkbox ── */
.stCheckbox label {
    color: #374151 !important;
    font-size: 0.9rem !important;
}

/* ── Code blocks ── */
.stCodeBlock, [data-testid="stCodeBlock"] {
    border-radius: 6px !important;
    border: 1px solid #e5e7eb !important;
    background: #f8fafc !important;
}

/* ── Success / Warning / Error banners ── */
[data-testid="stNotification"] {
    border-radius: 6px !important;
    font-size: 0.9rem !important;
}

/* ── Dataframe ── */
.stDataFrame {
    border-radius: 8px !important;
    overflow: hidden !important;
    border: 1px solid #e5e7eb !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
}
[data-testid="stDataFrame"] th {
    background: #f1f5f9 !important;
    color: #374151 !important;
    font-weight: 600 !important;
    font-size: 0.82rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.5px !important;
}

/* ── Expander (history) ── */
.streamlit-expanderHeader {
    background: #ffffff !important;
    border-radius: 6px !important;
    color: #111827 !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    border: 1px solid #e5e7eb !important;
    padding: 0.75rem 1rem !important;
}
.streamlit-expanderContent {
    background: #f9fafb !important;
    border: 1px solid #e5e7eb !important;
    border-top: none !important;
    border-radius: 0 0 6px 6px !important;
    padding: 1rem !important;
}

/* ── Divider ── */
hr {
    border-color: #e5e7eb !important;
    margin: 2rem 0 !important;
}

/* ── Subheaders ── */
h2 { color: #111827 !important; font-weight: 700 !important; font-size: 1.35rem !important; }
h3 { color: #1f2937 !important; font-weight: 600 !important; font-size: 1.1rem !important; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e5e7eb !important;
}
[data-testid="stSidebar"] .stMarkdown,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] li {
    color: #4b5563 !important;
    font-size: 0.88rem !important;
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: #111827 !important;
    font-size: 0.95rem !important;
    font-weight: 700 !important;
    letter-spacing: 0.2px !important;
}
[data-testid="stSidebar"] code {
    background: #eff6ff !important;
    color: #2563eb !important;
    border-radius: 4px !important;
    padding: 1px 6px !important;
    font-size: 0.82rem !important;
}
[data-testid="stSidebar"] .stSuccess {
    background: #f0fdf4 !important;
    border: 1px solid #bbf7d0 !important;
    border-radius: 6px !important;
    color: #166534 !important;
    font-size: 0.85rem !important;
}

/* ── Spinner ── */
.stSpinner > div {
    border-top-color: #2563eb !important;
}

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #f1f5f9; }
::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>
""", unsafe_allow_html=True)

# ── Top Nav Bar ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <span class="nav-dot"></span>
    <span class="nav-title">Text-to-SQL Studio</span>
</div>
""", unsafe_allow_html=True)

# ── Page Header ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="page-header">
    <h1>Query your database in plain English</h1>
    <p>Type a question below — the AI generates and runs the SQL for you instantly.</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────

with st.sidebar:
    st.header("⚙️ Connection Info")
    st.markdown(
        f"- **Host:** `{os.getenv('MYSQL_HOST', 'localhost')}:{os.getenv('MYSQL_PORT', '3306')}`\n"
        f"- **Database:** `{os.getenv('MYSQL_DATABASE', 'not set')}`\n"
        f"- **User:** `{os.getenv('MYSQL_USER') or os.getenv('MYSQL_USERNAME', 'not set')}`\n"
        f"- **Model:** `{os.getenv('GROK_MODEL', 'grok-3')}` (xAI Grok)"
    )

# ── Connection & schema (cached per session) ──────────────────────────────────

@st.cache_resource(show_spinner="Connecting to MySQL…")
def init_pool():
    """Initialise the connection pool once and verify connectivity."""
    conn = get_connection()   # test checkout — raises immediately if creds are wrong
    schema = get_schema(conn)
    conn.close()              # return to pool
    return schema


try:
    schema = init_pool()
    st.sidebar.success(f"✅ Connected to `{os.getenv('MYSQL_DATABASE')}`")
except Exception as e:
    st.error(f"❌ MySQL connection failed: {e}")
    with st.expander("Troubleshooting tips"):
        st.markdown("""
**Common issues:**

1. **Wrong database name** — Set `MYSQL_DATABASE` in `.env` to the exact schema name shown in MySQL Workbench.
2. **Wrong password** — Check `MYSQL_PASSWORD` in `.env`.
3. **MySQL not running** — Make sure MySQL server is started (check MySQL Workbench or Windows Services).
4. **Wrong port** — Default is `3306`; update `MYSQL_PORT` if yours differs.
5. **Missing driver** — Run: `pip install mysql-connector-python`
        """)
    st.stop()

# ── Schema viewer ─────────────────────────────────────────────────────────────

with st.sidebar.expander("📋 Database Schema", expanded=False):
    st.code(schema or "(no tables found)", language="sql")


# ── Query history ─────────────────────────────────────────────────────────────

if "history" not in st.session_state:
    st.session_state.history = []

# ── Main input ────────────────────────────────────────────────────────────────

st.markdown('<div class="section-label">ASK YOUR DATABASE</div>', unsafe_allow_html=True)
with st.form("query_form", clear_on_submit=False):
    question = st.text_area(
        "Your question",
        placeholder="e.g. Show the top 5 products by total sales this month",
        height=100,
    )
    col1, col2 = st.columns([1, 5])
    submitted = col1.form_submit_button("▶ Run", type="primary")
    auto_fix  = col2.checkbox("Auto-fix SQL on error", value=True)

if submitted and question.strip():
    with st.spinner("Generating SQL…"):
        sql = text_to_sql(question, schema)

    if sql.upper().startswith("ERROR:"):
        st.error(sql)
    else:
        formatted_sql = sqlparse.format(sql, reindent=True, keyword_case="upper")
        st.subheader("Generated SQL")
        st.code(formatted_sql, language="sql")

        with st.spinner("Running query on MySQL…"):
            try:
                df = run_query(get_connection(), sql)
                st.success(f"✅ {len(df)} row(s) returned")
                st.dataframe(df, use_container_width=True)
                st.session_state.history.insert(0, {
                    "question": question, "sql": formatted_sql,
                    "df": df, "error": None,
                })
            except Exception as e:
                err_msg = str(e)
                if auto_fix:
                    st.warning(f"Query failed — asking model to fix it…\n\n`{err_msg}`")
                    with st.spinner("Fixing SQL…"):
                        fixed_sql = fix_sql(question, schema, sql, err_msg)
                    formatted_fixed = sqlparse.format(
                        fixed_sql, reindent=True, keyword_case="upper"
                    )
                    st.subheader("Fixed SQL")
                    st.code(formatted_fixed, language="sql")
                    try:
                        df = run_query(get_connection(), fixed_sql)
                        st.success(f"✅ Fixed! {len(df)} row(s) returned")
                        st.dataframe(df, use_container_width=True)
                        st.session_state.history.insert(0, {
                            "question": question, "sql": formatted_fixed,
                            "df": df, "error": None,
                        })
                    except Exception as e2:
                        st.error(f"Still failed after fix: {e2}")
                        st.session_state.history.insert(0, {
                            "question": question, "sql": formatted_fixed,
                            "df": None, "error": str(e2),
                        })
                else:
                    st.error(f"Query failed: {err_msg}")
                    st.session_state.history.insert(0, {
                        "question": question, "sql": formatted_sql,
                        "df": None, "error": err_msg,
                    })

# ── Query history panel ───────────────────────────────────────────────────────

if st.session_state.history:
    st.divider()
    st.markdown('<div class="section-label">QUERY HISTORY</div>', unsafe_allow_html=True)
    st.subheader("Recent Queries")
    for i, item in enumerate(st.session_state.history[:10]):
        label = f"Q: {item['question'][:80]}" + ("…" if len(item['question']) > 80 else "")
        with st.expander(label, expanded=(i == 0)):
            st.code(item["sql"], language="sql")
            if item["df"] is not None:
                st.dataframe(item["df"], use_container_width=True)
            else:
                st.error(item["error"])
