import time
import random
import streamlit as st

# صفحہ کی سیٹنگ (Wide Mode)
st.set_page_config(
    page_title="Khawar Kaki - Trading Terminal",
    page_icon="🤖",
    layout="wide"
)

# ریٹرو اور پنک ڈارک تھیم کے لیے کسٹم CSS
st.markdown("""
    <style>
    .main {
        background-color: #0d0611;
        color: #ff2a8d;
    }
    .stSidebar {
        background-color: #15091d;
    }
    h1, h2, h3 {
        color: #ff2a8d !important;
        font-family: 'Courier New', monospace;
    }
    .metric-card {
        background-color: #1a0b24;
        border: 1px solid #ff2a8d;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
        box-shadow: 0 0 10px rgba(255, 42, 141, 0.2);
    }
    .scan-box {
        background-color: #12071a;
        border: 1px dashed #ff2a8d;
        padding: 10px;
        font-family: monospace;
        color: #00ffcc;
    }
    </style>
""", unsafe_allow_html=True)

# ٹاپ ہیڈر اور نام
st.markdown("<h1>⚡ KHAWAR KAKI + JEV TERMINAL ⚡</h1>", unsafe_allow_html=True)
st.markdown("<p style='color: #00ffcc;'>Live Node Scanner & Market Intelligence Active[span_0](start_span)[span_0](end_span)</p>", unsafe_allow_html=True)

# فرسٹ رو: چیف، اسکین، ویٹ، سوشل اور رسک ماڈیولز
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown('<div class="metric-card"><h4>CHIEF</h4><p>Last Pick: KHAKHI</p><h2>$12,450</h2></div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card"><h4>SCAN</h4><p>Active Nodes</p><h2>3.14M</h2></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="metric-card"><h4>VET</h4><p>Signal Strength</p><h2>94.2%</h2></div>', unsafe_allow_html=True)

with col4:
    st.markdown('<div class="metric-card"><h4>SOCIAL</h4><p>Sentiment</p><h2>BULLISH</h2></div>', unsafe_allow_html=True)

with col5:
    st.markdown('<div class="metric-card"><h4>RISK</h4><p>Level: Low</p><h2>0.12</h2></div>', unsafe_allow_html=True)

st.markdown("---")

# مڈل سیکشن: مکڑی کی طرح لائیو اسکیننگ اور گراف سیمولیشن
col_left, col_right = st.columns([2, 1])

with col_left:
    st.markdown("### 🕸️ Live Spider Node Scanner & Price Action")
    # فرضی لائیو ڈیٹا کے لیے اسکین باکس
    scan_placeholder = st.empty()
    
    # لائیو بیلنس اور چارٹ سیمولیشن
    chart_placeholder = st.empty()
    
    # لائیو بیلنس کا ڈسپلے
    balance_val = 13738.74 + random.uniform(-50, 50)
    st.metric(label="KHAWAR KAKI LIVE BALANCE (USD)", value=f"${balance_val:,.2f}", delta="+$412.18")

with col_right:
    st.markdown("### 🎛️ Terminal Controls")
    st.text_input("Target Asset", value="XAU/USD (Gold)")
    st.selectbox("Timeframe", ["5s", "1m", "5m", "1h", "1D"])
    
    if st.button("🚀 EXECUTE KHAWAR KAKI SIGNAL", use_container_width=True):
        st.success("Signal Sent Successfully via WhatsApp & MT5!")
        
    st.markdown("---")
    st.markdown("### 📊 Market Feed")
    st.markdown("""
    <div class="scan-box">
    > Initializing JEV core...<br>
    > Scanning volatility rings...<br>
    > Node connection established.<br>
    > Status: READY FOR SCALPING.
    </div>
    """, unsafe_allow_html=True)

# لوپ کے ذریعے اسکیننگ ٹیکسٹ کو لائیو چلانا
for i in range(3):
    nodes = [f"Node_{random.randint(100,999)} -> Linked [OK]", f"Scanning price action block #{i+1}", f"Risk threshold stable: 0.12"]
    scan_placeholder.code("\n".join(nodes))
    time.sleep(0.5)
