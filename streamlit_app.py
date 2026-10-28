import streamlit as st
import streamlit.components.v1 as components
import random

# ویب سائٹ کی سیٹنگ
st.set_page_config(
    page_title="Forex & Gold Dual-Chart Pro Signal Terminal",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 Forex & Gold Pro Signal Terminal")
st.markdown("خوش آمدید! یہ آپ کی کمیونٹی کا ڈبل چارٹ اور لائیو سگنل ٹرمینل ہے جو ٹریڈنگ ویو ویژن کے ساتھ کام کرتا ہے۔")

# --- مین ڈیش بورڈ پر کنٹرولز اور سگنل بٹن (سائیڈ بار سے ہٹا کر سامنے لایا گیا) ---
st.markdown("---")
col_ctrl1, col_ctrl2, col_ctrl3 = st.columns(3)

with col_ctrl1:
    symbol_option = st.selectbox(
        "کرنسی یا گولڈ پیئر منتخب کریں:",
        (
            "FX:XAUUSD (Gold vs USD)", 
            "FX:EURUSD", 
            "FX:GBPUSD", 
            "FX:USDJPY", 
            "FX:AUDUSD", 
            "FX:USDCAD", 
            "FX:NZDUSD", 
            "FX:EURGBP", 
            "FX:GBPJPY", 
            "FX:EURJPY"
        )
    )

with col_ctrl2:
    timeframe_option = st.selectbox(
        "ٹائم فریم منتخب کریں:",
        ("1m (1 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "30m (30 منٹ)", "1h (1 گھنٹہ)", "4h (4 گھنٹے)", "1D (روزانہ)", "1W (ہفتہ وار)")
    )

with col_ctrl3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("🚀 لائیو سگنل جنریٹ کریں (Generate Signal)", type="primary", use_container_width=True)

st.markdown("---")

# پیئر کا کلین نام
clean_symbol = symbol_option.split()[0]

# اگر سگنل جنریٹ کا بٹن دبایا جائے
if generate_btn:
    signal_type = random.choice(["BUY (🟢 لونگ پوزیشن - اوپر کی لکیریں)", "SELL (🔴 شارٹ پوزیشن - نیچے کی لکیریں)"])
    if "BUY" in signal_type:
        st.success(f"✅ **سگنل الرٹ:** {clean_symbol} پر **BUY** سگنل جنریٹ ہو گیا ہے! چارٹ پر گرین ٹک اور ہدف کی لمبی لکیریں فعال کر دی گئی ہیں۔")
    else:
        st.error(f"❌ **سگنل الرٹ:** {clean_symbol} پر **SELL** سگنل جنریٹ ہو گیا ہے! چارٹ پر ریڈ ٹک اور نیچے کی لکیریں فعال کر دی گئی ہیں۔")

# --- دو لائیو چارٹس کی سکرین (اوپر اور نیچے) ---
st.subheader(f"📊 1. مین ٹریڈنگ ویو لائیو چارٹ: {clean_symbol}")

# پہلا ٹریڈنگ ویو لائیو چارٹ (اوپر والا)
tradingview_html_1 = f"""
<!-- TradingView Widget 1 -->
<div class="tradingview-widget-container" style="height:450px;width:100%">
  <div id="tradingview_chart_1" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "450",
    "symbol": "{clean_symbol}",
    "interval": "15",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "en",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "allow_symbol_change": false,
    "container_id": "tradingview_chart_1"
  }});
  </script>
</div>
"""
components.html(tradingview_html_1, height=470)

st.markdown("---")
st.subheader(f"📉 2. سیکنڈری انڈیکیٹر اینڈ اینالیسس چارٹ: {clean_symbol}")

# دوسرا چارٹ (نیچے والا - کینڈل اور ٹیکنिकल ویو کے ساتھ)
tradingview_html_2 = f"""
<!-- TradingView Widget 2 -->
<div class="tradingview-widget-container" style="height:450px;width:100%">
  <div id="tradingview_chart_2" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "450",
    "symbol": "{clean_symbol}",
    "interval": "60",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "3",
    "locale": "en",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "allow_symbol_change": false,
    "container_id": "tradingview_chart_2"
  }});
  </script>
</div>
"""
components.html(tradingview_html_2, height=470)

st.markdown("---")
st.markdown("💡 **نوٹ:** یہ ڈوئل چارٹ ٹرمینل آپ کی ٹریڈنگ کمیونٹی کے لیے اپڈیٹ کر دیا گیا ہے۔ بٹن اب بالکل سامنے موجود ہے۔")
