import inspect
import os
import re
import threading
from dotenv import load_dotenv
from src.playground.prompts.tests_writer import TESTS_WRITER
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
  max_tokens=4000,
  model='gpt-4o',
  api_key=os.getenv("OPENAI_API_KEY")
)

#########
# from swarms.memory.dict_internal_memory import DictInternalMemory
# from swarms.memory.dict_shared_memory import DictSharedMemory
# from swarms.memory.lanchain_chroma import LangchainChromaVectorMemory

from src.core.classes.agent import Agent

#########

load_dotenv()

def extract_code_from_markdown(markdown_content: str):
    """
    Extracts code blocks from a Markdown string and returns them as a single string.

    Args:
    - markdown_content (str): The Markdown content as a string.

    Returns:
    - str: A single string containing all the code blocks separated by newlines.
    """
    # Regular expression for fenced code blocks
    pattern = r"```(?:\w+\n)?(.*?)```"
    matches = re.findall(pattern, markdown_content, re.DOTALL)

    # Concatenate all code blocks separated by newlines
    return "\n".join(code.strip() for code in matches)


def create_test(cls):
    """
    Process the documentation for a given class using OpenAI model and save it in a Python file.
    """
    doc = inspect.getdoc(cls)
    source = inspect.getsource(cls)
    input_content = (
        "Class Name:"
        f" {cls.__name__}\n\nDocumentation:\n{doc}\n\nSource"
        f" Code:\n{source}"
    )

    # Process with OpenAI model (assuming the model's __call__ method takes this input and returns processed content)
    processed_content = model(
        TESTS_WRITER(input_content, "core", "src.core.classes.agent")
    )
    processed_content = extract_code_from_markdown(processed_content.content)

    doc_content = f"# {cls.__name__}\n\n{processed_content}\n"

    # Create the directory if it doesn't exist
    dir_path = "workspace"
    os.makedirs(dir_path, exist_ok=True)

    # Write the processed documentation to a Python file
    file_path = os.path.join(dir_path, f"{cls.__name__.lower()}.py")
    with open(file_path, "w") as file:
        file.write(doc_content)


def main():
    classes = [
        Agent
    ]
    threads = []
    for cls in classes:
        thread = threading.Thread(target=create_test, args=(cls,))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Tests generated.")


if __name__ == "__main__":
    main()