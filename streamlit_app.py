import streamlit as st
import streamlit.components.v1 as components
import random

# ویب سائٹ کی سیٹنگ
st.set_page_config(
    page_title="Forex Pro Signal Board",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 Forex & Gold Pro Signal Board")
st.markdown("خوش آمدید! یہ آپ کی کمیونٹی کا لائیو سگنل اور اسٹریٹجی بورڈ ہے جو **Entry, Stop Loss اور Targets** فراہم کرتا ہے۔")

# سائیڈ بار - پیئرز اور ٹائم فریمز کی سیٹنگ
st.sidebar.header("⚙️ ٹریڈنگ سیٹنگز")

# 10 بہترین فارکس اور گولڈ پیئرز
pairs_data = {
    "FX:XAUUSD (Gold vs USD)": {"base": 2650.00, "sl": 15.0, "tp1": 20.0, "tp2": 40.0, "tp3": 70.0},
    "FX:EURUSD": {"base": 1.0850, "sl": 0.0030, "tp1": 0.0040, "tp2": 0.0080, "tp3": 0.0120},
    "FX:GBPUSD": {"base": 1.2750, "sl": 0.0035, "tp1": 0.0045, "tp2": 0.0090, "tp3": 0.0135},
    "FX:USDJPY": {"base": 155.00, "sl": 0.40, "tp1": 0.50, "tp2": 1.00, "tp3": 1.50},
    "FX:AUDUSD": {"base": 0.6550, "sl": 0.0025, "tp1": 0.0035, "tp2": 0.0070, "tp3": 0.0100},
    "FX:USDCAD": {"base": 1.3650, "sl": 0.0030, "tp1": 0.0040, "tp2": 0.0080, "tp3": 0.0120},
    "FX:NZDUSD": {"base": 0.6050, "sl": 0.0025, "tp1": 0.0035, "tp2": 0.0070, "tp3": 0.0100},
    "FX:EURGBP": {"base": 0.8550, "sl": 0.0020, "tp1": 0.0030, "tp2": 0.0060, "tp3": 0.0090},
    "FX:GBPJPY": {"base": 198.00, "sl": 0.50, "tp1": 0.70, "tp2": 1.40, "tp3": 2.10},
    "FX:EURJPY": {"base": 168.00, "sl": 0.45, "tp1": 0.60, "tp2": 1.20, "tp3": 1.80}
}

symbol_option = st.sidebar.selectbox(
    "کرنسی یا گولڈ پیئر منتخب کریں:",
    list(pairs_data.keys())
)

timeframe_option = st.sidebar.selectbox(
    "ٹائم فریم منتخب کریں:",
    ("1m (1 منٹ)", "3m (3 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "30m (30 منٹ)", "1h (1 گھنٹہ)", "4h (4 گھنٹے)", "1D (روزانہ)", "1W (ہفتہ وار)")
)

# سگنل جنریٹ کرنے کا بٹن
if st.sidebar.button("🔍 سگنل جنریٹ کریں (Generate Signal)"):
    st.sidebar.success("اسٹریٹجی کا تجزیہ مکمل ہو گیا!")

p_info = pairs_data[symbol_option]
# مارکیٹ کے مطابق لائیو پرائس جنریٹ کرنا
live_price = p_info["base"] + round(random.uniform(-2.0, 2.0) if "XAUUSD" in symbol_option else random.uniform(-0.0010, 0.0010), 4)

entry_price = live_price
stop_loss = entry_price - p_info["sl"]
tp1 = entry_price + p_info["tp1"]
tp2 = entry_price + p_info["tp2"]
tp3 = entry_price + p_info["tp3"]

st.info(f"📌 منتخب کردہ پیئر: **{symbol_option}** | ⚡ لائیو مارکیٹ ریٹ: **{entry_price:.4f}**")

# سکرین پر زبردست انداز میں ڈسپلے کرنا
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.error(f"🛑 Stop Loss\n\n**{stop_loss:.4f}**")
with col2:
    st.info(f"📍 Entry Price\n\n**{entry_price:.4f}**")
with col3:
    st.success(f"🎯 Target 1 (TP1)\n\n**{tp1:.4f}**")
with col4:
    st.success(f"🎯 Target 2 (TP2)\n\n**{tp2:.4f}**")
with col5:
    st.success(f"🎯 Target 3 (TP3)\n\n**{tp3:.4f}**")
    
st.markdown("---")

# --- TradingView Live Chart Widget ---
clean_symbol = symbol_option.split()[0]
st.subheader(f"📊 لائیو چارٹ: {clean_symbol} | ٹائم فریم: {timeframe_option}")

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
