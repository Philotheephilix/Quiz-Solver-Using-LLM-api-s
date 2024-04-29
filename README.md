# Quiz Solver Using Chat-GPT

## Overview

This repository provides a solution for solving quiz questions using LLM models, THis is a generic tool. With this tool, you can easily access the capabilities of Chat-GPT / Claude ai or any other llm by simply adding simple syntax in Solver/connect.py to assist in answering quiz questions.

## Features

- **Question Solving:** Utilize Chat-GPT / Claude ai to generate answers to quiz questions.
- **Easy Integration:** Simple setup process for accessing the quiz-solving functionality.
- **Customization:** Options for adjusting the behavior and settings of model according to your preferences.

## Installation

To get started, clone this repository to your local machine:

``` bash
git clone https://github.com/your-username/Quiz-Solver-Using-Chat-GPT.git
cd Quiz-Solver-Using-Chat-GPT
```
## Models Supported 
- OpenAi (Text only)
- Claude ai (Text only)

#### Switch between models by Commenting/Uncommenting line 16,17 in main.py

## Installation
Install the required dependencies by running:
``` bash
pip install -r requirements.txt
```

Add Your API key of the desired model in Solver/config.py
- Change API_KEY value to your own key
 

Run the main script:
``` bash
python main.py
```
Follow the prompts to input your quiz questions.
Configuration

You can customize the behavior of Models by modifying the prompt in the communicate.py file. Adjust parameters such as the maximum number of tokens, temperature, and top-k sampling to tailor the responses to your preferences.

## Usage

Start the flask application by running main.py and Send HTML Requests with the questions in the below format

``` json
 {'question': "Linux is a open source software",'options':['true','false']}
```
Design your application to send request in this format to http://127.0.0.1:5000 by default

### ACTUAL EXAMPLE OF THE REQUESTS GENERATION CAN BE FOUND IN <a href='https://github.com/Philotheephilix/oracle-bot'>PHILOTHEEPHILIX/ORACLE-BOT</a>

## Contributions
Contributions to this project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.