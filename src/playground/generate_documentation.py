import inspect
import os
import threading

import debugpy
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
import pydantic
from src.playground.generate_documentation.prompts.documentation_writer import DOCUMENTATION_WRITER
from src.playground.generate_documentation.prompts.kids_documentation_writer import KIDS_DOCUMENTATION_WRITER
from langchain_openai import ChatOpenAI

########## Importing the classes you would like to generate documentation for here ##########

from src.routers.rearrangeSwarm.router import streamRearrangeSwarm
from src.routers.spreadsheetSwarm.router import streamSpreadsheetSwarm
from src.routers.designAndRunSwarm.stream import streamDesignAndRunSwarm
from src.routers.designAndRunSwarm.designSwarm import designSwarm
import glob
import json

#############################################################################################

load_dotenv()

# model = ChatOpenAI(
#     max_tokens=4000,
#     model='gpt-4o',
#     api_key=os.getenv("OPENAI_API_KEY")
# )

model = ChatAnthropic(model="claude-3-5-sonnet-20240620", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY"))

def collect_schema(folder_path):
    """
    Collects all the pydantic models from the files in the given folder path and returns a formatted string.
    """
    import importlib.util

    schema = ""

    # Get all the Python files in the folder path
    files = glob.glob(f"{folder_path}/**/*.py", recursive=True)

    for file in files:
        try:
            # Get the module name from the file path
            module_name = os.path.splitext(os.path.basename(file))[0]

            # Import the module dynamically
            spec = importlib.util.spec_from_file_location(module_name, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            # Iterate through the attributes of the module
            for name, obj in inspect.getmembers(module):
                # Check if the object is a subclass of Pydantic's BaseModel and not BaseModel itself
                if inspect.isclass(obj) and issubclass(obj, pydantic.BaseModel) and obj is not pydantic.BaseModel:
                    # Get the schema of the Pydantic model (for Pydantic v2)
                    schema += f"Model: {name}\n"
                    schema += f"{obj.model_json_schema()}\n\n"
        except Exception as e:
            # If any error occurs, log the file and continue with other files
            print(f"Error processing {file}: {e}")

    return schema

def process_documentation(cls):
    """
    Process the documentation for a given class using an LLM and save it in a Markdown file.
    """

    doc = inspect.getdoc(cls)
    source = inspect.getsource(cls)
    input_content = (
        "Class Name:"
        f" {cls.__name__}\n\nDocumentation:\n{doc}\n\nSource"
        f" Code:\n{source}"
        f" \n\nSchema:\n{collect_schema("src/core/schemas")}" 
    )

    # Process with OpenAI model (assuming the model's __call__ method takes this input and returns processed content)
    processed_content = model(
        DOCUMENTATION_WRITER(input_content, f"{cls}")
        # KIDS_DOCUMENTATION_WRITER(input_content, f"{cls}")
    )

    # doc_content = f"# {cls.__name__}\n\n{processed_content}\n"
    doc_content = f"{processed_content.content}\n"

    # Create the directory if it doesn't exist
    # dir_path = "docs/swarms/tokenizers"
    dir_path = "workspace"
    os.makedirs(dir_path, exist_ok=True)

    # Write the processed documentation to a Markdown file
    file_path = os.path.join(dir_path, f"{cls.__name__.lower()}.md")
    with open(file_path, "w") as file:
        file.write(doc_content)

    print(f"Documentation generated for {cls.__name__}.")


def main():
    # debugpy.listen(("0.0.0.0", 5678))
    # debugpy.wait_for_client()

    modules = [
        streamRearrangeSwarm,
        streamSpreadsheetSwarm,
        streamDesignAndRunSwarm,
        designSwarm,
    ]
    threads = []
    for cls in modules:
        thread = threading.Thread(
            target=process_documentation, args=(cls,)
        )
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    print("Documentation generated in 'workspace' directory.")

if __name__ == "__main__":
    main()