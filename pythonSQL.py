import streamlit as st
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="التحدي التفاعلي 🛡️",
    page_icon="⚔️",
    layout="centered"
)

# رابط Web App الخاص بـ Google Apps Script
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzCHyNyjkDlVHLuHjavamU7VnwEBFZSRKo4oJLKufOSnglxs-rlzsZuBmC0SSo-r-4xvA/exec"

# التنسيق الشامل لتعديل الألوان وتوجيه الأكواد
st.markdown("""
    <style>
    /* 1. اتجاه التطبيق الأساسي RTL */
    .stApp { 
        background-color: #0d1117; 
        color: #ffffff !important; 
        direction: rtl;
    }

    /* 2. تحويل جميع النصوص وعناوين الأسئلة (Labels) للون الأبيض الناصع والصريح */
    div[data-testid="stWidgetLabel"] p, 
    label, 
    .stWidgetLabel, 
    .stSelectbox label, 
    .stTextInput label, 
    .stNumberInput label, 
    .stRadio label,
    p, span {
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.1rem !important;
        opacity: 1 !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* 3. العناوين الرئيسية والفرعية */
    h1, h2, h3, .stSubheader { 
        color: #58a6ff !important; 
        padding-bottom: 5px; 
    }

    /* 4. إصلاح اتجاه الأكواد البرمجية بالكامل لتكون من اليسار لليمين LTR */
    div[data-testid="stCodeBlock"], 
    div[data-testid="stCodeBlock"] * {
        direction: ltr !important;
        text-align: left !important;
    }

    .stCodeBlock code, pre {
        direction: ltr !important;
        text-align: left !important;
        font-family: 'Courier New', Courier, monospace !important;
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px;
    }

    /* 5. خط أبيض فاصل بين الأسئلة */
    hr {
        border: none !important;
        border-top: 2px solid #ffffff !important;
        margin: 25px 0 !important;
        opacity: 0.8;
    }

    /* 6. إعدادات الخانات والقوائم المنسدلة */
    div[data-baseweb="select"] > div, input, textarea {
        background-color: #161b22 !important;
        color: #ffffff !important;
        border-color: #484f58 !important;
    }

    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"], li[role="option"] {
        background-color: #161b22 !important;
        color: #ffffff !important;
    }

    li[role="option"]:hover, li[role="option"][aria-selected="true"] {
        background-color: #58a6ff !important;
        color: #0d1117 !important;
    }

    /* 7. زر التسليم */
    .stButton > button {
        width: 100%; 
        background-color: #238636 !important; 
        color: #ffffff !important;
        border: none !important; 
        font-weight: bold; 
        font-size: 1.2rem;
        padding: 10px 20px; 
        border-radius: 6px;
    }
    .stButton > button:hover { 
        background-color: #2ea043 !important; 
        box-shadow: 0 0 10px #2ea043; 
    }
    </style>
""", unsafe_allow_html=True)

# العنوان
st.title("🛡️ التحدي التفاعلي")
st.write("قم بتحليل السيناريوهات الأمنية والبرمجية أدناه، وأدخل الإجابات الصحيحة لتجاوز النظام.")

st.markdown("<hr>", unsafe_allow_html=True)

