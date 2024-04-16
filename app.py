import streamlit as st
import time

from generation import get_panels, generate_comic

st.set_page_config(page_title="AI Comic Generator", page_icon="🦸", layout='wide')


# Function to handle the layout and style of the app
def create_layout():
    st.sidebar.title("AI Comic Generator Settings")
    char_number = st.sidebar.number_input("How many characters are in your comic?", min_value=1, max_value=10, value=2)
    characters = {}
    for i in range(int(char_number)):
        characters[f"Character {i + 1}"] = st.sidebar.text_area(f"Describe Character {i + 1}:")

    comic_style = st.sidebar.selectbox("Choose the style of the comic:",
                                       ["American-Comic", "Manga", "Black-White", "Vintage"])
    story_description = st.sidebar.text_area("Describe the story of the comic:")

    if st.sidebar.button("Generate Comic"):
        generate_comic_main(characters, comic_style, story_description)


def generate_comic_main(characters, style, story):
    with st.spinner("Generating Comic..."):
        characters_description = ""
        for char, desc in characters.items():
            characters_description += f"{char}: {desc}\n"
        input = "Characters: " + characters_description + "Story: " + story
        style = style.lower().replace("-", " ")
        panels = get_panels(input, style)
        generate_comic(panels, style)
        st.progress(1.0)
    st.success("Comic generated successfully!")
    st.image("output/comic.png", caption="Generated Comic Strip")


if __name__ == "__main__":
    create_layout()
