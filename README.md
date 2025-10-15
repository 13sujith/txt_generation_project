# Text Generation Model with GPT-2

This project is a simple text generation application that uses the GPT-2 model from Hugging Face Transformers to generate coherent paragraphs based on user input prompts.

## Overview

- Uses the GPT-2 pretrained language model for generating text.
- Allows users to input prompts and get generated text as output.
- Simple command-line interface using Python.
- Dependencies managed via `requirements.txt`.

## Installation

To install the necessary packages, run:


The main dependencies are:
- `transformers`
- `torch`

## Usage

Run the text generation script with:


You will be prompted to enter a text prompt. The script will generate and display a continuation of your text using GPT-2.

## How It Works

- The script loads the GPT-2 model and tokenizer.
- The input prompt is tokenized and fed into the model.
- The model generates a sequence of tokens based on the prompt.
- The tokens are decoded to human-readable text and printed.

## Project Structure

- `text_generation.py`: Main script that loads the GPT-2 model and generates text from user input.
- `requirements.txt`: Contains required Python libraries.
- `README.md`: This documentation file.

## Customization

- You can change the maximum length and number of generated sequences in `text_generation.py`.
- GPU acceleration can be added if you modify the device settings in the script.

## License

This project is intended for educational and research purposes.