student_name = st.text_input("أدخل اسمك الثلاثي لتسجيل النتيجة:")

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 1 -----------------
st.subheader("🚩 التحدي 1: تجاوز نظام الحماية عبر SQL Injection")
st.write("حاول مهاجم تسجيل الدخول في نظام عبر الحقل الخاص بـ Username. ما هي القيمة التي إذا أدخلها في الخانة ستجعل شرط الاستعلام دائم الصحة (True) للوصول للحساب دون معرفة كلمة المرور؟")
st.code("SELECT * FROM users WHERE username = 'INPUT' AND status = 'active';", language="sql")
q1_input = st.selectbox(
    "اختر المدخل الخبيث المناسب للالتفاف على الفحص:",
    ["اختر الإجابة...", "admin", "admin' OR '1'='1", "admin'; DROP TABLE users; --", "admin' AND '1'='2"]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 2 -----------------
st.subheader("🚩 التحدي 2: تتبع كود حظر المحاولات بـ Python")
code_q2 = """lockout = False
attempts = 0

while attempts < 3 and not lockout:
    pin = input("Enter PIN: ")
    if pin == "9900":
        print("Unlocked")
        break
    attempts += 1

if attempts == 3:
    lockout = True
    print("SYSTEM_LOCKED")"""
st.code(code_q2, language="python")
q2_input = st.selectbox(
    "إذا أدخل المستخدم القيم التالية بالترتيب (1111, 2222, 3333)، ما هي الرسالة النهائية التي ستطبع؟",
    ["اختر الإجابة...", "Unlocked", "SYSTEM_LOCKED", "Unlocked وتليها SYSTEM_LOCKED", "لن يطبع شيء"]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 3 -----------------
st.subheader("🚩 التحدي 3: تحليل الذاكرة والنظام الثنائي")
st.write("في فحص للذاكرة، تم العثور على قيمة ثنائية مكونة من 8-bit وهي: `00010100`.")
st.code("00010100", language="text")
q3_input = st.number_input("ما هي القيمة المكافئة لها بالنظام العشري (Decimal)؟", min_value=0, max_value=255, value=0)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 4 -----------------
st.subheader("🚩 التحدي 4: فك تشفير البيانات السداسية العشرية")
st.write("تم اعتراض حزمة بيانات تحتوي على الحروف المشفّرة بنظام Hex التالية:")
st.code("48 41 43 4b", language="hex")
q4_input = st.text_input("اعتماداً على جدول ASCII، ما هي الكلمة الإنجليزية المكونة لهذا النص؟ (اكتب بالـ Capital)")

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 5 -----------------
st.subheader("🚩 التحدي 5: تقييم الصلاحيات بالأمر الشرطي")
code_q5 = """role = "analyst"
clearance = 3

if role == "admin" or clearance >= 5:
    print("Full Access")
elif role == "analyst" and clearance >= 3:
    print("Restricted Access")
else:
    print("No Access")"""
st.code(code_q5, language="python")
q5_input = st.selectbox(
    "ما هي المخرجات المتوقعة من هذا التنفيذ؟",
    ["اختر الإجابة...", "Full Access", "Restricted Access", "No Access"]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 6 -----------------
st.subheader("🚩 التحدي 6: استعلام تحليل البيانات بـ SQL")
st.write("تريد تحديد عدد جميع المحاولات الفاشلة للمستخدم 'user1' من جدول `logs`.")
q6_input = st.selectbox(
    "ما هو الاستعلام الصحيح لاسترجاع هذا العدد؟",
    [
        "اختر الإجابة...",
        "SELECT COUNT(*) FROM logs WHERE username = 'user1' AND status = 'failed';",
        "SELECT SUM(*) FROM logs WHERE username = 'user1';",
        "SELECT * FROM logs WHERE username = 'user1' SORT BY failed;",
        "COUNT logs WHERE status = 'failed';"
    ]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 7 -----------------
st.subheader("🚩 التحدي 7: تمثيل ترميز UTF-8")
q7_input = st.radio(
    "لماذا يُفضل استخدام ترميز UTF-8 في نقل البيانات عبر الشبكات مقارنةً بـ UTF-32؟",
    [
        "اختر الإجابة...",
        "لأنه يوفر في حجم البيانات المقولة باستخدام حجم متغير (من 1 إلى 4 بايتات) حسب نوع الحرف",
        "لأنه أسرع في المعالجة دائماً بفضل حجمه الثابت 4 بايتات",
        "لأنه يستوعب الرموز بينما UTF-32 يقتصر على النصوص فقط"
    ]
)

st.markdown("<hr>", unsafe_allow_html=True)

# ----------------- التحدي 8 -----------------
st.subheader("🚩 التحدي 8: شفرة الألوان Hex")
st.write("يمثل اللون الأخضر الصافي بالنظام السداسي العشرية بالصيغة `#00FF00`.")
q8_input = st.text_input("ما هي القيمة الثنائية (Binary) المكافئة لقيمة الجزء الخاص بالأخضر (FF)؟")

st.markdown("<hr>", unsafe_allow_html=True)

# زر التسليم والحساب المئوي
if st.button("تأكيد وتسليم التحدي 🚀"):
    if not student_name.strip():
        st.error("⚠️ يرجى كتابة اسمك أولاً لتأكيد التسليم!")
    else:
        total_questions = 8
        correct_answers = 0

        if q1_input == "admin' OR '1'='1":
            correct_answers += 1
        if q2_input == "SYSTEM_LOCKED":
            correct_answers += 1
        if q3_input == 20:
            correct_answers += 1
        if q4_input.strip().upper() == "HACK":
            correct_answers += 1
        if q5_input == "Restricted Access":
            correct_answers += 1
        if q6_input == "SELECT COUNT(*) FROM logs WHERE username = 'user1' AND status = 'failed';":
            correct_answers += 1
        if "يوفر في حجم البيانات المقولة" in q7_input:
            correct_answers += 1
        if q8_input.strip() == "11111111":
            correct_answers += 1

        final_percentage = (correct_answers / total_questions) * 100

        payload = {
            "student_name": student_name,
            "score": f"{final_percentage:.1f}% ({correct_answers}/{total_questions})",
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        try:
            res = requests.post(WEB_APP_URL, json=payload)
            st.balloons()
            st.success(f"🎉 تم تسليم النتيجة بنجاح يا {student_name}!")
            st.markdown(f"""
            ### 📊 تفاصيل النتيجة:
            * **عدد الأسئلة المجاب عليها بشكل صحيح:** `{correct_answers}` من أصل `{total_questions}` أسئلة.
            * **الدرجة النهائية:** `{final_percentage:.1f} / 100`
            """)
        except Exception as e:
            st.error(f"تعذر الاتصال بـ Google Sheets: {e}")
