import streamlit as st
import pandas as pd
import plotly.express as px


st.title("采煤机大部件温度可视化")

# 文件上传
uploaded_file = st.file_uploader("拖拽文件到这里", type=["csv", "xlsx", "txt"])

if uploaded_file:
    # 确保文件不是 None 后再检查文件名
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.txt'):
        df = pd.read_csv(uploaded_file, delimiter='\t')  # 处理制表符分隔的文本文件
    else:
        df = pd.read_csv(uploaded_file)  # 默认读取 CSV 文件

    # 数据预览
    st.write("### 数据预览")
    st.dataframe(df)

    # 用户选择 X 轴和多列 Y 轴
    st.write("### 选择需要分析的测量数据")
    x_axis = st.selectbox("选择X轴", df.columns, index=0)
    y_axes = st.multiselect("选择需要分析的多个测量数据", df.columns[1:], default=[df.columns[1]])

    # 用户自定义样式
    line_color = st.color_picker("选择线条颜色", value="#0000FF")  # 默认蓝色
    line_dash = st.selectbox("选择线条样式", ["solid", "dash", "dot", "dashdot"])  # Plotly 样式选项

    # 时间列转换为相对分钟数
    try:
        df[x_axis] = pd.to_datetime(df[x_axis])  # 转换为 datetime 格式
        df["相对分钟数"] = (df[x_axis] - df[x_axis].min()).dt.total_seconds() // 60  # 添加相对分钟数
        x_axis = "相对分钟数"  # 使用相对分钟数作为 X 轴
    except Exception as e:
        st.warning("时间列无法转换为 datetime 格式，将按原始数据展示")

    # 使用 Plotly 绘图
    st.write("### 温度趋势图")
    fig = px.line(df, x=x_axis, y=y_axes, title="温度趋势图")
    for i, y_axis in enumerate(y_axes):
        fig.data[i].line.color = line_color  # 设置线条颜色
        fig.data[i].line.dash = line_dash  # 设置线条样式
    fig.update_xaxes(title="相对分钟数", tickmode="linear", dtick=10)  # 设置 X 轴小刻度
    fig.update_yaxes(title="温度值", tickmode="linear", dtick=5)  # 设置 Y 轴小刻度
    st.plotly_chart(fig)

    # 数据统计
    st.write("### 数据统计")
    for y_axis in y_axes:
        st.write(f"{y_axis}: 最大值: {df[y_axis].max()}, 最小值: {df[y_axis].min()}, 平均值: {df[y_axis].mean():.2f}")


