import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="출퇴근 계산기", page_icon="⏲")
st.title("출퇴근 계산기 ⌚️")

st.info("💡 각 요일마다 출퇴근 시간을 입력해주세요")


timeIndex = ["출근 시간", "퇴근 시간"]
timeColumns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

timeDF = pd.DataFrame(index=timeIndex, columns=timeColumns)

writtenTimeDF = st.data_editor(timeDF, key="my_data_editor")

