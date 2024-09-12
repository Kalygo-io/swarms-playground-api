import inspect
import os
import threading

from dotenv import load_dotenv
from playground.generate_documentation.prompts.documentation_writer import DOCUMENTATION_WRITER
from langchain_openai import ChatOpenAI

# from swarms.structs.majority_voting import MajorityVoting
# from swarms.structs.stackoverflow_swarm import StackOverflowSwarm
# from swarms.structs.task_queue_base import TaskQueueBase

########## Importing the classes you would like to generate documentation for here ##########

#############################################################################################

load_dotenv()

model = ChatOpenAI(
    max_tokens=4000,
    model='gpt-4o-mini',
    api_key=os.getenv("OPENAI_API_KEY")
)


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
    )

    # Process with OpenAI model (assuming the model's __call__ method takes this input and returns processed content)
    processed_content = model(
        DOCUMENTATION_WRITER(input_content, "swarms.world")
    )

    # doc_content = f"# {cls.__name__}\n\n{processed_content}\n"
    doc_content = f"{processed_content}\n"

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
    modules = [
        MajorityVoting,
        StackOverflowSwarm,
        TaskQueueBase,
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