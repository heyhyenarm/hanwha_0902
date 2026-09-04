import streamlit as st

if "purpose" not in st.session_state:
    st.session_state.purpose = None

PURPOSES = [None, "포트폴리오", "경력기술서", "관리자 모드"]

def login():
    st.header("개발자 남헤림 페이지")
    purpose = st.selectbox("Choose your purpose", PURPOSES)

    if st.button("Go"):
        st.session_state.purpose = purpose
        st.rerun()

def logout():
    st.session_state.purpose = None
    st.rerun()

purpose = st.session_state.purpose

logout_page = st.Page(logout, title="나가기", icon="🔙")
settings = st.Page("settings.py", title="관리자 모드", icon="👽")

# 포트폴리오 페이지
portfolio_1 = st.Page(
    "portfolio/portfolio_1.py",
    title="Portfolio 1",
    icon="📕",
    default=(purpose == "포트폴리오"),
)
portfolio_2 = st.Page(
    "portfolio/portfolio_2.py", 
    title="Portfolio 2", 
    icon="📗"
)

# 경력기술서 페이지
resume_1 = st.Page(
    "resume/resume_1.py",
    title="Resume 1",
    icon="🏢",
    default=(purpose == "경력기술서"),
)

# 관리자 모드 페이지
admin_1 = st.Page(
    "admin/admin_1.py",
    title="Admin 1",
    icon="🛸",
    default=(purpose == "관리자 모드"),
)
admin_2 = st.Page(
    "admin/admin_2.py",
    title="Admin 2",
    icon="⚙️"
)

account_pages = [logout_page, settings]
portfolio_pages = [portfolio_1, portfolio_2]
resume_pages = [resume_1]
admin_pages = [admin_1, admin_2]

st.title("개발자 남혜림 페이지")
st.logo("images/logo.png")

page_dict = {}
if st.session_state.purpose in ["포트폴리오", "관리자 모드"]:
    page_dict["포트폴리오"] = portfolio_pages
if st.session_state.purpose in ["경력기술서", "관리자 모드"]:
    page_dict["경력기술서"] = resume_pages
if st.session_state.purpose in ["관리자 모드"]:
    page_dict["관리자 모드"] = admin_pages

if len(page_dict) > 0:
    pg = st.navigation({"Account": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()
