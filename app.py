import streamlit as st
from rembg import remove
from PIL import Image
import io

st.set_page_config(page_title="Rimozione Sfondo Immagini", page_icon=":dragon:")

st.title("Rimozione Sfondo Immagini con AI")
st.write("Carica un'immagine e rimuovi lo sfondo automaticamente.")

uploaded_file = st.file_uploader("Carica un'immagine", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Immagine originale", use_column_width=True)

    with st.spinner("Rimozione dello sfondo in corso..."):
        img_byte_arr = io.BytesIO()
        input_image.save(img_byte_arr, format='PNG')
        img_byte_arr = img_byte_arr.getvalue()

        output = remove(img_byte_arr)
        output_image = Image.open(io.BytesIO(output))

        st.image(output_image, caption="Immagine senza sfondo", use_column_width=True)
        st.success("Sfondo rimosso con successo!")
        
        st.download_button(
            label="Scarica Immagine Senza Sfondo",
            data=output,
            file_name="immagine_senza_sfondo.png",
            mime="image/png"
        )
