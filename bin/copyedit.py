import os
import re
import sys
import openai

def setup_openai():
    openai.api_key = os.getenv('OPEN_AI_BEARER_TOKEN')

def clean_content(content):
    content = re.sub(r'^---[\s\S]*?---', '', content, flags=re.MULTILINE)
    content = re.sub(r'<.*?>', '', content)
    content = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
    content = re.sub(r'(?<=\n)[ ]{4,}.*?(\n|$)', '', content)
    content = re.sub(r'#[^\n]*', '', content)
    content = re.sub(r'\*.*?\*', '', content)
    return content

def correct_typos(text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": """
You are an experienced technical copy editor. Your task is to fix spelling and grammatical errors in markdown and mdx files.

- Focus on improving readability, grammar, and spelling of the textual content.
- Ignore code blocks, inline code, and any markup or non-text content (such as HTML tags, markdown headers, links, or bullet points).
- Only correct prose and narrative sections.
- Please keep technical terms intact and avoid altering specialized terminology.
            """},
            {"role": "user", "content": text}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    cleaned_content = clean_content(content)
    corrected_text = correct_typos(cleaned_content)

    if cleaned_content != corrected_text:
        corrected_content = content.replace(cleaned_content, corrected_text)
        return corrected_content

    return None

def process_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.md') or file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                corrected_content = process_file(file_path)

                if corrected_content:
                    output_file = f"{os.path.splitext(file_path)[0]}_corrected{os.path.splitext(file_path)[1]}"
                    with open(output_file, 'w', encoding='utf-8') as out_file:
                        out_file.write(corrected_content)
                    print(f"Processed: {file_path}")
                else:
                    print(f"No changes found for: {file_path}")

if __name__ == "__main__":
    setup_openai()
    folder = sys.argv[1]
    process_folder(folder)
