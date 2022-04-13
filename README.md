# st.template

`st.template` allows writing text and arguments to the Streamlit app.

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.template/)

## Code
Here's how to use `st.write`:
```python
import streamlit as st
import pandas as pd

st.header('st.file_uploader')

st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

## Line-by-line explanation
The very first thing to do when creating a Streamlit app is to start by importing the `streamlit` library as `st` and other prerequisite library like so:
```python
import streamlit as st
import pandas as pd
```

## Further reading
- [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
