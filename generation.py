import json
from generate_panels import generate_panels
from stability_ai import text_to_image
from add_text import add_text_to_panel
from create_strip import create_strip
from dotenv import load_dotenv

load_dotenv()


# SCENARIO = """
# Characters: Adrien is a guy with blond hair. Vincent is a guy with black hair.
# Story: Adrien and Vincent work at the office and want to start a new product, and they create it in one night before presenting it to the board.
# """
# STYLE = "american comic, colored"


def get_panels(scenario, style):
    SCENARIO = scenario
    STYLE = style
    print(f"Generate panels with style '{STYLE}' for this scenario: \n {SCENARIO}")
    panels = generate_panels(SCENARIO)
    return panels


def generate_comic(panels, style):
    STYLE = style
    with open('output/panels.json', 'w') as outfile:
        json.dump(panels, outfile)

    panel_images = []

    for panel in panels:
        panel_prompt = panel["description"] + ", cartoon box, " + STYLE
        print(f"Generate panel {panel['number']} with prompt: {panel_prompt}")
        panel_image = text_to_image(panel_prompt)
        panel_image_with_text = add_text_to_panel(panel["text"], panel_image)
        panel_image_with_text.save(f"output/panel-{panel['number']}.png")
        panel_images.append(panel_image_with_text)

    create_strip(panel_images).save("output/comic.png")
