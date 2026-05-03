# YouTube Script Generator (AI Powered)

## Overview

This project is an AI-powered YouTube script generator that creates engaging video scripts based on user inputs like topic, tone, and duration. It uses Google Gemini API via Google AI Studio to generate high-quality content.

## Features
- Generate YouTube video scripts instantly
- Choose tone (Informative, Casual, Funny, etc.)
- Set video duration
- Clean and structured script output:
    - Hook
    - Introduction
    - Main content
    - Conclusion with CTA

## Tech Stack
- Python 
- Streamlit 
- Gemini API 
- LangChain 

## Project Structure
project/
│── app.py                # Streamlit UI
│── script_generator.py   # Core AI logic
│── .env                  # API key (not pushed to GitHub)
│── requirements.txt      # Dependencies
│── README.md 

## Setup Instructions
1. Clone the repository
```git clone https://github.com/your-username/youtube-script-generator.git```
```cd youtube-script-generator```
2. Create virtual environment (optional but recommended)
```python -m venv venv```
```venv\Scripts\activate ```  # Windows
3. Install dependencies
```pip install -r requirements.txt```
4. Add API key: Create a .env file:

```GOOGLE_API_KEY=your_api_key_here```
Get your API key from Google AI Studio.

5. Run the app
```streamlit run app.py```

## Security Note
- API key is stored in .env
- .env is excluded using .gitignore
- Never expose API keys publicly

## Author
Cilus Duwadi
Project focused on AI + backend integration using Gemini API.