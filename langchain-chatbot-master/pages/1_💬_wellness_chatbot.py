import utils
import streamlit as st
import sys

sys.path.append('C:\\sqlite\\mysql\\code\\AI\\FINAL_project\\dialogLM\\dialogLM\\service')
from Demonstration.model.load_electra import DialogElectra 
from Demonstration.model.load_kogpt2 import answer_generator
from streaming import StreamHandler

# DialogElectra 모델 로드

@st.cache_data(hash_funcs={DialogElectra: lambda _: None, answer_generator: lambda _: None}, show_spinner=False)
def load_models():
    dialog_electra = DialogElectra()
    kogpt2_model = answer_generator()
    return dialog_electra, kogpt2_model

# Streamlit 응용 프로그램 설정
st.set_page_config(page_title="Chatbot", page_icon="💬")
st.header('기본 챗봇')
st.write('사용자가 LLM과 상호 작용할 수 있게 합니다.')
st.write('[![소스 코드 보기](https://img.shields.io/badge/소스_코드_보기-gray?logo=github)](https://github.com/shashankdeshpande/langchain-chatbot/blob/master/pages/1_%F0%9F%92%AC_basic_chatbot.py)')

def display_msg(msg, role):
    if role == 'assistant':
        style = "message-container assistant"
        icon = ""
        color = "lightblue"
        font = "Courier New"
    else:
        style = "message-container user"
        icon = ""
        color = "lightgreen"
        font = "Helvetica"

    st.markdown(
        f"<div class='{style}' style='background-color:{color}; font-family:{font};'>\
        {icon}<b>{role.capitalize()}:</b> {msg}</div>",
        unsafe_allow_html=True
    )

@utils.enable_chat_history
def main():
    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # 모델 로드
    dialog_electra, kogpt2 = load_models()

    user_query = st.text_input("당신의 질문:", placeholder="무엇이든 물어봐주세요!", key="user_input")

    # 사용자 입력 상자 바로 아래에 있는 상자 없애기
    st.markdown(
        """
        <style>
        .css-1c7y2kd.e1d0834u4 {
            display: none !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    if user_query:
        with st.spinner("처리 중..."):
            utils.display_msg(user_query, 'user')
            st_cb = StreamHandler(st.empty())  # StreamHandler에 사용할 엘리먼트를 명시적으로 지정
            answer = kogpt2.get_answer(user_query)
            st.session_state.messages.insert(0, {"role": "assistant", "content": answer})

        # 메시지를 역순으로 출력합니다.
        for message in reversed(st.session_state.messages):
            display_msg(message['content'], message['role'])

if __name__ == "__main__":
    main()
