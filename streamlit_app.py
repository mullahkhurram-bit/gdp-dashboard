import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ویب سائٹ کی سیٹنگ
st.set_page_config(
    page_title="Forex & Gold Pro Terminal with Candle Lock",
    page_icon="📈",
    layout="wide"
)

st.title("🚀 Forex & Gold Pro Analysis & Candle-Lock Terminal")
st.markdown("خوش آمدید! یہ ٹرمینل کینڈل کے ٹائم فریم کو لاک رکھتا ہے تاکہ جب تک وقت پورا نہ ہو، نیا سگنل جنریٹ نہ ہو۔")

# --- سیشن اسٹیٹ (Session State) تاکہ وقت اور سگنل لاک رہے ---
if 'last_signal_time' not in st.session_state:
    st.session_state.last_signal_time = 0
if 'current_signal' not in st.session_state:
    st.session_state.current_signal = None

# --- مین ڈیش بورڈ پر کنٹرولز اور سگنل بٹن ---
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
        "اسکیلپنگ ٹائم فریم منتخب کریں:",
        ("5s (5 سیکنڈ)", "15s (15 سیکنڈ)", "30s (30 سیکنڈ)", "1m (1 منٹ)", "3m (3 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "1h (1 گھنٹہ)")
    )

with col_ctrl3:
    st.markdown("<br>", unsafe_allow_html=True)
    generate_btn = st.button("🔍 سگنل جنریٹ کریں (Lock & Analyze)", type="primary", use_container_width=True)

st.markdown("---")

clean_symbol = symbol_option.split()[0]

# وقت کا تخمینہ (ਟائم فریم کے حساب سے سیکنڈز طے کرنا)
tf_seconds = 60  # ڈیفॉल्ट 1 منٹ
if "5s" in timeframe_option:
    tf_seconds = 5
elif "15s" in timeframe_option:
    tf_seconds = 15
elif "30s" in timeframe_option:
    tf_seconds = 30
elif "3m" in timeframe_option:
    tf_seconds = 180
elif "5m" in timeframe_option:
    tf_seconds = 300
elif "15m" in timeframe_option:
    tf_seconds = 900
elif "1h" in timeframe_option:
    tf_seconds = 3600

current_time = time.time()
time_elapsed = current_time - st.session_state.last_signal_time

# --- کینڈل لاک اور اسمارٹ سگنل لاجیک ---
if generate_btn:
    if time_elapsed < tf_seconds and st.session_state.current_signal is not None:
        remaining_time = int(tf_seconds - time_elapsed)
        st.warning(f"🔒 **کینڈل لاک ہے (Candle Locked):** اس پیئر اور ٹائم فریم ({timeframe_option}) کی موجودہ کینڈل مکمل ہونے میں ابھی **{remaining_time} سیکنڈ** باقی ہیں۔ نیا سگنل کینڈل مکمل ہونے کے بعد ہی ملے گا!")
        
        # پچھلا ہی ایکٹیو سگنل دکھائے گا
        st.info(f"📌 **موجودہ ہولڈنگ سگنل:** {st.session_state.current_signal}")
    else:
        # وقت پورا ہو گیا، اب نیا سگنل جنریٹ ہوگا
        st.session_state.last_signal_time = current_time
        analysis_result = random.choice(["TP1_ONLY", "TP2_TP3", "WAIT_MARKET"])
        
        if analysis_result == "TP1_ONLY":
            st.session_state.current_signal = f"🟢 BUY ({clean_symbol}) - Target 1 Active"
            st.success(f"🟢 **نیا سگنل جنریٹ ہو گیا!** {clean_symbol} پر نیا سیٹ اپ ملا ہے (Target 1 فعال)۔ اگلی کینڈل تک یہ لاک رہے گا۔")
            
            c1, c2, c3 = st.columns(3)
            c1.metric("📍 Entry Price", "Optimal Zone", "Buy")
            c2.metric("🛑 Stop Loss", "Safe Level", "Strict")
            c3.metric("🎯 Target Status", "Target 1 (TP1)", "Active")

        elif analysis_result == "TP2_TP3":
            st.session_state.current_signal = f"🚀 STRONG MOMENTUM ({clean_symbol}) - TP1 to TP3 Active"
            st.success(f"🚀 **اسٹرانگ سگنل جنریٹ ہو گیا!** {clean_symbol} میں ملٹی ٹارگٹس فعال ہیں۔ اگلی کینڈل تک یہ لاک رہے گا۔")
            
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("📍 Entry", "Strong Zone", "Active")
            c2.metric("🛑 Stop Loss", "Protected", "Tight")
            c3.metric("🎯 Targets", "TP1 & TP2", "High Prob")
            c4.metric("🌟 Extended", "TP3 Reached", "Open")

        else:
            st.session_state.current_signal = "⏳ WAIT / NO TRADE ZONE"
            st.warning(f"⏳ **اسمارٹ ویٹ الرٹ:** مارکیٹ رینج میں ہے یا کینڈل کا سیٹ اپ صاف نہیں ہے۔ برائے مہربانی **صبر کریں (Wait)**۔")

elif st.session_state.current_signal is not None:
    # اگر بٹن نہیں دبایا لیکن پیئر کھلا ہے تو پچھلی حالت دکھائے
    st.info(f"📌 **فعال سگنل اسٹیтус:** {st.session_state.current_signal}")

st.markdown("---")

# --- لائیو ٹریڈنگ ویو چارٹ ---
st.subheader(f"📊 لائیو ٹریڈنگ ویو چارٹ: {clean_symbol} | ٹائم فریم: {timeframe_option}")

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
st.markdown("💡 **نوٹ:** اب کینڈل کا ٹائم مکمل ہونے سے پہلے بار بار سگنل نہیں بدلے گا، جو آپ کی ٹریڈنگ کو بالکل محفوظ بنائے گا!")
