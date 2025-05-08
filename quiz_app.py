import streamlit as st
import random

# 제목 설정
st.title("윤재를 위해 이모가 만든 재미있는 퀴즈!")

# 퀴즈 문제와 답 설정
quiz_data = [
    {"question": "세상에서 가장 잘생긴 가위는?", "answer": "핸썸가위", "hint": "ㅎㅆㄱㄱㅇ"},
    {"question": "세상에서 가장 빠른 떡은?", "answer": "헐레벌떡", "hint": "ㅎㄹㅂㄸ"},
    {"question": "미소가 가장 예쁜 사람은?", "answer": "광대", "hint": "ㄱㄷㄷ"},
    {"question": "오리가 옆으로 가면?", "answer": "옆으로가오리", "hint": "ㅇㅇㄹㄱㅇㄹ"},
    {"question": "우유가 옆으로 넘어지면?", "answer": "아야", "hint": "ㅇㅇㅇ"},
    {"question": "고기 먹을 때 심심하면?", "answer": "소심하다", "hint": "ㅅㅅㅎㄷ"},
    {"question": "날마다 새로운 옷을 입는 것은?", "answer": "달력", "hint": "ㄷㄹ"},
    {"question": "세상에서 가장 뜨거운 바다는?", "answer": "열바다", "hint": "ㅇㅂㄷ"},
    {"question": "칼이 정색하면?", "answer": "검정색", "hint": "ㄱㅈㅅ"}
    {"question": "세상에서 제일 윤재를 사랑하는 사람 두명은?", "answer": "아빠엄마", "hint": "ㅇㅃㅇㅁ"}
]

# 세션 상태 초기화
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False

# 현재 문제 표시
if st.session_state.current_question < len(quiz_data):
    current_quiz = quiz_data[st.session_state.current_question]
    
    # 점수 표시
    st.write(f"현재 점수: {st.session_state.score} / {len(quiz_data)}")
    st.write(f"문제 {st.session_state.current_question + 1}번:")
    st.write(current_quiz["question"])
    
    # 힌트 버튼
    if st.button("힌트 보기"):
        st.session_state.show_hint = True
    
    if st.session_state.show_hint:
        st.write(f"힌트: {current_quiz['hint']}")
    
    # 답 입력
    user_answer = st.text_input("답을 입력하세요:", key=f"answer_{st.session_state.current_question}")
    
    if st.button("정답 확인"):
        if user_answer == current_quiz["answer"]:
            st.success("윤재야! 정답이야! 엄청난걸 껄껄껄")
            st.session_state.score += 1
        else:
            st.error("윤재야! 이 문제는 모르겠지? 이모한테 물어봐 ㅋㅋ")
            st.write(f"정답은 '{current_quiz['answer']}'였어!")
        
        st.session_state.current_question += 1
        st.session_state.show_hint = False
        st.experimental_rerun()
# 모든 문제를 다 풀었을 때
else:
    st.success(f"퀴즈 끝! 최종 점수: {st.session_state.score} / {len(quiz_data)}")
    if st.button("다시 시작"):
        st.session_state.score = 0
        st.session_state.current_question = 0
        st.session_state.show_hint = False
        st.experimental_rerun()
