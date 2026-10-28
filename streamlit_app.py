import streamlit as st
import streamlit.components.v1 as components
import random

# ویب سائٹ کی سیٹنگ
st.set_page_config(
    page_title="Forex Pro Signal Board - Community Edition",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 Forex & Gold Pro Signal Board")
st.markdown("خوش آمدید! یہ آپ کی کمیونٹی کا لائیو سگنل اور اسٹریٹجی بورڈ ہے جو **Entry, Stop Loss اور Targets** فراہم کرتا ہے۔")

# سائیڈ بار - پیئرز اور ٹائم فریمز کی سیٹنگ
st.sidebar.header("⚙️ ٹریڈنگ سیٹنگز")

# 10 بہترین فارکس اور گولڈ پیئرز
symbol_option = st.sidebar.selectbox(
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

# ٹائم فریمز کی لسٹ
timeframe_option = st.sidebar.selectbox(
    "ٹائم فریم منتخب کریں:",
    ("1m (1 منٹ)", "3m (3 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "30m (30 منٹ)", "1h (1 گھنٹہ)", "4h (4 گھنٹے)", "1D (روزانہ)", "1W (ہفتہ وار)")
)

# سگنل جنریٹ کرنے کا بٹن
if st.sidebar.button("🔍 سگنل جنریٹ کریں (Generate Signal)"):
    st.sidebar.success("اسٹریٹجی کا تجزیہ مکمل ہو گیا!")
    
    # فرضی یا لائیو مارکیٹ ریٹ کی بنیاد پر لیولز بنانا (مثال کے طور پر گولڈ یا فارکس کے لیے)
    base_price = 2650.00 if "XAUUSD" in symbol_option else 1.0850
    
    entry_price = base_price
    stop_loss = base_price - 15.0 if "XAUUSD" in symbol_option else base_price - 0.0030
    tp1 = base_price + 20.0 if "XAUUSD" in symbol_option else base_price + 0.0040
    tp2 = base_price + 40.0 if "XAUUSD" in symbol_option else base_price + 0.0080
    tp3 = base_price + 70.0 if "XAUUSD" in symbol_option else base_price + 0.0120
    
    # سکرین پر زبردست انداز میں ڈسپلے کرنا
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.error(f"🛑 Stop Loss\n\n**{stop_loss:.2f}**")
    with col2:
        st.info(f"📍 Entry Price\n\n**{entry_price:.2f}**")
    with col3:
        st.success(f"🎯 Target 1 (TP1)\n\n**{tp1:.2f}**")
    with col4:
        st.success(f"🎯 Target 2 (TP2)\n\n**{tp2:.2f}**")
    with col5:
        st.success(f"🎯 Target 3 (TP3)\n\n**{tp3:.2f}**")
        
    st.markdown("---")

# --- TradingView Live Chart Widget ---
clean_symbol = symbol_option.split()[0]
st.subheader(f"📊 لائیو چارٹ: {clean_symbol} | ٹائم فریم: {timeframe_option}")

# ٹریڈنگ ویو لائیو چارٹ
tradingview_html = f"""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:550px;width:100%">
  <div id="tradingview_chart" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "550",
    "symbol": "{clean_symbol}",
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

components.html(tradingview_html, height=570)

st.markdown("---")
st.markdown("💡 **نوٹ:** یہ پلیٹ فارم آپ کی ٹریڈنگ کمیونٹی کے لیے ڈیزائن کیا گیا ہے۔ ہمیشہ اپنے رسک مینجمنٹ کا خیال رکھیں۔")
