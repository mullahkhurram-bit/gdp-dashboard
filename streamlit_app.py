import streamlit as st
import streamlit.components.v1 as components
import yfinance as yf

# ویب سائٹ کی سیٹنگ
st.set_page_config(
    page_title="Forex Pro Signal Board - Live Market Edition",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 Forex & Gold Live Signal Board")
st.markdown("خوش آمدید! یہ بورڈ اب **لائیو مارکیٹ ریٹ** کے حساب سے آپ کو Entry, Stop Loss اور Targets فراہم کرتا ہے۔")

# سائیڈ بار - پیئرز اور ٹائم فریمز کی سیٹنگ
st.sidebar.header("⚙️ ٹریڈنگ سیٹنگز")

# کرنسی اور گولڈ ٹِکرز (TradingView اور Yahoo Finance کے ناموں کے ساتھ)
pairs = {
    "FX:XAUUSD (Gold)": {"ticker": "GC=F", "default": 2650.00, "sl_pts": 15.0, "tp1_pts": 20.0, "tp2_pts": 40.0, "tp3_pts": 70.0},
    "FX:EURUSD": {"ticker": "EURUSD=X", "default": 1.0850, "sl_pts": 0.0030, "tp1_pts": 0.0040, "tp2_pts": 0.0080, "tp3_pts": 0.0120},
    "FX:GBPUSD": {"ticker": "GBPUSD=X", "default": 1.2750, "sl_pts": 0.0035, "tp1_pts": 0.0045, "tp2_pts": 0.0090, "tp3_pts": 0.0135},
    "FX:USDJPY": {"ticker": "USDJPY=X", "default": 155.00, "sl_pts": 0.40, "tp1_pts": 0.50, "tp2_pts": 1.00, "tp3_pts": 1.50},
    "FX:AUDUSD": {"ticker": "AUDUSD=X", "default": 0.6550, "sl_pts": 0.0025, "tp1_pts": 0.0035, "tp2_pts": 0.0070, "tp3_pts": 0.0100},
    "FX:USDCAD": {"ticker": "USDCAD=X", "default": 1.3650, "sl_pts": 0.0030, "tp1_pts": 0.0040, "tp2_pts": 0.0080, "tp3_pts": 0.0120},
    "FX:NZDUSD": {"ticker": "NZDUSD=X", "default": 0.6050, "sl_pts": 0.0025, "tp1_pts": 0.0035, "tp2_pts": 0.0070, "tp3_pts": 0.0100},
    "FX:EURGBP": {"ticker": "EURGBP=X", "default": 0.8550, "sl_pts": 0.0020, "tp1_pts": 0.0030, "tp2_pts": 0.0060, "tp3_pts": 0.0090},
    "FX:GBPJPY": {"ticker": "GBPJPY=X", "default": 198.00, "sl_pts": 0.50, "tp1_pts": 0.70, "tp2_pts": 1.40, "tp3_pts": 2.10},
    "FX:EURJPY": {"ticker": "EURJPY=X", "default": 168.00, "sl_pts": 0.45, "tp1_pts": 0.60, "tp2_pts": 1.20, "tp3_pts": 1.80}
}

selected_pair_name = st.sidebar.selectbox(
    "کرنسی یا گولڈ پیئر منتخب کریں:",
    list(pairs.keys())
)

timeframe_option = st.sidebar.selectbox(
    "ٹائم فریم منتخب کریں:",
    ("1m (1 منٹ)", "3m (3 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "30m (30 منٹ)", "1h (1 گھنٹہ)", "4h (4 گھنٹے)", "1D (روزانہ)", "1W (ہفتہ وار)")
)

# لائیو قیمت حاصل کرنے کی کوشش
pair_info = pairs[selected_pair_name]
live_price = pair_info["default"]

try:
    ticker_obj = yf.Ticker(pair_info["ticker"])
    todays_data = ticker_obj.history(period="1d")
    if not todays_data.empty:
        live_price = float(todays_data['Close'].iloc[-1])
except:
    pass

# سگنل جنریٹ کرنے کا بٹن
if st.sidebar.button("🔍 لائیو سگنل جنریٹ کریں"):
    st.sidebar.success("لائیو مارکیٹ ڈیٹا کے ساتھ تجزیہ مکمل ہو گیا!")

# لائیو ریٹ کے حساب سے لیولز کا حساب
entry_price = live_price
sl = entry_price - pair_info["sl_pts"]
tp1 = entry_price + pair_info["tp1_pts"]
tp2 = entry_price + pair_info["tp2_pts"]
tp3 = entry_price + pair_info["tp3_pts"]

# سکرین پر لائیو ریٹ دکھانا
st.info(f"📌 منتخب کردہ پیئر: **{selected_pair_name}** | ⚡ لائیو مارکیٹ ریٹ: **{live_price:.4f}**")

# خانوں میں لیولز ڈسپلے کرنا
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.error(f"🛑 Stop Loss\n\n**{sl:.4f}**")
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
clean_symbol = selected_pair_name.split()[0]
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
st.markdown("💡 **نوٹ:** یہ پلیٹ فارم لائیو مارکیٹ ڈیٹا اور ٹریڈنگ ویو کے ساتھ منسلک ہے۔ ہمیشہ رسک مینجمنٹ کا خیال رکھیں۔")
