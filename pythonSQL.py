import streamlit as st
import requests

# رابط جوجل المحدث الخاص بك
WEB_APP_URL = "https://script.google.com/macros/s/AKfycbws7Qv6UkPqQ1KlECjSGsBR-X5oDodTFfNxYxNafIYYBLZYYP1kGB9mRukYQPl_nBzpcw/exec"

# إعدادات الصفحة
st.set_page_config(page_title="تحدي الأمن السيبراني ", page_icon="🔐", layout="centered")

# تنسيق CSS لضمان محاذاة الواجهة من اليمين لليسار، والأكواد من اليسار لليمين
st.markdown("""
    <style>
    .main {
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
        color: #ffffff;
    }
    h1, h2, h3, h4, h5, h6, p, label, .stMarkdown {
        direction: rtl;
        text-align: right;
    }
    .stTextInput input, .stSelectbox div[data-baseweb="select"] {
        direction: rtl;
        text-align: right;
    }
    code, pre, .code-box {
        direction: ltr !important;
        text-align: left !important;
        unicode-bidi: embed;
        background-color: #161b22;
        padding: 2px 6px;
        border-radius: 4px;
        color: #ff7b72;
    }
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
st.markdown("<h1 style='text-align: center; color: #ff4b4b;'>🔐 تحدي المحقق الرقمي المتقدم (Pre-Security CTF)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>أهلاً بك أيها المحقق. يتطلب هذا الاختبار تحليلاً دقيقاً لـ 10 تحديات تقنية. أدخل اسمك الثلاثي واجب عن الأسئلة بحذر.</p>", unsafe_allow_html=True)
st.markdown("---")

# نموذج الأسئلة في صفحة واحدة
with st.form("advanced_ctf_form"):
    
    # حقل إدخال الاسم الثلاثي
    st.subheader("📝 1. هوية المحقق الرقمي")
    full_name = st.text_input("أدخل الاسم الثلاثي واللقب بدقة:")
    
    st.markdown("---")
    st.subheader("🔒 2. الأسئلة والتحديات التحليلية (10 أسئلة)")

    # السؤال 1
    st.markdown("##### 1. الأنظمة العددية (Hex to Decimal)")
    st.markdown("ما هي القيمة العشرية (Decimal) الناتجة عن تحويل الرقم السداسي عشري الصارم <code>2F</code>؟", unsafe_allow_html=True)
    q1 = st.text_input("إجابة السؤال 1 (رقم):", key="q1")

    st.markdown("")

    # السؤال 2
    st.markdown("##### 2. تمثيل الألوان الثنائي")
    st.markdown("في كود اللون <code>#00FF00</code>، كم يبلغ مجموع الأجزاء (Bits) النشطة (التي تحمل القيمة 1) في التمثيل الثنائي لقناة اللون الأخضر وحدها؟", unsafe_allow_html=True)
    q2 = st.text_input("إجابة السؤال 2 (رقم):", key="q2")

    st.markdown("")

    # السؤال 3
    st.markdown("##### 3. العمليات البتية (Bitwise Operations)")
    st.markdown("إذا أجرينا عملية <code>12 AND 5</code> في النظام الثنائي، ما هي القيمة العشرية الناتجة؟", unsafe_allow_html=True)
    q3 = st.text_input("إجابة السؤال 3 (رقم):", key="q3")

    st.markdown("")

    # السؤال 4
    st.markdown("##### 4. ترميز النصوص (ASCII Analysis)")
    st.markdown("إذا كانت القيمة العشرية للحرف الكبير <code>A</code> هي 65، فما هي القيمة العشرية للحرف الصغير <code>a</code> في معيار ASCII؟", unsafe_allow_html=True)
    q4 = st.text_input("إجابة السؤال 4 (رقم):", key="q4")

    st.markdown("")

    # السؤال 5
    st.markdown("##### 5. مشاكل التشفير والترميز (Encoding)")
    st.markdown("ما هو المعيار العالمي الشامل الذي وُجد لحل مشكلة احتواء لغات متعددة (مثل العربية والصينية) وعجز معيار ASCII عنها؟", unsafe_allow_html=True)
    q5 = st.selectbox("اختر المعيار:", ["--- اختر الإجابة ---", "ASCII", "Unicode", "Base64", "MD5"], key="q5")

    st.markdown("")

    # السؤال 6
    st.markdown("##### 6. تحليل منطق بايثون (Python Logic)")
    st.markdown("ما هي النتيجة التي ستطبعها الشيفرة التالية: <code>print(type(str(1024)))</code>؟", unsafe_allow_html=True)
    q6 = st.selectbox("اختر نوع البيانات الناتج:", ["--- اختر الإجابة ---", "<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'bool'>"], key="q6")

    st.markdown("")

    # السؤال 7
    st.markdown("##### 7. الحلقات التكرارية في بايثون")
    st.markdown("كم مرة ستقوم حلقة التكرار التالية بتنفيذ الأوامر بداخلها؟ <br><code>for i in range(1, 10, 2):</code>", unsafe_allow_html=True)
    q7 = st.text_input("إجابة السؤال 7 (عدد المرات):", key="q7")

    st.markdown("")

    # السؤال 8
    st.markdown("##### 8. دوال بايثون المدمجة")
    st.markdown("أي من الدوال التالية تُستخدم في بايثون لمعرفة عدد العناصر (الطول) داخل قائمة أو نص؟", unsafe_allow_html=True)
    q8 = st.selectbox("اختر الدالة:", ["--- اختر الإجابة ---", "count()", "size()", "len()", "length()"], key="q8")

    st.markdown("")

    # السؤال 9
    st.markdown("##### 9. قواعد البيانات واستعلامات SQL")
    st.markdown("ما هي الكلمة المفتاحية في لغة SQL المستخدمة حصرياً لترتيب نتائج الاستعلام تصاعدياً أو تنازلياً؟", unsafe_allow_html=True)
    q9 = st.text_input("إجابة السؤال 9:", key="q9")

    st.markdown("")

    # السؤال 10
    st.markdown("##### 10. أمن قواعد البيانات (SQL Injection Concepts)")
    st.markdown("في استعلامات SQL، الرمز الذي يُستخدم عادة كتعليق (Comment) لإيقاف تنفيذ باقي الاستعلام أثناء اختبارات الاختراق هو:", unsafe_allow_html=True)
    q10 = st.text_input("إجابة السؤال 10 (رمز التعليق):", key="q10")

    st.markdown("---")
    
    # زر الإرسال النهائي
    submit_btn = st.form_submit_button("تقييم التحليل وإرسال النتيجة النهائية 🚀")

# عند الضغط على زر الإرسال
if submit_btn:
    if not full_name or len(full_name.strip().split()) < 3:
        st.warning("⚠️ يرجى إدخال الاسم الثلاثي واللقب بدقة قبل إرسال النتيجة.")
    else:
        score = 0
        results_details = []

        # تصحيح الأسئلة
        if q1.strip() == "47":
            score += 10
            results_details.append("✅ س 1: صحيح (47)")
        else:
            results_details.append("❌ س 1: خطأ (الصحيح: 47)")

        if q2.strip() == "8":
            score += 10
            results_details.append("✅ س 2: صحيح (8 بتات)")
        else:
            results_details.append("❌ س 2: خطأ (الصحيح: 8)")

        if q3.strip() == "4":
            score += 10
            results_details.append("✅ س 3: صحيح (4)")
        else:
            results_details.append("❌ س 3: خطأ (الصحيح: 4)")

        if q4.strip() == "97":
            score += 10
            results_details.append("✅ س 4: صحيح (97)")
        else:
            results_details.append("❌ س 4: خطأ (الصحيح: 97)")

        if q5 == "Unicode":
            score += 10
            results_details.append("✅ س 5: صحيح (Unicode)")
        else:
            results_details.append("❌ س 5: خطأ (الصحيح: Unicode)")

        if q6 == "<class 'str'>":
            score += 10
            results_details.append("✅ س 6: صحيح (<class 'str'>)")
        else:
            results_details.append("❌ س 6: خطأ (الصحيح: <class 'str'>)")

        if q7.strip() == "5":
            score += 10
            results_details.append("✅ س 7: صحيح (5 مرات)")
        else:
            results_details.append("❌ س 7: خطأ (الصحيح: 5)")

        if q8 == "len()":
            score += 10
            results_details.append("✅ س 8: صحيح (len())")
        else:
            results_details.append("❌ س 8: خطأ (الصحيح: len())")

        if q9.strip().upper() in ["ORDER BY", "ORDERBY"]:
            score += 10
            results_details.append("✅ س 9: صحيح (ORDER BY)")
        else:
            results_details.append("❌ س 9: خطأ (الصحيح: ORDER BY)")

        if q10.strip() == "--":
            score += 10
            results_details.append("✅ س 10: صحيح (--)")
        else:
            results_details.append("❌ س 10: خطأ (الصحيح: --)")

        # إرسال البيانات لجوجل شيت باستخدام data
        try:
            payload = {
                "name": full_name.strip(),
                "score": score
            }
            response = requests.post(WEB_APP_URL, data=payload)
            success_sent = True
        except Exception as e:
            success_sent = False

        # عرض التقرير النهائي
        st.balloons()
        st.markdown(f"### 📊 تقرير التحليل النهائي للمحقق: {full_name.strip()}")
        st.info(f"🌟 **علامتك النهائية:** {score} / 100")

        st.markdown("**مراجعة تفصيلية للإجابات:**")
        for res in results_details:
            st.write(res)

        if success_sent:
            st.success("✅ تم إرسال الاسم والنتيجة إلى لوحة تحكم المعلم بنجاح عبر رابط جوجل الجديد!")
        else:
            st.warning("⚠️ تم احتساب النتيجة، ولكن تعذر الإرسال التلقائي للرابط حالياً بسبب اتصال الشبكة.")
