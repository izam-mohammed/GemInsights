# GemInsights

Repo for GemInsights: A project in Lablab ai Gemini Hackathon

![](https://drive.google.com/uc?export=view&id=1qJD9HbdUZ3U3CgvY2IsGLX5NZIVLznL4)


### Installation and Setup 🛠️

These installation instructions assume that you have conda installed and added to your path.

To get started with the Note Taking Website, follow these steps:

1. Clone the Repository: Clone this repository to your local machine using the following command:

   ```bash
   git clone https://github.com/izam-mohammed/GemInsights
   cd GemInsights
   ```

2. Create a virtual environment (or modify an existing one).
   ```bash
   conda create -n geminsights python=3.11  # Skip if using an existing environment.
   conda activate geminsights
   ```
 
3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Set the google cloud credentials in credentials folder as cloud_credentials.json

5. Run the server
   ```bash
   streamlit run app.py
   ```

### pipelines

- Visualizations 
- Prompt Creation
- Prompting
- Evaluation

## Hackathon Team members 👥

- [Izam Mohammed](github.com/izam-mohammed)
- [Vishu Prasad]()
- [Afsal](https://github.com/AfsalAfzz-Pro)
- [Josekutty](github.com/jkutty-7)
- [AbduRahiman]()
- [Amal]()


## Repository Code Formatting 📝

This repository follows a consistent code formatting approach to enhance readability and maintainability.

### Python Files 🐍

Python files in this repository are formatted using [Black](https://github.com/psf/black). Black is an opinionated code formatter that automatically formats your Python code to adhere to the PEP 8 style guide.

To ensure that your Python code is formatted correctly, you can install Black and format the code by running the following command in your terminal:

```bash
pip install black
black .
```

### HTML Files 🌐

HTML files in this repository are formatted using [Prettier](https://prettier.io/). Prettier is a code formatter that supports multiple languages, including HTML.

## License 📄

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements 🙌

- Gemini-pro, Gemini-pro-vision
- Llama-index
- TruLens
- Vertex AI

---

Feel free to customize this `README.md` template to suit your project's specific details and add any additional sections you find relevant.