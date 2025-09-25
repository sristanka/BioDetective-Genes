# level5.py
import streamlit as st

def render_level():
    st.header("Level 5: Everyday Biotech 🌍")
    st.markdown("**Concept:** Biotech is all around us! Match items to their processes.")

    # Items and options
    items = ["Yogurt", "Insulin", "Bt Cotton"]
    processes = [
        "Fermentation by microbes",
        "Human insulin production via bacteria",
        "Crop improved for pest resistance"
    ]
    distractors = [
        "Used in brewing beer",
        "Vitamin supplement",
        "Pesticide sprayed crop"
    ]
    all_options = ["Choose the correct option"] + processes + distractors

    correct_map = dict(zip(items, processes))

    # Store user selections
    user_matches = {}
    for item in items:
        key = f"level5_{item.lower().replace(' ','_')}"
        if key not in st.session_state:
            st.session_state[key] = all_options[0]
        selected = st.selectbox(
            f"{item}:",
            all_options,
            index=all_options.index(st.session_state[key]),
            key=key
        )
        user_matches[item] = selected

    # Save inputs in session state
    st.session_state.level_inputs[5] = user_matches

    # Hints
    hints = {
        "Yogurt": "This process involves bacteria and usually makes your breakfast creamy!",
        "Insulin": "Humans need it to control blood sugar, and bacteria help produce it.",
        "Bt Cotton": "This crop has a natural shield against pests thanks to genetic tweaks."
    }

    hint_shown = "level5_hint" in st.session_state.level_hints_shown
    if not hint_shown:
        if st.button("💡 Show Hint"):
            st.session_state.level_hints_shown["level5_hint"] = True
            st.session_state.hints_used += 1
            st.rerun()
    if hint_shown:
        st.markdown("**Hints:**")
        for item in items:
            st.markdown(f"- **{item}:** {hints[item]}")

    # Show answer
    if st.button("📝 Show Answer"):
        for item in items:
            st.markdown(f"**{item}: {correct_map[item]}** ✅")
            st.markdown("Explanation: This is the correct process; other options are incorrect.")

    # Check completion
    level_cleared = all(user_matches[i] == correct_map[i] for i in items)
    if level_cleared:
        st.success("🎉 Hurray!! Level 5 cleared")
        if "level5_done" not in st.session_state:
            st.session_state.score += len(items)
            st.session_state.level5_done = True
        if st.button("➡️ Finish Game"):
            st.session_state.completed_levels.add(5)
            st.session_state.current_level = 6
            st.rerun()
