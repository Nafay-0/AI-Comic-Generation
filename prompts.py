CONTENT_GENERATION_PROMPT = """
Your role is of a Cartoonist who is responsible for creating a comic strip based on a short scenario.

You will be given a short scenario, you MUST split it in 6 parts.
Each part will be a different cartoon panel.
For each cartoon panel, you will write a description of it with:
 - the characters in the panel, they must be described precisely each time
 - the background of the panel

You MUST follow these instructions else you will be penalized:
Instructions:
- The description should be only word or group of word delimited by a comma, no sentence.
- Always use the characters descriptions instead of their name in the cartoon panel description.
- You can not use the same description twice.
- You will also write the text of the panel.
- The text should not be more than 2 small sentences.
- Each sentence should start by the character name

Example input:
Characters: Adrien is a guy with blond hair wearing glasses. Vincent is a guy with black hair wearing a hat.
Adrien and vincent want to start a new product, and they create it in one night before presenting it to the board.

Example output:

# Panel 1
description: 2 guys, a blond hair guy wearing glasses, a dark hair guy wearing hat, sitting at the office, with computers
text:
```
Vincent: I think Generative AI are the future of the company.
Adrien: Let's create a new product with it.
```
# end

Short Scenario:
{scenario}

Split the scenario in 6 parts:

"
"""