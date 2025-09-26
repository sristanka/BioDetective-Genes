import streamlit as st
import level1, level2, level3, level4, level5

# Initialize session state
def init_session_state():
    st.session_state.setdefault("current_level", 1)
    st.session_state.setdefault("score", 0)
    st.session_state.setdefault("hints_used", 0)
    st.session_state.setdefault("level_inputs", {})
    st.session_state.setdefault("level_hints_shown", {})
    st.session_state.setdefault("completed_levels", set())

init_session_state()

# App title and intro
st.title("🧬 BioDetective: Genes 🕵️‍♂️")
st.markdown("Hey Welcome Detective!")
st.markdown("Can you solve all the biotech mysteries and earn your title as an **Explorer**? 🌍")

# Topics by level
level_topics = {
    1: "DNA Base Pairing",
    2: "DNA or RNA?",
    3: "DNA → Protein",
    4: "Cell Organelles",
    5: "Everyday Biotech"
}

# Sidebar dashboard
with st.sidebar:
    st.markdown("Welcome Detective!")
    st.header("Detective Dashboard 📊")
    progress = st.session_state.score / 12
    st.progress(progress)
    st.markdown(f"**Score: {st.session_state.score}/12**")
    st.markdown(f"**Hints Used: {st.session_state.hints_used}**")

    for i in range(1, 6):
        status = "✅" if i in st.session_state.completed_levels else "🔒"
        st.markdown(f"{status} Level {i}: {level_topics[i]}")

    st.markdown("---")
    st.markdown("### 👨‍💻 Created By")
    st.markdown("**Sristanka Adhikary**")

    st.markdown("### 📬 Contact & Connect")
    st.markdown(
        "🔗 [LinkedIn](https://www.linkedin.com/in/sristanka-adhikary) – for professional updates and networking  \n"
        "📷 [Instagram](https://www.instagram.com/btwsris/) – follow for more projects & behind the scenes"
    )

    st.markdown("---")
    if st.button("🔄 Reset Game"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        init_session_state()
        st.rerun()

# Completion screen
def show_completion():
    st.balloons()
    st.markdown("🎉 Congratulations! You are now an Explorer! 🎓")
    st.markdown(f"**Final Score: {st.session_state.score}/12**")
    st.markdown(f"**Total Hints Used (all levels): {st.session_state.hints_used}**")
    st.markdown("See you at Part 2 of BioDetective soon! 👋")
    if st.button("🔄 Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        init_session_state()
        st.rerun()

# Level rendering
levels = [level1, level2, level3, level4, level5]
if st.session_state.current_level > len(levels):
    show_completion()
else:
    levels[st.session_state.current_level - 1].render_level()
