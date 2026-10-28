import streamlit as st
import streamlit.components.v1 as components
import random

# ویب سائٹ کی سادی اور صاف سیٹنگ
st.set_page_config(
    page_title="Forex & Gold Simple Terminal",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Forex & Gold Simple Trading Terminal")
st.markdown("خوش آمدید! یہ آپ کا بالکل صاف اور آسان ٹرمینل ہے۔")

st.markdown("---")

# --- ایک ہی لائن میں کنٹرولز (پیئر، ٹائم فریم اور سگنل بٹن) ---
col1, col2, col3 = st.columns([2, 2, 2])

with col1:
    symbol_option = st.selectbox(
        "پیئر منتخب کریں:",
        ("FX:XAUUSD (Gold)", "FX:EURUSD", "FX:GBPUSD", "FX:USDJPY")
    )

with col2:
    timeframe_option = st.selectbox(
        "ٹائم فریم:",
        ("1m (1 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "1h (1 گھنٹہ)")
    )

with col3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("🚀 سگنل جنریٹ کریں", type="primary", use_container_width=True)

st.markdown("---")

clean_symbol = symbol_option.split()[0]

# --- سگنل کا نتیجہ ---
if generate_btn:
    signal_type = random.choice(["BUY", "SELL", "WAIT"])
    
    if signal_type == "BUY":
        st.success(f"🟢 **بائے (BUY) سگنل:** {clean_symbol} پر اوپر جانے کا مضبوط سیٹ اپ بن رہا ہے!")
    elif signal_type == "SELL":
        st.error(f"🔴 **سیل (SELL) سگنل:** {clean_symbol} پر نیچے آنے کا سیٹ اپ بن رہا ہے!")
    else:
        st.warning(f"⏳ **ویٹ (WAIT):** فی الحال مارکیٹ صاف نہیں ہے، صبر کریں۔")

st.markdown("---")

# --- اوپر چھوٹا اور صاف لائیو ٹریڈنگ ویو چارٹ ---
st.subheader(f"📈 لائیو چارٹ: {clean_symbol}")

tradingview_html = f"""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:380px;width:100%">
  <div id="tradingview_chart" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "380",
    "symbol": "{clean_symbol}",
    "interval": "1",
    "timezone": "Etc/UTC",
    "theme": "dark",
    "style": "1",
    "locale": "en",
    "toolbar_bg": "#f1f3f6",
    "enable_publishing": false,
    "allow_symbol_change": true,
    "container_id": "tradingview_chart"
  }});
  </script>
</div>
<!-- TradingViewWidget END -->
"""

components.html(tradingview_html, height=400)
