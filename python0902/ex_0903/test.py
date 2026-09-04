import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'first column' : [1, 2, 3, 4],
    'second column' : [10, 20, 30, 40]
})
#df

st.write("ㅎㅇ")
st.write(df)

datframe = np.random.randn(10, 20)
st.dataframe(datframe)

datframestyle = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20))
)
st.dataframe(datframestyle.style.highlight_max(axis=0))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)

