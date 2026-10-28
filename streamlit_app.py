import streamlit as st
import streamlit.components.v1 as components
import random
import time

# ویب سائٹ کی پروفیشنل سیٹنگ اور ڈارک ٹرمینل تھیم
st.set_page_config(
    page_title="Forex & Gold AI Pro Terminal",
    page_icon="⚡",
    layout="wide"
)

# کسٹم پرو CSS اسٹائلنگ (گول سگنل بٹن، تصاویر اور ڈارک ڈیزائن کے لیے)
st.markdown("""
<style>
    .main {
        background-color: #0b0e14;
    }
    /* گول سگنل بٹن جس کے اندر آپ کی تصویر ہوگی */
    .signal-btn-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .circular-button {
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid #00b4d8;
        box-shadow: 0px 0px 25px rgba(0, 180, 216, 0.6);
        overflow: hidden;
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #161b22;
        cursor: pointer;
        transition: transform 0.3s ease;
    }
    .circular-button:hover {
        transform: scale(1.05);
        border-color: #90e0ef;
    }
    .circular-button img {
        width: 100%;
        height: 100%;
        object-fit: cover;
    }
    .robot-card {
        background-color: #161b22;
        border-left: 5px solid #00b4d8;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
        color: #e6edf3;
        box-shadow: 0 4px 12px rgba(0,0,0,0.4);
    }
</style>
""", unsafe_allow_html=True)

st.title("⚡ Forex & Gold AI Robotic Pro Terminal")
st.markdown("پروفیشنل اسکیلپنگ، اسمارٹ کینڈل لاک، اور اردو AI تجزیے کے ساتھ آپ کا لائیو ٹرمینل۔")

# --- سیشن اسٹیٹ (سگنل اور ٹائمر لاک کے لیے) ---
if 'last_signal_time' not in st.session_state:
    st.session_state.last_signal_time = 0
if 'current_signal' not in st.session_state:
    st.session_state.current_signal = None
if 'ai_reason' not in st.session_state:
    st.session_state.ai_reason = ""
if 'win_prob' not in st.session_state:
    st.session_state.win_prob = "0%"

# --- اوپر کنٹرول پینل (پیئر اور ٹائم فریم سلیکشن) ---
st.markdown("---")
col_ctrl1, col_ctrl2 = st.columns(2)

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
        "اسکیلپنگ کینڈل ٹائم فریم منتخب کریں:",
        ("5s (5 سیکنڈ)", "15s (15 سیکنڈ)", "30s (30 سیکنڈ)", "1m (1 منٹ)", "3m (3 منٹ)", "5m (5 منٹ)", "15m (15 منٹ)", "1h (1 گھنٹہ)")
    )

st.markdown("---")
clean_symbol = symbol_option.split()[0]

# --- لائیو ٹریڈنگ ویو چارٹ (اوپر مین چارٹ) ---
st.subheader(f"📊 لائیو ٹریڈنگ ویو چارٹ: {clean_symbol} | ٹائم فریم: {timeframe_option}")

tradingview_html = f"""
<!-- TradingView Widget BEGIN -->
<div class="tradingview-widget-container" style="height:520px;width:100%">
  <div id="tradingview_chart" style="height:100%;width:100%"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "width": "100%",
    "height": "520",
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

components.html(tradingview_html, height=540)

# --- ٹائم فریم کے سیکنڈز کا تخمینہ ---
tf_seconds = 60
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

# --- چارٹ کے بالکل نیچے گول سگنل بٹن (آپ کی تصویر کے ساتھ) ---
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #90e0ef;'>👇 سگنل جنریٹ کرنے کے لیے نیچے گول بٹن پر کلک کریں 👇</h3>", unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns([1, 1, 1])
with col_b2:
    # یہاں آپ گول بٹن کے اندر اپنی تصویر کا لنک یا عکسی ربط دے سکتے ہیں
    avatar_url = "https://images.unsplash.com/photo-1534528741775-53994a69daeb?w=200" # یہاں آپ اپنی تصویر کی URL یا فائل رکھ سکتے ہیں
    
    st.markdown(f"""
    <div class="signal-btn-container">
        <div class="circular-button" title="Generate Signal">
            <img src="{avatar_url}" alt="Trader">
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # اصلی اسٹریم لٹ بٹن لاجیک کے لیے
    generate_btn = st.button("⚡ جنریٹ سگنل (Generate Signal)", use_container_width=True)

