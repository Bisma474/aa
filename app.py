import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="Bisma Munir Portfolio", page_icon="💼", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
        padding: 20px;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .section-title {
        font-size: 26px;
        margin-top: 30px;
        color: #34495e;
    }
    .service-box {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #888888;
        margin-top: 50px;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        margin-top: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
    }
    button {
        background-color: #2ecc71;
        color: white;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        margin-top: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=120)
st.sidebar.title("👤 My Portfolio")
st.sidebar.markdown("""
**Name:** Bisma Munir  
**Email:** bismamunir474@gmail.com  
**Location:** Pakistan  
""")

# --- MAIN CONTENT ---
st.markdown('<div class="main">', unsafe_allow_html=True)
st.markdown('<div class="title">💼 Welcome to My Professional Portfolio</div>', unsafe_allow_html=True)
st.write("I help businesses and individuals by providing expert services in Copywriting, Data Analysis, and Data Entry.")

# --- ABOUT SECTION ---
st.markdown('<div class="section-title">🧑‍💼 About Me</div>', unsafe_allow_html=True)
st.write("""
I'm a multi-skilled freelancer offering:
- ✍️ SEO-optimized and persuasive **Copywriting**
- 📊 Insightful **Data Analysis** using Python, Excel & Power BI
- ⌨️ Reliable and accurate **Data Entry** services

With a strong attention to detail and passion for helping clients grow, I ensure professional quality in every project.
""")

# --- SERVICES SECTION ---
st.markdown('<div class="section-title">🛠️ Services</div>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("✍️ Copywriting")
    st.write("""
    - Blog posts & articles  
    - Website copy  
    - Product descriptions  
    - Email marketing & ads
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("📊 Data Analysis")
    st.write("""
    - Data cleaning & exploration  
    - Excel dashboards & pivot tables  
    - Visualizations using Power BI / Python  
    - Insights & reporting
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="service-box">', unsafe_allow_html=True)
    st.subheader("⌨️ Data Entry")
    st.write("""
    - Accurate data input  
    - PDF/Word to Excel conversion  
    - Web research & scraping  
    - Formatting and cleanup
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACT FORM ---
st.markdown('<div class="section-title">📩 Contact Me</div>', unsafe_allow_html=True)
contact_form = """
<form action="https://formsubmit.co/bismamunir474@gmail.com" method="POST">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your Message..." rows="5" required></textarea>
     <button type="submit">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<div class="footer">© 2025 Bisma Munir | Built with ❤️ using Streamlit</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
