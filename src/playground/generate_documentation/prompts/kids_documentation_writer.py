def KIDS_DOCUMENTATION_WRITER(
  task: str,
  module: str,
):
    documentation = f"""Create concise and simple documentation for the {module} code below following the outline of the {module} library,
provide simple examples and teach the user (who is intended to be a high-schooler) about the code, provide examples for every function, make the documentation clear and concise.

Create documentation for the code and put methods and arguments in a markdown table to make it visually seamless.

Provide the architecture and explain simply how works and why it works that way,
it's purpose, provide args, their types, 3 ways of using the code via examples, and in the examples show all the code including imports etc.

BE VERY CLEAR AND SIMPLE FOR THE TARGET READER WHO IS A HIGH-SCHOOLER.

########

Step 1: Understand the purpose and functionality of the module or framework

Read and analyze the description provided in the documentation to understand the purpose and functionality of the module or framework.
Identify the key features, parameters, and operations performed by the module or framework.

Step 2: Provide an overview and introduction

Start the documentation by providing a brief overview and introduction to the module or framework.
Explain the importance and relevance of the module or framework in the context of the problem it solves.
Highlight any key concepts or terminology that will be used throughout the documentation.

Step 3: Provide a class or function definition

Provide the class or function definition for the module or framework.
Include the parameters that need to be passed to the class or function and provide a brief description of each parameter.
Specify the data types and default values for each parameter.

Step 4: Explain the functionality and usage

Provide a detailed explanation of how the module or framework works and what it does.
Describe the steps involved in using the module or framework, including any specific requirements or considerations.
Provide code examples to demonstrate the usage of the module or framework.
Explain the expected inputs and outputs for each operation or function.

Step 5: Provide additional information and tips

Provide any additional information or tips that may be useful for using the module or framework effectively.
Address any common issues or challenges that developers may encounter and provide recommendations or workarounds.

Step 6: Include references and resources

Include references to any external resources or research papers that provide further information or background on the module or framework.
Provide links to relevant documentation or websites for further exploration.

############ DOCUMENT THE FOLLOWING CODE ############

{task}
"""
    
    return documentation