# level1.py
import streamlit as st
import utils

def render_level():
    st.header("Level 1: DNA Base-Pair Matching 🧬")
    st.markdown("""
Concept:  
DNA consists of four nitrogenous bases: Adenine (A), Thymine (T), Cytosine (C), and Guanine (G).  

In the double-helix structure, these bases pair specifically:  
- Adenine pairs with Thymine (A-T)  
- Cytosine pairs with Guanine (C-G)  

These complementary strands are held together by hydrogen bonds.  

Therefore, DNA is like a ladder with letters A, T, G, C. Each letter has a partner:  
**A ↔ T, G ↔ C**  

Let's build complementary strands!
""")

    # Generates two DNA sequences if not already
    if 'level1_dna' not in st.session_state:
        st.session_state.level1_dna = utils.generate_dna(length=5, count=2)

    # Tracks level completion
    level_cleared = True

    for idx, original_strand in enumerate(st.session_state.level1_dna, start=1):
        correct_complement = utils.get_complement(original_strand)
        st.markdown(f"**Question {idx}: Fill in the complementary strand for:** {original_strand}")

        default_value = st.session_state.level_inputs.get(f"level1_{idx}", "")
        user_input = st.text_input(f"Your answer for question {idx}:", key=f"level1_input_{idx}", value=default_value).upper().strip()

        hint_shown = f"level1_hint_{idx}" in st.session_state.level_hints_shown
        if not hint_shown:
            if st.button(f"💡 Show Hint Q{idx}"):
                st.session_state.level_hints_shown[f"level1_hint_{idx}"] = True
                st.session_state.hints_used += 1
                st.rerun()
        if hint_shown:
            st.markdown("**Hint:** Check each base: A→T, T→A, G→C, C→G. Write them one by one!")

        if st.button(f"📝 Show Answer Q{idx}"):
            st.markdown(f"**Correct Complement:** {correct_complement}")
            st.markdown(f"**Explanation:** Each base pairs specifically: A with T, G with C.")

        if st.button(f"✅ Check Answer Q{idx}"):
            st.session_state.level_inputs[f"level1_{idx}"] = user_input
            if user_input == correct_complement:
                st.success(f"🎉 Correct! Question {idx} done!")
            else:
                st.error(f"❌ Incorrect. Correct answer: {correct_complement}")
                level_cleared = False

        # If any question not correct yet, mark level as not cleared
        if st.session_state.level_inputs.get(f"level1_{idx}", "") != correct_complement:
            level_cleared = False

    # Show next button after all correct
    if level_cleared:
        st.success("🎉 Hurry!! Level 1 cleared")
        if "level1_done" not in st.session_state:
            st.session_state.score += len(st.session_state.level1_dna)
            st.session_state.level1_done = True
        if st.button("➡️ Next Level"):
            st.session_state.completed_levels.add(1)
            st.session_state.current_level = 2
            st.rerun()
