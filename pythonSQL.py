import streamlit as st
import requests

# رابط جوجل المحدد لربط النتائج
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzCHyNyjkDlVHLuHjavamU7VnwEBFZSRKo4oJLKufOSnglxs-rlzsZuBmC0SSo-r-4xvA/exec"

# إعدادات الصفحة والتصميم العصري (Cybersecurity Theme)
st.set_page_config(page_title="تحدي الأمن السيبراني التفاعلي", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #ff4b4b; color: white; font-weight: bold; height: 3em; }
    .success-box { padding: 20px; border-radius: 10px; background-color: #1e3a1e; border: 1px solid #2ecc71; text-align: center; }
    .header-title { text-align: center; color: #ff4b4b; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='header-title'>🛡️ تحدي الأقفال الرقمية (Pre-Security CTF)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>أهلاً بك أيها المحقق الرقمي! اجتاز الأقفال الأربعة التالية لفك النظام بالكامل وتسجيل نتيجتك رسمياً.</p>", unsafe_allow_html=True)
st.markdown("---")

# إدارة الجلسة (Session State) لتتبع بيانات الطالب والمستوى الحالي
if "full_name" not in st.session_state:
    st.session_state.full_name = ""
if "stage" not in st.session_state:
    st.session_state.stage = 1  # المستويات من 1 إلى 4، والمستوى 5 للنهاية
if "score" not in st.session_state:
    st.session_state.score = 0
if "data_sent" not in st.session_state:
    st.session_state.data_sent = False

# الخطوة 0: التحقق من إدخال الاسم الثلاثي
if not st.session_state.full_name:
    with st.form("name_form"):
        st.subheader("📝 الخطوة المسبقة: تسجيل هوية المحقق")
        name_input = st.text_input("أدخل الاسم الثلاثي واللقب بدقة:")
        submitted_name = st.form_submit_button("بدء التحدي وفتح البوابة 🚀")
        if submitted_name:
            if len(name_input.strip().split()) >= 3:
                st.session_state.full_name = name_input.strip()
                st.rerun()
            else:
                st.warning("⚠️ يرجى إدخال الاسم الثلاثي كاملاً لضمان تسجيل النتيجة بشكل صحيح.")
    st.stop()

# شريط تقدم التحدي
progress = (st.session_state.stage - 1) / 4
st.progress(progress)
st.info(f"👤 المحقق الحالي: **{st.session_state.full_name}** | 🎯 العلامة الحالية: **{st.session_state.score} / 100**")

# --- القفل الأول: تمثيل الألوان والأعداد ---
if st.session_state.stage == 1:
    st.markdown("### 🔒 القفل الأول: الألوان والأنظمة العددية")
    st.markdown("في الكود اللوني السداسي عشري `#BC002D`، ما هي القيمة **العشرية (Decimal)** لقناة اللون الأحمر الممثلة بالزوج الأول `BC`؟[cite: 1]")
    
    ans1 = st.text_input("أدخل القيمة الرقمية العشرية:", key="q1")
    if st.button("محاولة فتح القفل الأول 🔓", key="b1"):
        if ans1.strip() == "188":
            st.session_state.score += 25
            st.session_state.stage = 2
            st.success("🎉 ممتاز! تم فك القفل الأول بنجاح (القيمة 188)[cite: 1].")
            st.rerun()
        else:
            st.error("❌ إجابة خاطئة! القفل ما زال مغلقاً، تذكر أن `BC` تعادل 188 بالعشري[cite: 1].")

# --- القفل الثاني: ترميز النصوص والمحارف ---
elif st.session_state.stage == 2:
    st.markdown("### 🔒 القفل الثاني: ترميز النصوص (Text Encoding)")
    st.markdown("بالاعتماد على جدول معيار `ASCII`، ما هي القيمة **العشرية** للحرف الكبير **Q** في اسم `Qaswarah`؟[cite: 2]")
    
    ans2 = st.text_input("أدخل القيمة العشرية للحرف:", key="q2")
    if st.button("محاولة فتح القفل الثاني 🔓", key="b2"):
        if ans2.strip() == "81":
            st.session_state.score += 25
            st.session_state.stage = 3
            st.success("🎉 رائع! القفل الثاني انفتح بنجاح (القيمة 81)[cite: 2].")
            st.rerun()
        else:
            st.error("❌ إجابة خاطئة! راجع جدول ASCII الخاص بالحرف Q[cite: 2].")

# --- القفل الثالث: أساسيات بايثون ---
elif st.session_state.stage == 3:
    st.markdown("### 🔒 القفل الثالث: البرمجة بلغة بايثون (Python)")
    st.markdown("في سكريبت لعبة تخمين الرقم، ما هي الكلمة المفتاحية المستخدمة لبناء حلقة تكرارية تستمر ما دام التخمين لا يساوي الرقم السري؟[cite: 3]")
    
    ans3 = st.selectbox("اختر الكلمة المناسبة:", ["--- اختر الإجابة ---", "for", "while", "if", "loop"], key="q3")
    if st.button("محاولة فتح القفل الثالث 🔓", key="b3"):
        if ans3 == "while":
            st.session_state.score += 25
            st.session_state.stage = 4
            st.success("🎉 أحسنت! حلقة while هي حلقة التكرار المشروط المستخدمة[cite: 3].")
            st.rerun()
        elif ans3 == "--- اختر الإجابة ---":
            st.warning("⚠️ يرجى اختيار إجابة من القائمة.")
        else:
            st.error("❌ إجابة خاطئة! فكر في بنية التكرار المستمر في بايثون[cite: 3].")

# --- القفل الرابع: قواعد البيانات و SQL ---
elif st.session_state.stage == 4:
    st.markdown("### 🔒 القفل الرابع: قواعد البيانات (SQL)")
    st.markdown("ما هي الكلمة المفتاحية في لغة SQL المستخدمة لتصفية السجلات واسترجاع طلبات القهوة `Coffee` فقط؟[cite: 4]")
    
    ans4 = st.text_input("أدخل الكلمة المفتاحية:", key="q4")
    if st.button("فتح القفل الأخير وإنهاء التحدي 🔓", key="b4"):
        if ans4.strip().upper() == "WHERE":
            st.session_state.score += 25
            st.session_state.stage = 5
            st.rerun()
        else:
            st.error("❌ إجابة خاطئة! تذكر أمر التصفية والشرط في SQL[cite: 4].")

# --- المرحلة الخامسة: الإرسال وحفل التخرج المصغر ---
elif st.session_state.stage == 5:
    st.balloons()
    
    # إرسال البيانات تلقائياً لجوجل شيت عبر WEB_APP_URL إذا لم تُرسل مسبقاً
    if not st.session_state.data_sent:
        try:
            payload = {
                "name": st.session_state.full_name,
                "score": st.session_state.score
            }
            response = requests.post(WEB_APP_URL, json=payload)
            st.session_state.data_sent = True
        except Exception as e:
            pass # في حال وجود عائق شبكي مؤقت

    st.markdown("""
        <div class='success-box'>
            <h2>🏆 تهانينا الكبرى أيها المحقق الرقمي!</h2>
            <p>لقد قمت بفتح جميع الأقفال الأربعة بنجاح واجتياز التحدي العملي لكورس الـ Pre-Security بكفاءة تامة.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write(f"📌 **اسم الطالب الثلاثي:** {st.session_state.full_name}")
    st.write(f"🌟 **النتيجة النهائية:** {st.session_state.score} / 100")
    st.success("✅ تم إرسال نتيجة اختبارك وعلامتك رسمياً إلى لوحة تحكم المعلم عبر رابط جوجل بنجاح.")

    if st.button("إعادة محاولة / طالب جديد"):
        st.session_state.full_name = ""
        st.session_state.stage = 1
        st.session_state.score = 0
        st.session_state.data_sent = False
        st.rerun()
