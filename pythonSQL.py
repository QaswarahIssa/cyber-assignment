import streamlit as st

# إعدادات الصفحة والتنسيق العام
st.set_page_config(
    page_title="تحدي أمن المعلومات والبرمجة 🛡️",
    page_icon="⚔️",
    layout="centered"
)

# تطبيق التنسيق ذو الخلفية السوداء وتحديد اتجاهات النصوص والأكواد
st.markdown("""
    <style>
    /* خلفية التطبيق سوداء بالكامل */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
    }
    
    /* ضبط النص العام والأسئلة ليكون من اليمين لليسار */
    html, body, [class*="css"], div, h1, h2, h3, h4, h5, h6, p, label, .stRadio, .stSelectbox {
        direction: rtl !important;
        text-align: right !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* عناوين البرمجة والتحديات */
    h1, h2, h3 {
        color: #58a6ff !important;
        border-bottom: 1px solid #30363d;
        padding-bottom: 10px;
    }

    /* ضبط كتل الأكواد والرموز البرمجية لتبدأ من اليسار لليمين */
    .stCodeBlock, code, pre, div[data-baseweb="input"] input {
        direction: ltr !important;
        text-align: left !important;
        font-family: 'Courier New', Courier, monospace !important;
    }

    /* تخصيص خانات الإدخال والاختيارات */
    .stTextInput > div > div > input, .stSelectbox > div > div {
        background-color: #161b22 !important;
        color: #3fb950 !important;
        border: 1px solid #30363d !important;
        border-radius: 6px;
    }

    /* أزرار الإرسال والتفاعل */
    .stButton > button {
        width: 100%;
        background-color: #238636 !important;
        color: #ffffff !important;
        border: none !important;
        font-weight: bold;
        padding: 10px 20px;
        border-radius: 6px;
    }
    .stButton > button:hover {
        background-color: #2ea043 !important;
        box-shadow: 0 0 10px #2ea043;
    }

    /* بطاقات التحدي */
    .challenge-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 8px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة التحدي
st.title("🛡️ تحدي البرمجة وأمن المعلومات")
st.write("أهلاً بك يا بطل! قم بتحليل السيناريوهات والأكواد التالية بعناية، ثم أجب عن الأسئلة لتأكيد تسليم الواجب.")

st.divider()

# اسم الطالب
student_name = st.text_input("أدخل اسمك الثلاثي لتأكيد التسليم:")

st.divider()

# ----------------- التحدي 1 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 1: تمثيل الألوان بالنظام الثنائي")
st.write("إذا كان لدينا لون في نظام RGB ممثل بالشيفرة الثنائية التالية المكونة من 24 بت:")
st.code("11111111 00000000 00000000", language="binary")
q1_input = st.selectbox(
    "ما هو اللون الصريح الذي تمثله هذه القيمة؟",
    ["اختر الإجابة...", "الأسود (Black)", "الأحمر (Red)", "الأخضر (Green)", "الأبيض (White)"]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 2 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 2: فك تشفير القيم السداسية العشرية (Hex Decoding)")
st.write("قام نظام أمني بتسجيل القيمة السداسية العشرية التالية المكونة لكلمة مرور:")
st.code("50 61 73 73 77 6f 72 64", language="hex")
q2_input = st.text_input("ما هو النص الصريح (Plaintext) المكون لهذه القيمة؟ (اكتب الكلمة بالإنجليزية كما هي)")
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 3 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 3: حجم الحروف في معايير الترميز (UTF)")
st.write("عند تخزين حرف إنجليزي أساسي من جدول ASCII مثل الحرف 'A'، كم عدد البايتات التي يحتاجها الحرف عند استخدام UTF-8 و UTF-32 على التوالي؟")
q3_input = st.radio(
    "اختر الإجابة الصحيحة:",
    [
        "اختر الإجابة...",
        "1 بايت في UTF-8، و 4 بايتات في UTF-32",
        "4 بايتات في UTF-8، و 1 بايت في UTF-32",
        "2 بايت في UTF-8، و 2 بايت في UTF-32",
        "1 بايت في UTF-8، و 1 بايت في UTF-32"
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 4 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 4: تتبع أتمتة الأمن بـ Python")
code_q4 = """failed_attempts = int(input("Enter failed attempts: "))

if failed_attempts > 5:
    print("[ALERT] Account Suspended!")
elif 1 <= failed_attempts <= 5:
    remaining = 5 - failed_attempts
    print(f"[WARNING] Remaining attempts: {remaining}")
else:
    print("[INFO] Access Granted.")"""
st.code(code_q4, language="python")
q4_input = st.selectbox(
    "إذا أدخل المستخدم الرقم 7، ما هي الرسالة التي ستظهر في شاشة الكونسول؟",
    [
        "اختر الإجابة...",
        "[INFO] Access Granted.",
        "[WARNING] Remaining attempts: -2",
        "[ALERT] Account Suspended!"
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 5 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 5: تتبع الحلقات التكرارية (While Loops)")
code_q5 = """secret = 10
guess = 0
tries = 0

while guess != secret:
    guess = int(input("Enter guess: "))
    tries += 1

print(tries)"""
st.code(code_q5, language="python")
q5_input = st.selectbox(
    "إذا أدخل المستخدم الأرقام التالية بالترتيب (3, 7, 10)، ما هي القيمة النهائية التي سيعرضها أمر print(tries)؟",
    ["اختر الإجابة...", "1", "2", "3", "10"]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 6 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 6: تحليل ثغرة حقن قواعد البيانات (SQLi)")
st.code("SELECT * FROM users WHERE username = 'admin' AND password = '' OR '1'='1';", language="sql")
q6_input = st.radio(
    "كيف أثر المشغّل المنطقي OR والشرط '1'='1' على أمان هذا الاستعلام؟",
    [
        "اختر الإجابة...",
        "قام بتشفير كلمة المرور تلقائياً لحمايتها",
        "جعل الشرط دائم الصحة (TRUE) بغض النظر عن كلمة المرور مما أدى لتجاوز الفحص",
        "تسبب في إغلاق محرك قواعد البيانات وحذف كافة السجلات"
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 7 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 7: استعلامات التصفية والفرز في SQL")
st.write("نريد كتابة استعلام SQL يسترجع جميع الطلبات من جدول `Orders` بشرط أن يكون المشروب `Coffee` وفقط مرتبة من السعر الأعلى إلى السعر الأقل.")
q7_input = st.selectbox(
    "ما هو الاستعلام الصحيح للقيام بذلك؟",
    [
        "اختر الإجابة...",
        "SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price DESC;",
        "SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price ASC;",
        "SELECT Coffee FROM Orders SORT BY price;",
        "SELECT * FROM Orders ORDER BY drink WHERE price DESC;"
    ]
)
st.markdown('</div>', unsafe_allow_html=True)

# ----------------- التحدي 8 -----------------
st.markdown('<div class="challenge-card">', unsafe_allow_html=True)
st.subheader("🚩 التحدي 8: التحويل من السداسي عشري إلى العشري")
st.write("إذا كان لدينا القيمة السداسية العشرية `AB` المخزنة في الذاكرة:")
st.code("AB (Hexadecimal)", language="text")
q8_input = st.number_input("ما هي القيمة المكافئة لها في النظام العشري (Decimal)؟", min_value=0, max_value=500, value=0)
st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# ----------------- زر إرسال التحدي -----------------
if st.button("تأكيد وتسليم التحدي 🚀"):
    if not student_name.strip():
        st.error("⚠️ يرجى كتابة اسمك أولاً لتأكيد التسليم!")
    else:
        score = 0
        
        # تصحيح الإجابات
        if q1_input == "الأحمر (Red)":
            score += 1
        if q2_input.strip().lower() == "password":
            score += 1
        if "1 بايت في UTF-8، و 4 بايتات في UTF-32" in q3_input:
            score += 1
        if q4_input == "[ALERT] Account Suspended!":
            score += 1
        if q5_input == "3":
            score += 1
        if "جعل الشرط دائم الصحة" in q6_input:
            score += 1
        if q7_input == "SELECT * FROM Orders WHERE drink = 'Coffee' ORDER BY price DESC;":
            score += 1
        if q8_input == 171:
            score += 1

        st.balloons()
        st.success(f"🎉 تم تسليم الواجب بنجاح يا {student_name}!")
        st.markdown(f"### 📊 النتيجة النهائية: `{score} / 8`")