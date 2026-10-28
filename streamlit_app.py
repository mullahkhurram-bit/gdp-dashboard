import streamlit as st
import streamlit.components.v1 as components
import random

# ویب سائٹ کی سیٹنگ اور ٹائٹل
st.set_page_config(
    page_title="Forex Live Signal Board - Community Edition",
    page_icon="📈",
    layout="wide"
)

# کمیونٹی کے لیے ہیڈنگ
st.title("🚀 Forex Live Signal Board & Strategy Dashboard")
st.markdown("خوش آمدید! یہ بورڈ **Auction Market Theory** اور **Market Profile** کی اسٹریٹجی کے مطابق سگنل دکھاتا ہے۔")

# سائیڈ بار (Side Bar) - کرنسی جوڑا منتخب کرنے کے لیے
st.sidebar.header("⚙️ ٹریڈنگ سیٹنگز")
symbol_option = st.sidebar.selectbox(
    "کرنسی یا مارکیٹ منتخب کریں:",
    ("FX:EURUSD", "FX:GBPUSD", "FX:USDJPY", "FX:XAUUSD (Gold)", "CRYPTO:BTCUSD")
)

# سگنل جنریٹ کرنے کا بٹن
if st.sidebar.button("🔍 لائیو سگنل چیک کریں"):
    st.sidebar.success("مارکیٹ کا تجزیہ مکمل ہو گیا!")
    
    # فرضی یا لائیو اسٹریٹجی سگنल کی مثال (آپ یہاں اپنی اصل اسٹریٹجی کا لاجک لگا سکتے ہیں)
    signals = ["STRONG BUY (خریدیں)", "STRONG SELL (بیچیں)", "WAIT / CONSOLIDATION (انتظار کریں)"]
    chosen_signal = random.choice(signals)
    
    if "BUY" in chosen_signal:
        st.success(f"📊 سگنل: {chosen_signal} | لوکیشن: Out of Balance (Bullish)")
    elif "SELL" in chosen_signal:
        st.error(f"📊 سگنل: {chosen_signal} | لوکیشن: Out of Balance (Bearish)")
    else:
        st.warning(f"📊 سگنل: {chosen_signal} | مارکیٹ اس وقت بیلنس (Balance Area) میں ہے۔")

# --- TradingView Live Chart Widget ---
st.subheader(f"📊 لائیو چارٹ: {symbol_option}")

# ٹریڈنگ ویو کا فری لائیو چارٹ ویجیٹ
tradingview_html = f"""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:500px;width:100%">
  <div id="tradingview_chart" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "500",
    "symbol": "{symbol_option.split()[0]}",
    "interval": "15",
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
<!-- TradingView Widget END -->
"""

# ویب سائٹ پر چارٹ دکھانا
components.html(tradingview_html, height=520)

# نیچے کمیونٹی کے لیے معلومات
st.markdown("---")
st.markdown("💡 **نوٹ:** یہ پلیٹ فارم آپ کی کمیونٹی کے لیے بالکل مفت تیار کیا گیا ہے۔ ٹریڈ ہمیشہ اپنے رسک مینجمنٹ اور بروکر کے مطابق کریں۔")
