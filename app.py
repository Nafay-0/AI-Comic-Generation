import streamlit as st
import time

from generation import get_panels, generate_comic, generate_characters_description

st.set_page_config(page_title="AI Comic Generator", page_icon="🦸", layout='wide')

# Function to handle the layout and style of the app
def create_layout():
    st.sidebar.title("AI Comic Generator Settings")
    auto_generate_descriptions = st.sidebar.checkbox("Automatically generate character descriptions")

    char_number = st.sidebar.number_input("How many characters are in your comic?", min_value=1, max_value=10, value=2)
    characters = {}
    for i in range(int(char_number)):
        if auto_generate_descriptions:
            auto_description = auto_generate_description()
            characters[f"Character {i + 1}"] = st.sidebar.text_area(f"Describe Character {i + 1}:",
                                                                    value=auto_description, disabled=True)
        else:
            characters[f"Character {i + 1}"] = st.sidebar.text_area(f"Describe Character {i + 1}:",
                                                                    placeholder=f"Character {i + 1} description")

    comic_style = st.sidebar.selectbox("Choose the style of the comic:",
                                       ["american comic colored, cartoon box", "manga black and white, cartoon box",
                                        "manga colored, cartoon box", "belgium comic, black and white"])
    story_description = st.sidebar.text_area("Describe the story of the comic:")

    if st.sidebar.button("Generate Comic"):
        generate_comic_main(characters, comic_style, story_description, auto_generate_descriptions)

def auto_generate_description():
    # Placeholder for your actual AI-based description generation logic
    return "Automatically generated description of the character."

def generate_comic_main(characters, style, story, auto_generate):
    with st.spinner("Generating Comic..."):
        characters_description = ""
        if auto_generate:
            characters_description = generate_characters_description(story)
            st.success("Character descriptions generated successfully!")
            st.write(characters_description)
        else:
            characters_description = "\n".join([f"{char}: {desc}" for char, desc in characters.items()])

        input = "Characters: " + characters_description + " Story: " + story
        style = style.lower().replace("-", " ")
        panels = get_panels(input, style)
        generate_comic(panels, style, characters_description)
        st.progress(1.0)
    st.success("Comic generated successfully!")
    st.image("output/comic.png", caption="Generated Comic Strip")

if __name__ == "__main__":
    create_layout()
