# level2.py
import streamlit as st
import utils

def render_level():
    st.header("Level 2: Mutation Spotter 🔍")
    st.markdown("**Concept:**  A gene mutation is a permanent change in the DNA sequence of a gene. Mutations can occur naturally or be caused by environmental factors. They can affect how proteins are made, sometimes causing diseases or creating new traits.")
    st.markdown("So mutations are like tiny typos in DNA.")
    st.markdown("""
                **DNA is like a LEGO instruction manual.**
                
                Every letter is a LEGO block.
                Mutations are like sneaky prank blocks someone swapped in:  

                - Sometimes the LEGO set still works… 🟢  
                - Sometimes the spaceship turns into a wobbly tower… 🔴  

                Spot them and fix them to make the sequence correct!
                """)



    if 'level2_original' not in st.session_state:
        originals = utils.generate_dna(length=6, count=2)
        mutated = [utils.introduce_mutations(seq, num_mutations=2) for seq in originals]
        st.session_state.level2_original = originals
        st.session_state.level2_mutated = mutated

    level_cleared = True

    for idx, (original, mutated) in enumerate(zip(st.session_state.level2_original, st.session_state.level2_mutated), start=1):
        st.markdown(f"**Question {idx}: Correct the mutated DNA**")
        st.markdown(f"**Mutated:** {mutated}")

        default_value = st.session_state.level_inputs.get(f"level2_{idx}", "")
        user_input = st.text_input(f"Corrected sequence Q{idx}:", key=f"level2_input_{idx}", value=default_value).upper().strip()

        hint_shown = f"level2_hint_{idx}" in st.session_state.level_hints_shown
        if not hint_shown:
            if st.button(f"💡 Show Hint Q{idx}"):
                st.session_state.level_hints_shown[f"level2_hint_{idx}"] = True
                st.session_state.hints_used += 1
                st.rerun()
        if hint_shown:
            st.markdown("**Hint:** Compare each base with the original. Look carefully at differences to spot mutations!")

        if st.button(f"📝 Show Answer Q{idx}"):
            st.markdown(f"**Correct Answer:** {original}")
            st.markdown("**Explanation:** Only letters matching the original sequence are correct; others are mutations.")

        if st.button(f"✅ Check Answer Q{idx}"):
            st.session_state.level_inputs[f"level2_{idx}"] = user_input
            if user_input == original:
                st.success(f"🎉 Correct! Question {idx} fixed!")
            else:
                st.error(f"❌ Incorrect. Correct answer: {original}")
                level_cleared = False

        if st.session_state.level_inputs.get(f"level2_{idx}", "") != original:
            level_cleared = False

    if level_cleared:
        st.success("🎉 Hurry!! Level 2 cleared")
        if "level2_done" not in st.session_state:
            st.session_state.score += len(st.session_state.level2_original)
            st.session_state.level2_done = True
        if st.button("➡️ Next Level"):
            st.session_state.completed_levels.add(2)
            st.session_state.current_level = 3
            st.rerun()
