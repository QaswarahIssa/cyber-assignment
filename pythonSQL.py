import streamlit as st
import requests

# رابط جوجل المحدد لربط النتائج
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzCHyNyjkDlVHLuHjavamU7VnwEBFZSRKo4oJLKufOSnglxs-rlzsZuBmC0SSo-r-4xvA/exec"

# إعدادات الصفحة
st.set_page_config(page_title="تحدي الأمن السيبراني التفاعلي", page_icon="🛡️", layout="centered")

# تنسيق CSS لضمان محاذاة الواجهة من اليمين لليسار، وبقاء حقول الإجابة والأكواد من اليسار لليمين
st.markdown("""
    <style>
    /* الاتجاه العام من اليمين لليسار */
    .main {
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* محاذاة عناصر العناوين والنصوص لليمين */
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        direction: rtl;
        text-align: right;
    }
    
    /* محاذاة حقول إدخال النص والأسماء من اليمين لليسار (أو حسب رغبة الطالب) */
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
    }
    
    /* تنسيق خاص للأكواد والمدخلات التقنية لتكون من اليسار لليمين (LTR) بوضوح */
    code, pre, .code-box {
        direction: ltr !important;
        text-align: left !important;
        unicode-bidi: embed;
        background-color: #161b22;
        padding: 2px 6px;
        border-radius: 4px;
        color: #ff7b72;
    }

    /* تنسيق الأزرار */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        height: 3em;
    }
    </style>
""", unsafe_allow_html=True)

# ترويسة التطبيق
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🛡️ تحدي الأقفال الرقمية (Pre-Security CTF)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>أهلاً بك أيها المحقق الرقمي! قم بتعبئة بياناتك والإجابة عن الأسئلة الأربعة في صفحة واحدة، ثم اضغط على زر إرسال النتيجة.</p>", unsafe_allow_html=True)
st.markdown("---")

# نموذج لجمع الاسم وإجابات الأسئلة في صفحة واحدة
with st.form("ctf_form"):
    
    # حقل إدخال الاسم الثلاثي
    st.subheader("📝 1. هوية المحقق")
    full_name = st.text_input("أدخل الاسم الثلاثي واللقب بدقة:")
    
    st.markdown("---")
    st.subheader("🔒 2. تحدي الأقفال الأربعة")

    # القفل الأول
    st.markdown("##### القفل الأول: الألوان والأنظمة العددية")
    st.markdown("في الكود اللوني السداسي عشري <code>#BC002D</code>، ما هي القيمة <b>العشرية (Decimal)</b> لقناة اللون الأحمر الممثلة بالزوج الأول <code>BC</code>؟", unsafe_allow_html=True)
    ans1 = st.text_input("إجابة القفل الأول (مثال: رقم عشري):", key="q1")

    st.markdown("")

    # القفل الثاني
    st.markdown("##### القفل الثاني: ترميز النصوص (Text Encoding)")
    st.markdown("بالاعتماد على جدول معيار <code>ASCII</code>، ما هي القيمة <b>العشرية</b> للحرف الكبير <code>Q</code> في اسم <code>Qaswarah</code>؟", unsafe_allow_html=True)
    ans2 = st.text_input("إجابة القفل الثاني (مثال: رقم عشري):", key="q2")

    st.markdown("")

    # القفل الثالث
    st.markdown("##### القفل الثالث: البرمجة بلغة بايثون (Python)")
    st.markdown("في سكريبت لعبة تخمين الرقم، ما هي الكلمة المفتاحية المستخدمة لبناء حلقة تكرارية تستمر ما دام التخمين لا يساوي الرقم السري؟")
    ans3 = st.selectbox("اختر الإجابة:", ["--- اختر الإجابة البرمجية ---", "for", "while", "if", "loop"], key="q3")

    st.markdown("")

    # القفل الرابع
    st.markdown("##### القفل الرابع: قواعد البيانات (SQL)")
    st.markdown("ما هي الكلمة المفتاحية في لغة <code>SQL</code> المستخدمة لتصفية السجلات واسترجاع طلبات القهوة <code>Coffee</code> فقط؟", unsafe_allow_html=True)
    ans4 = st.text_input("إجابة القفل الرابع (مثال: كلمة مفتاحية):", key="q4")

    st.markdown("---")
    
    # زر الإرسال النهائي
    submit_btn = st.form_submit_button("تقييم الإجابات وإرسال النتيجة 🚀")

# عند الضغط على زر الإرسال
if submit_btn:
    # التحقق من الاسم الثلاثي
    if not full_name or len(full_name.strip().split()) < 3:
        st.warning("⚠️ يرجى إدخال الاسم الثلاثي واللقب بدقة قبل إرسال النتيجة.")
    else:
        # حساب العلامة
        score = 0
        results_details = []

        # تصحيح السؤال الأول
        if ans1.strip() == "188":
            score += 25
            results_details.append("✅ القفل الأول: صحيح (188)")
        else:
            results_details.append("❌ القفل الأول: خطأ (الصحيح هو 188)")

        # تصحيح السؤال الثاني
        if ans2.strip() == "81":
            score += 25
            results_details.append("✅ القفل الثاني: صحيح (81)")
        else:
            results_details.append("❌ القفل الثاني: خطأ (الصحيح هو 81)")

        # تصحيح السؤال الثالث
        if ans3 == "while":
            score += 25
            results_details.append("✅ القفل الثالث: صحيح (while)")
        else:
            results_details.append("❌ القفل الثالث: خطأ (الصحيح هو while)")

        # تصحيح السؤال الرابع
        if ans4.strip().upper() == "WHERE":
            score += 25
            results_details.append("✅ القفل الرابع: صحيح (WHERE)")
        else:
            results_details.append("❌ القفل الرابع: خطأ (الصحيح هو WHERE)")

        # محاولة إرسال البيانات إلى جوجل شيت
        try:
            payload = {
                "name": full_name.strip(),
                "score": score
            }
            response = requests.post(WEB_APP_URL, json=payload)
            success_sent = True
        except Exception as e:
            success_sent = False

        # عرض النتيجة للطالب
        st.balloons()
        st.markdown(f"### 📊 تقرير النتائج للمحقق: {full_name.strip()}")
        st.info(f"🌟 **علامتك النهائية:** {score} / 100")

        st.markdown("**تفاصيل الإجابات:**")
        for res in results_details:
            st.write(res)

        if success_sent:
            st.success("✅ تم إرسال نتيجة اختبارك وعلامتك إلى لوحة تحكم المعلم بنجاح عبر رابط جوجل!")
        else:
            st.warning("⚠️ تم احتساب النتيجة، ولكن تعذر الإرسال التلقائي للرابط حالياً بسبب اتصال الشبكة.")
