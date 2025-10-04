import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# --- 網頁配置 ---
st.set_page_config(
    page_title="互動式線性迴歸產生器",
    page_icon="📈",
    layout="wide"
)

# --- 標題與說明 ---
st.title("📈 互動式線性迴歸產生器")
st.write("本應用程式讓您透過調整參數來生成資料，並即時觀察簡單線性迴歸模型的分析結果與圖表。")

# --- 側邊欄：使用者輸入 ---
st.sidebar.header("資料生成參數")

def get_user_inputs():
    """獲取使用者在側邊欄輸入的參數"""
    a = st.sidebar.slider("真實斜率 (a)", min_value=-10.0, max_value=10.0, value=2.5, step=0.1)
    b = st.sidebar.slider("真實截距 (b)", min_value=-10.0, max_value=10.0, value=5.0, step=0.1)
    noise = st.sidebar.slider("雜訊標準差 (noise)", min_value=0.0, max_value=20.0, value=2.0, step=0.1)
    n_points = st.sidebar.slider("資料點數量", min_value=10, max_value=1000, value=100, step=10)
    return a, b, noise, n_points

a_true, b_true, noise_std, n_points = get_user_inputs()

# --- 資料生成 ---
@st.cache_data
def generate_data(a, b, noise, n):
    """根據參數生成資料集"""
    x = np.linspace(-10, 10, n)
    random_noise = np.random.normal(0, noise, n)
    y = a * x + b + random_noise
    df = pd.DataFrame({'x': x, 'y': y})
    return df, x, y

df, x, y = generate_data(a_true, b_true, noise_std, n_points)

# --- 模型訓練 ---
# 將特徵 x 轉換為 scikit-learn 需要的 2D 陣列
X = x.reshape(-1, 1)

# 建立並訓練線性迴歸模型
model = LinearRegression()
model.fit(X, y)

# 獲取模型預測結果
a_pred = model.coef_[0]
b_pred = model.intercept_
r2_score = model.score(X, y)

# --- 結果展示 ---
st.header("迴歸模型結果")
st.markdown("---")

col1, col2, col3 = st.columns(3)
col1.metric("預測斜率 (Coefficient)", f"{a_pred:.4f}", f"真實值: {a_true:.2f}")
col2.metric("預測截距 (Intercept)", f"{b_pred:.4f}", f"真實值: {b_true:.2f}")
col3.metric("R² 分數 (R-squared)", f"{r2_score:.4f}")

# --- 圖表繪製 ---
st.header("資料與迴歸線圖表")
st.markdown("---")

fig, ax = plt.subplots(figsize=(10, 6))

# 繪製生成的資料點
ax.scatter(x, y, alpha=0.7, label="生成的資料點 (y = ax + b + noise)")

# 繪製真實的關係線
y_true_line = a_true * x + b_true
ax.plot(x, y_true_line, color='green', linestyle='--', linewidth=2, label=f"真實線 (y={a_true:.2f}x+{b_true:.2f})")

# 繪製模型預測的迴歸線
y_pred_line = model.predict(X)
ax.plot(x, y_pred_line, color='red', linewidth=3, label=f"迴歸線 (y={a_pred:.2f}x+{b_pred:.2f})")

ax.set_title("資料分佈與線性迴歸結果", fontsize=16)
ax.set_xlabel("X", fontsize=12)
ax.set_ylabel("Y", fontsize=12)
ax.legend()
ax.grid(True)
plt.style.use('ggplot')

st.pyplot(fig)

# --- 顯示原始資料 ---
with st.expander("點擊展開/收合以查看生成的原始資料"):
    st.dataframe(df)
