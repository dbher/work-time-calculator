import streamlit as st
import numpy as np
import pandas as pd
import re

def change_string_to_sec(stringTypeTime):
    pattern = "([0-9]+):([0-9]+):([0-9]+)"
    secList = re.search(pattern, stringTypeTime)
    sec = int(secList.group(1)) * 60 * 60 + int(secList.group(2)) * 60 + int(secList.group(3))
    return sec

def make_num_time_df(df):
    timeIndex = ["출근 시간", "퇴근 시간"]
    timeColumns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    numTimeDF = pd.DataFrame(index=timeIndex, columns=timeColumns)
    for count in range (2) :
        numTimeDF["Monday"][count - 1] = change_string_to_sec(df["Monday"][count - 1])
        numTimeDF["Tuesday"][count - 1] = change_string_to_sec(df["Tuesday"][count - 1])
        numTimeDF["Wednesday"][count - 1] = change_string_to_sec(df["Wednesday"][count - 1])
        numTimeDF["Thursday"][count - 1] = change_string_to_sec(df["Thursday"][count - 1])
        numTimeDF["Friday"][count - 1] = change_string_to_sec(df["Friday"][count - 1])

    return numTimeDF

def make_working_time_df(df):
    timeIndex = ["근무 시간"]
    timeColumns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    workingTimeDF = pd.DataFrame(index=timeIndex, columns=timeColumns)

    for count in range (2) :
        workingTimeDF["Monday"][count - 1] = change_string_to_sec(df["Monday"][count - 1])
        workingTimeDF["Tuesday"][count - 1] = change_string_to_sec(df["Tuesday"][count - 1])
        workingTimeDF["Wednesday"][count - 1] = change_string_to_sec(df["Wednesday"][count - 1])
        workingTimeDF["Thursday"][count - 1] = change_string_to_sec(df["Thursday"][count - 1])
        workingTimeDF["Friday"][count - 1] = change_string_to_sec(df["Friday"][count - 1])

    return workingTimeDF

st.set_page_config(page_title="출퇴근 계산기", page_icon="⏲")
st.title("출퇴근 계산기 ⌚️")

st.info("💡 각 요일마다 출퇴근 시간을 입력해주세요")

timeIndex = ["출근 시간", "퇴근 시간"]
timeColumns = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

timeDF = pd.DataFrame(index=timeIndex, columns=timeColumns)

writtenTimeDF = st.data_editor(timeDF, key="initalValue")


if st.button('테스트', key = 'test'):
    st.write(make_num_time_df(writtenTimeDF))
    
    # st.write(writtenTimeDF["Monday"][0])
    
    # st.write(change_string_to_sec(test))
# st.write(timeDF["Monday"][1])
    


st.button("확인")



