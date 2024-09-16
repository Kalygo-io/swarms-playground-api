import inspect
import os
import threading
from dotenv import load_dotenv
from src.core.helpers.gen_tests.extract_code_from_markdown import extract_code_from_markdown
from src.core.prompts.TESTS_WRITER import TESTS_WRITER
from langchain_openai import ChatOpenAI
import debugpy

load_dotenv()

model = ChatOpenAI(
  max_tokens=4000,
  model='gpt-4o',
  api_key=os.getenv("OPENAI_API_KEY")
)

from src.core.classes.agent import Agent

load_dotenv()

def create_test(cls):
    doc = inspect.getdoc(cls["class"])
    source = inspect.getsource(cls["class"])
    input_content = f"""Class Name: {cls["class"].__name__}

Documentation: {doc}

Source Code: {source}
    """
    
    processed_content = model.invoke( # Process with the LLM
        TESTS_WRITER(input_content, cls["module"])
    )

    generated_tests = extract_code_from_markdown(processed_content.content)

    dir_path = "scratchspace" # Create the directory if it doesn't exist
    os.makedirs(dir_path, exist_ok=True)

    # Write the processed documentation to a Python file
    file_path = os.path.join(dir_path, f"test_{cls["class"].__name__.lower()}.py")
    with open(file_path, "w") as file:
        file.write(generated_tests)

def main():
    print('generating tests...')

    # debugpy.listen(("0.0.0.0", 5678))
    # debugpy.wait_for_client()

    classes = [
        {
            "class": Agent,
            "module": "src.core.classes.agent"
        }
    ]
    threads = []
    for cls in classes:
        thread = threading.Thread(target=create_test, args=(cls,))
        threads.append(thread)
        thread.start()

    for thread in threads: # Wait for all threads to complete
        thread.join()

    print("Tests generated.")

if __name__ == "__main__":
    main()