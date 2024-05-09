# import altair as alt
# import numpy as np
# import pandas as pd
# import streamlit as st

# """
# # Welcome to Streamlit!

# Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
# If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
# forums](https://discuss.streamlit.io).

# In the meantime, below is an example of what you can do with just a few lines of code:
# """

# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)

# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices

# x = radius * np.cos(theta)
# y = radius * np.sin(theta)

# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })

# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))


import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="小明简历")

NAME = "小明"
# profile_pic = Path.cwd() / "profile-pic.png"
# profile_pic = Image.open(profile_pic)

col1, col2 = st.columns(2,gap="small")

# with col1:
#     st.image(profile_pic,width=230)
    
with col2:
    st.title(NAME)
    st.write("邮件：xiaoming@126.com")
    st.write("手机号：12345678910（微信同）")
    st.write("出生年月：2000年1月1号")
    st.write("政治面貌：群众")
    
st.write('\n')
st.subheader("教育背景")
st.write(
    """
- 2019年9月--2023年6月 D大学 D专业 博士
- 2016年9月--2019年6月 B大学 B专业 硕士
- 2012年9月--2016年6月 A大学 A专业 学士
"""
)

st.write('\n')
st.subheader("科研经历")
st.write(
    """
- AAA
"""
)

st.write('\n')
st.subheader("发表论文")
st.write(
    """
- 论文A
- 论文B
- 论文C
"""
)

st.write('\n')
st.subheader("获奖情况")
st.write(
    """
- 国家奖学金
- 最佳墙报
"""
)

st.write('\n')
st.subheader("科研技能")
st.write(
    """
- 编程（R/python/linux）
- 组学数据处理（基因组学/转录组学/群体基因组学）
- 组学数据处理流程搭建（snakemake）
- 网页搭建（streamlit/gradio）
"""
)

st.write('\n')
st.subheader("兴趣爱好")
st.write(
    """
- 篮球/网球
""")
