import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image #画像を表示させるライブラリ
from io import BytesIO #pngを表示させるためのライブラリ
import time

st.title("Streamlit 超入門")

#プログレスバーの表示
st.write("プログレスバーの表示")
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i+1)
    time.sleep(0.01)

"Done!"


#2カラムレイアウトにする
left_column, right_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラムです")

#expander
expander1 = st.expander("問い合わせ1")
expander1.write("問い合わせ1回答")
expander2 = st.expander("問い合わせ2")
expander2.write("問い合わせ2回答")
expander3 = st.expander("問い合わせ3")
expander3.write("問い合わせ3回答")

##select
option = st.sidebar.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11))
)

"あなたの好きな数字は、", option ,"です"

##テキスト入力
text = st.sidebar.text_input("あなたの趣味を教えてください。")
"あなたの趣味:", text

##
condition = st.sidebar.slider("あなたの今の調子は?", 0, 100, 50)
"コンディション", condition


##画像表示jpg
if st.checkbox("Monk:jpg"):
    img = Image.open("pray-g942ae3e81_1920.jpg")
    st.image(img, caption="monk boy", use_column_width = True)

##画像表示png (参照:https://qiita.com/wasnot/items/be649f289073fb96513b)
if st.checkbox("irasutoya:png"):
    filename = "computer_tokui_boy.png"
    # 画像ファイルパスから読み込み
    img = Image.open(filename)
    # バイナリから読み込み(python3なのでbinaryモードで読み込み)
    with open(filename, 'rb') as f:
        binary = f.read()
    img = Image.open(BytesIO(binary))
    # numpy配列の取得
    img_array = np.asarray(img)
    # 色の変換も簡単ですが、できる色が制限されます。
    rgb = img.convert('RGB')
    st.image(rgb, caption="computer_tokui_boy", use_column_width = True)

# ##自分のファイルから動画表示
# if st.checkbox("movie:mp4"):
#     video_file = open('Star - 6962.mp4', 'rb')
#     video_bytes = video_file.read()
#     st.video(video_bytes, start_time = 2)

##URLから動画表示
if st.checkbox("movie:url"):
    st.video("https://www.youtube.com/watch?v=K5_ktUB62G0")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1,2,3,4],
    "2列目": [10,20,30,40]
})

#writeとdataframeどちらでもいい
#ソートができる
#dataframeの方がwidthやheight,highlightなど指定できる
#tableはソートできない
#dataframe():動的(dynamic)
#table():静的(static)
"""
```python
st.write(df)
"""
if st.checkbox("write"):
    st.write(df)

"""
```python
st.dataframe(df, width=100, height=100)

"""
if st.checkbox("dataframe"):
    st.dataframe(df, width=100, height=100)
"""
```python
st.table(df.style.highlight_max(color='green'))

"""
if st.checkbox("table"):
    st.table(df.style.highlight_max(color='green'))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd

```
"""

#line-chart
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a", "b", "c"]
)

"""
### 折線グラフ:line_chart()
"""
if st.checkbox("折線グラフ"):
    st.line_chart(df)

"""
### 面グラフ:area_chart()
"""
if st.checkbox("面グラフ"):
    st.area_chart(df)

"""
### 棒グラフ:bar_chart()
"""
if st.checkbox("棒グラフ"):
    st.bar_chart(df)

#緯度経度をマッピング

"""
### 緯度経度からマッピング

```python
st.map(df)
```
"""
df = pd.DataFrame(
        np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
        columns=["lat", "lon"]
    )

if st.checkbox("mapping"):
    st.map(df)