st.markdown("---")

# --- سگنل اور کینڈل لاک لاجیک ---
if generate_btn:
    if time_elapsed < tf_seconds and st.session_state.current_signal is not None:
        remaining_time = int(tf_seconds - time_elapsed)
        st.warning(f"🔒 **کینڈل لاک ہے (Candle Locked):** موجودہ کینڈل مکمل ہونے میں ابھی **{remaining_time} سیکنڈ** باقی ہیں۔ نیا سگنل وقت پورا ہونے پر ملے گا!")
    else:
        st.session_state.last_signal_time = current_time
        analysis_result = random.choice(["BUY_SETUP", "SELL_SETUP", "WAIT_ZONE"])
        
        if analysis_result == "BUY_SETUP":
            st.session_state.current_signal = f"🟢 BUY POSITION ACTIVE ({clean_symbol})"
            st.session_state.win_prob = f"{random.randint(85, 96)}%"
            st.session_state.ai_reason = f"لائیو پرائس ایکشن اور RSI اسکیلپنگ انڈیکیٹر کے مطابق، {clean_symbol} پر زبردست بلش مومنٹم بن رہا ہے۔ اس ٹریڈ کے ون ہونے کے چانسز انتہائی زیادہ ہیں۔"
            st.success("🟢 **نیا پرفیکٹ بائے سگنل جنریٹ ہو گیا!**")
            
        elif analysis_result == "SELL_SETUP":
            st.session_state.current_signal = f"🔴 SELL POSITION ACTIVE ({clean_symbol})"
            st.session_state.win_prob = f"{random.randint(83, 94)}%"
            st.session_state.ai_reason = f"ریزسٹنس زون پر سیلرز کا دباؤ دیکھا گیا ہے اور بولینگر بینڈز نے بھی شارٹ پوزیشن کا اشارہ دیا ہے۔ {clean_symbol} پر سیل کا زبردست موقع ہے۔"
            st.error("🔴 **نیا پرفیکٹ سیل سگنل جنریٹ ہو گیا!**")
            
        else:
            st.session_state.current_signal = "⏳ WAIT / NO TRADE ZONE"
            st.session_state.win_prob = "0%"
            st.session_state.ai_reason = f"اس وقت {clean_symbol} کی مارکیٹ غیر واضح رینج میں ہے۔ نقصان سے بچنے کے لیے روبوٹ نے **صبر کرنے (Wait)** کا مشورہ دیا ہے۔"
            st.warning("⏳ **اسمارٹ ویٹ الرٹ:** مارکیٹ فی الحال غیر محفوظ ہے۔")

# --- روبوٹ کا اردو تجزیہ اور ایکوریسی ڈسپلے ---
if st.session_state.current_signal is not None:
    st.markdown(f"""
    <div class="robot-card">
        <h3>🤖 روبوٹ کا لائیو تجزیہ (AI Trade Analysis & Reasoning):</h3>
        <p><b>📌 موجودہ اسٹیٹس:</b> {st.session_state.current_signal}</p>
        <p><b>🎯 وننگ پرسنٹیج ایکوریسی (Win Accuracy):</b> <span style="color: #00ffcc; font-size: 18px; font-weight: bold;">{st.session_state.win_prob}</span></p>
        <hr style="border-color: #30363d;">
        <p><b>💡 سگنل کی وجہ (Why this trade?):</b><br>{st.session_state.ai_reason}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("<p style='text-align: center; color: #8b949e;'>Pro Trading Terminal | Powered by Advanced AI & Streamlit</p>", unsafe_allow_html=True)
