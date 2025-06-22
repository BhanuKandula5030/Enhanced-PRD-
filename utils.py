
import openai

def summarize_prd(text, api_key):
    prompt = f"Summarize the following Product Requirements Document in a concise, professional way:\n\n{text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        api_key=api_key
    )
    return response.choices[0].message.content.strip()

def generate_uat_cases(text, api_key):
    prompt = (
        "You are a professional Product Owner. Based on the following PRD, generate clear, actionable "
        "user acceptance test cases in Gherkin format (Given, When, Then). Group scenarios by features "
        "and make the language natural and easy to understand:\n\n"
        f"{text}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        api_key=api_key
    )
    return response.choices[0].message.content.strip()
