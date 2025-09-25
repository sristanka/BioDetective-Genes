import streamlit as st

def render_level():
    st.header("Level 4: Cell Organelles 🦠")
    st.markdown(
        "**Concept:** A cell is like a bustling city, where different organelles handle different jobs. "
        "Some control information, some generate energy, and others build essential materials. "
        "Can you match the organelles to their correct roles?"
    )

    # Functions and correct organelles
    functions = ["Stores DNA", "Produces energy", "Makes proteins"]
    correct_map = {"Stores DNA": "Nucleus", "Produces energy": "Mitochondria", "Makes proteins": "Ribosomes"}

    # Distractor options
    organelles = ["Nucleus", "Mitochondria", "Ribosomes"]
    distractors = ["Golgi Apparatus", "Lysosome", "Chloroplast"]
    all_options = ["Choose the correct option"] + organelles + distractors

    # Store user selections
    user_matches = {}
    for func in functions:
        key = f"level4_{func.replace(' ','_').lower()}"
        if key not in st.session_state:
            st.session_state[key] = all_options[0]
        selected = st.selectbox(
            f"{func}:",
            all_options,
            index=all_options.index(st.session_state[key]),
            key=key
        )
        user_matches[func] = selected

    st.session_state.level_inputs[4] = user_matches

    # Hints
    hints = {
        "Stores DNA": "This organelle is the control center, holding all the genetic instructions.",
        "Produces energy": "Known as the powerhouse of the cell!",
        "Makes proteins": "Tiny factories inside the cell that synthesize proteins."
    }

    hint_shown = "level4_hint" in st.session_state.level_hints_shown
    if not hint_shown:
        if st.button("💡 Show Hint"):
            st.session_state.level_hints_shown["level4_hint"] = True
            st.session_state.hints_used += 1
            st.rerun()
    if hint_shown:
        st.markdown("**Hints:**")
        for func in functions:
            st.markdown(f"- **{func}:** {hints[func]}")

    # Show answer
    if st.button("📝 Show Answer"):
        for func in functions:
            st.markdown(f"**{func}: {correct_map[func]}** ✅")
            st.markdown("Explanation: This organelle performs the function; others do not.")

    # Check completion
    level_cleared = all(user_matches[f] == correct_map[f] for f in functions)
    if level_cleared:
        st.success("🎉 Hurray!! Level 4 cleared")
        if "level4_done" not in st.session_state:
            st.session_state.score += len(functions)
            st.session_state.level4_done = True
        if st.button("➡️ Next Level"):
            st.session_state.completed_levels.add(4)
            st.session_state.current_level = 5
            st.rerun()
