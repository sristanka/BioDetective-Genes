# level3.py
import streamlit as st
import utils
from PIL import Image

def render_level():
    st.header("Level 3: DNA → Protein 🔄")
    st.markdown("**Concept:** A codon is a sequence of three DNA bases (triplet) that codes for a specific amino acid or a stop signal during protein synthesis. DNA is transcribed into RNA, which is then translated into a chain of amino acids to form a protein.")
    st.markdown("""
            Think of DNA as a secret recipe book for proteins! 🍳
            - Every **codon** (3 letters) is like one ingredient in your recipe.
            - Line them up correctly, and you bake a protein sandwich! 🥪
            - Mess up the order, and you might end up with a weird dish! 🍲
            - Use the codon table to decode the recipe and build your protein!
                """)
    st.markdown("**Note:** Write in this order for eg: 'Met-Ala-Ser' (with hyphens, no spaces)")


    # Hidden codon table image
    image = Image.open("codon_table.png")
    if st.button("📖 Check Codon Table for Help"):
        st.image(image, caption="Codon Table Reference", use_container_width=True)

    # Generate two mRNA sequences if not already
    if 'level3_mrna' not in st.session_state:
        mrnas = utils.generate_random_mrna(num_codons=3, count=2)
        proteins = [utils.translate_mrna_to_protein(m) for m in mrnas]
        st.session_state.level3_mrna = mrnas
        st.session_state.level3_protein = proteins

    level_cleared = True

    for idx, (mrna, correct_protein) in enumerate(zip(st.session_state.level3_mrna, st.session_state.level3_protein), start=1):
        st.markdown(f"**Question {idx}: Translate this mRNA:** {mrna}")

        default_value = st.session_state.level_inputs.get(f"level3_{idx}", "")
        user_input = st.text_input(f"Protein sequence Q{idx}:", key=f"level3_input_{idx}", value=default_value).strip()

        # Hints
        hint_shown = f"level3_hint_{idx}" in st.session_state.level_hints_shown
        if not hint_shown:
            if st.button(f"💡 Show Hint Q{idx}"):
                st.session_state.level_hints_shown[f"level3_hint_{idx}"] = True
                st.session_state.hints_used += 1
                st.rerun()
        if hint_shown:
            st.markdown("**Hint:** Each codon (3 letters) codes for one amino acid. Use the codon table above!")

        # Show answer
        if st.button(f"📝 Show Answer Q{idx}"):
            st.markdown(f"**Correct Protein:** {correct_protein}")
            st.markdown("**Explanation:** Each codon translates to a specific amino acid. Check your codons carefully!")

        # Submit
        if st.button(f"✅ Check Answer Q{idx}"):
            st.session_state.level_inputs[f"level3_{idx}"] = user_input
            if user_input == correct_protein:
                st.success(f"🎉 Correct! Question {idx} protein built!")
            else:
                st.error(f"❌ Incorrect. Correct protein: {correct_protein}")
                level_cleared = False

        # If any question not correct, mark level as not cleared
        if st.session_state.level_inputs.get(f"level3_{idx}", "") != correct_protein:
            level_cleared = False

    # Next Level button & score
    if level_cleared:
        st.success("🎉 Hurry!! Level 3 cleared")
        if "level3_done" not in st.session_state:
            st.session_state.score += len(st.session_state.level3_protein)
            st.session_state.level3_done = True
        if st.button("➡️ Next Level"):
            st.session_state.completed_levels.add(3)
            st.session_state.current_level = 4
            st.rerun()
