import streamlit as st
import requests
from datetime import datetime

# إعدادات الصفحة
st.set_page_config(
    page_title="تحدي الأمن والبرمجة المتقدم 🛡️",
    page_icon="⚔️",
    layout="centered"
)

# رابط Web App الخاص بـ Google Apps Script
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzCHyNyjkDlVHLuHjavamU7VnwEBFZSRKo4oJLKufOSnglxs-rlzsZuBmC0SSo-r-4xvA/exec"

# التنسيق الشامل مع تعديل لون الخط الرمادي ليصبح أبيض وبارز جداً
st.markdown("""
    <style>
    /* 1. ضبط اتجاه التطبيق وخلفية سوداء بالكامل */
    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #0d1117 !important; 
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* 2. تحويل جميع النصوص الرمادية والأوصاف والفرعيات إلى الأبيض الناصع */
    .stApp p, .stApp span, .stApp label, .stApp div, .stWidgetLabel, 
    [data-testid="stMarkdownContainer"] p, .stCaption {
        color: #FFFFFF !important;
        opacity: 1 !important;
        font-weight: 500;
    }

    /* 3. تعديل عناوين الأسئلة والبطاقات لتبدو باللون الأزرق الفاتح المضيء */
    h1, h2, h3, .stSubheader { 
        color: #58a6ff !important; 
        border-bottom: 1px solid #30363d; 
        padding-bottom: 10px; 
    }

    /* 4. ضبط الأكواد البرمجية لتكون واضحة وباتجاه اليسار لليمين LTR */
    div[data-testid="stCodeBlock"], code, pre {
        direction: ltr !important;
        text-align: left !important;
        font-family: 'Courier New', Courier, monospace !important;
        background-color: #161b22 !important;
        color: #79c0ff !important;
        border: 1px solid #30363d !important;
        border-radius: 6px;
    }

    /* 5. إصلاح القوائم المنسدلة والرموز الرمادية بداخلها */
    div[data-baseweb="select"] > div, div[data-baseweb="select"] span {
        background-color: #161b22 !important;
        border-color: #484f58 !important;
        color: #ffffff !important;
    }

    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[role="listbox"] {
        background-color: #161b22 !important;
        border: 1px solid #484f58 !important;
    }

    li[role="option"], div[role="option"] {
        background-color: #161b22 !important;
        color: #ffffff !important;
    }

    li[role="option"]:hover, div[role="option"]:hover {
        background-color: #58a6ff !important;
        color: #0d1117 !important;
    }

    /* 6. تعديل ألوان الإدخال النصي والأرقام */
    input, textarea {
        background-color: #161b22 !important;
        color: #ffffff !important;
        border: 1px solid #484f58 !important;
    }

    /* 7. بطاقات التحدي */
    .challenge-card { 
        background-color: #161b22; 
        padding: 20px; 
        border-radius: 8px; 
        border: 1px solid #30363d; 
        margin-bottom: 20px; 
    }
    
    /* 8. صندوق موعد التسليم */
    .deadline-card {
        background-color: #1c2128;
        border-right: 4px solid #58a6ff;
        padding: 12px 16px;
        border-radius: 6px;
        margin: 15px 0;
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ التحدي التفاعلي: الأمن والبرمجة")
st.write("قم بتحليل السيناريوهات الأمنية والبرمجية أدناه، وأدخل الإجابات الصحيحة لتجاوز النظام.")

st.divider()

student_name = st.text_input("أدخل اسمك الثلاثي لتسجيل النتيجة:")

# تنبيه موعد التسليم تحت خانة الاسم
st.markdown("""
    <div class="deadline-card">
        ⏳ <b>تنويه هام:</b> يرجى العلم أن آخر موعد لتسليم الإجابات واحتساب النتيجة هو <b>12 أيلول 2026</b>. بالتوفيق للجميع! 🚀
    </div>
""", unsafe_allow_html=True)

st.divider()

# ----------------- التحدي 1 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 1: تجاوز نظام الحماية عبر SQL Injection")
st.write("حاول مهاجم تسجيل الدخول في نظام عبر الحقل الخاص بـ Username. ما هي القيمة التي إذا أدخلها في الخانة ستجعل شرط الاستعلام دائم الصحة (True) للوصول للحساب دون معرفة كلمة المرور؟")
st.code("SELECT * FROM users WHERE username = 'INPUT' AND status = 'active';", language="sql")
q1_input = st.selectbox(
    "اختر المدخل الخبيث المناسب للالتفاف على الفحص:",
    ["اختر الإجابة...", "admin", "admin' OR '1'='1", "admin'; DROP TABLE users; --", "admin' AND '1'='2"]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 2 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 3 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 3: تحليل الذاكرة والنظام الثنائي")
st.write("في فحص للذاكرة، تم العثور على قيمة ثنائية مكونة من 8-bit وهي: `00010100`.")
st.code("00010100", language="text")
q3_input = st.number_input("ما هي القيمة المكافئة لها بالنظام العشري (Decimal)؟", min_value=0, max_value=255, value=0)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 4 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 4: فك تشفير البيانات السداسية العشرية")
st.write("تم اعتراض حزمة بيانات تحتوي على الحروف المشفّرة بنظام Hex التالية:")
st.code("48 41 43 4b", language="hex")
q4_input = st.text_input("اعتماداً على جدول ASCII، ما هي الكلمة الإنجليزية المكونة لهذا النص؟ (اكتب بالـ Capital)")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 5 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 6 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 7 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
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
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 8 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 8: شفرة الألوان Hex")
st.write("يمثل اللون الأخضر الصافي بالنظام السداسي العشرية بالصيغة `#00FF00`.")
q8_input = st.text_input("ما هي القيمة الثنائية (Binary) المكافئة لقيمة الجزء الخاص بالأخضر (FF)؟")
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# زر التسليم
if st.button("تأكيد وتسليم التحدي 🚀", type="primary", use_container_width=True):
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
            * **عدد الأسئلة الصحيحة:** `{correct_answers}` من أصل `{total_questions}`
            * **الدرجة النهائية:** `{final_percentage:.1f}%`
            """)
        except Exception as e:
            st.error(f"تعذر الاتصال بـ Google Sheets: {e}")
