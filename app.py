import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 页面标题
st.title("CSV文件自动可视化工具")
st.write("将您的CSV文件拖拽到这里，即可自动生成图表！")

# 上传文件
uploaded_file = st.file_uploader("拖拽CSV文件到这里", type=["csv"])

if uploaded_file:
    # 读取CSV文件
    df = pd.read_csv(uploaded_file)
    st.write("### 数据预览")
    st.dataframe(df)

    # 选择 X 和 Y 轴
    st.write("### 选择要可视化的列")
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

    st.success("图表生成完毕！")

# 说明
st.info("提示：如果数据格式相似，您可以反复上传不同的文件进行可视化。")
