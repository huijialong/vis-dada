import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 页面标题
st.title("采煤机大部件温度可视化")
st.write("将您的文件拖拽到这里，即可生成趋势图！")

# 上传文件
uploaded_file = st.file_uploader("拖拽文件到这里", type=["csv"])

if uploaded_file:
    # 读取CSV文件
    df = pd.read_csv(uploaded_file)
    st.write("### 数据预览")
    st.dataframe(df)

    # 选择 X 和 Y 轴
    st.write("### 选择需要分析的测量数据")
    x_axis = st.selectbox("选择X轴", df.columns, index=0)
    y_axis = st.selectbox("选择Y轴", df.columns, index=1)

    # 绘制图表
    st.write("### 自动生成的图表")
    fig, ax = plt.subplots()
    ax.plot(df[x_axis], df[y_axis], label=f"{y_axis} 随 {x_axis} 变化")
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.legend()
    ax.grid()
    st.pyplot(fig)

    st.success("Done!")

