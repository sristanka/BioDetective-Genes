# level2.py
import streamlit as st
import utils

def render_level():
    st.header("Level 2: DNA vs RNA Identifier 🧬")
    st.markdown("""
    **Concept:** 
    DNA has bases **A, T, G, C**.  
    RNA has bases **A, U, G, C**.  

    Your task: Identify whether the given strand is **DNA** or **RNA**.
    """)

    # Generate 2 random strands (DNA or RNA)
    if 'level2_strands' not in st.session_state:
        st.session_state.level2_strands = utils.generate_dna_or_rna(length=6, count=2)

    level_cleared = True
    options = ["Select...", "DNA", "RNA"]  # Default "Select..." prevents preselection

    for idx, strand_info in enumerate(st.session_state.level2_strands, start=1):
        st.markdown(f"**Question {idx}: Identify the strand type**")
        st.markdown(f"**Strand:** {strand_info['sequence']}")

        key = f"level2_input_{idx}"
        if key not in st.session_state:
            st.session_state[key] = options[0]  # Start with "Select..."

        user_choice = st.selectbox(
            f"Choose the type for Q{idx}:",
            options,
            index=options.index(st.session_state[key]),
            key=key
        )

        st.session_state.level_inputs[f"level2_{idx}"] = user_choice

        # Hint button
        hint_key = f"level2_hint_{idx}"
        if hint_key not in st.session_state.level_hints_shown:
            if st.button(f"💡 Show Hint Q{idx}"):
                st.session_state.level_hints_shown[hint_key] = True
                st.session_state.hints_used += 1
                st.rerun()
        if hint_key in st.session_state.level_hints_shown:
            st.info("Hint: DNA has T (Thymine), RNA has U (Uracil). Look carefully!")

        # Show answer
        if st.button(f"📝 Show Answer Q{idx}"):
            st.markdown(f"**Correct Answer:** {strand_info['type']}")

        # Check correctness
        if user_choice == strand_info['type']:
            st.success(f"✅ Correct! This is {strand_info['type']}")
        elif user_choice != options[0]:
            st.error(f"❌ Incorrect. Correct answer: {strand_info['type']}")
            level_cleared = False
        else:
            level_cleared = False  # "Select..." not considered correct

    # Next level button
    if level_cleared:
        st.success("🎉 Level 2 cleared!")
        if "level2_done" not in st.session_state:
            st.session_state.score += len(st.session_state.level2_strands)
            st.session_state.level2_done = True
        if st.button("➡️ Next Level"):
            st.session_state.completed_levels.add(2)
            st.session_state.current_level = 3
            st.rerun()
