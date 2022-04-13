# st.file_uploader

`st.file_uploader` displays a file uploader widget [[1](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)].

By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option. For more info on how to set config options, see [[2](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)].

## Demo app

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/dataprofessor/st.file_uploader/)

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
1. [`st.file_uploader`](https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader)
2. [Set configuration options](https://docs.streamlit.io/library/advanced-features/configuration#set-configuration-options)
