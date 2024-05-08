
# AI based Comics Generator

This project uses AI to generate comic images based on provided prompts. It uses the Stability API for image generation and editing.

## Setup

1. **Environment Variables**: Copy the `sample.env` file and rename it to `.env`. Fill in the required API keys:

    ```env
    OPENAI_API_KEY= YOUR OPEN API KEY
    STABILITY_KEY= YOUR STABILITY API KEY
    TOGETHER_API_KEY= YOUR TOGETHER API KEY
    ```

2. **Install Dependencies**: This project uses Python and pip for package management. Install the required packages with the following command:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, execute the `app.py` file using Streamlit:

```bash
streamlit run app.py
```

This will start the Streamlit server and the application will be accessible at `localhost:8501` in your web browser.

## Usage

The application generates comic images based on the prompts you provide. You can also edit existing images by providing an image path and a prompt.

## Contributing

Contributions are welcome. Please open an issue to discuss your ideas or submit a pull request with your changes.

## License

This project is licensed under the terms of the MIT license.
