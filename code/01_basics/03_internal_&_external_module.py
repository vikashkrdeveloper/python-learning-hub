"""
# What is a module in Python?
    ## A module is a file containing Python code that can define functions, classes, and variables. It allows for code reusability and organization.

# What is the purpose of using modules in Python?
    ## Modules help in organizing code, promoting code reuse, and separating functionality into different files.
    ## They also provide a way to share code across multiple programs.

# What is Internal Module in Python?
    ## Internal modules are built-in modules that come with the Python Standard Library. Examples include `math`, `sys`, and `os`.
    ## These modules provide a wide range of functionalities and are readily available for use without any additional installation.

# How to import an internal module in Python?
    ## You can import an internal module using the `import` statement. For example:
    ## ```python
    ## import math
    ## print(math.sqrt(16))  # Output: 4.0
    ## ```

# What is External Module in Python?
    ## External modules are third-party libraries that are not included in the Python Standard Library. Examples include `requests`, `numpy`, and `pandas`.
    ## These modules need to be installed separately using package managers like `pip`.

# How to install and import an external module in Python?
    ## You can install an external module using `pip`. For example:
    ## ```
    ## pip install requests
    ## ```
    ## After installation, you can import it in your code:
    ## ```python
    ## import requests
    ## response = requests.get('https://api.github.com')
    ## print(response.status_code)  # Output: 200
    ## ```

# What is the difference between internal and external modules in Python?
    ## Internal modules are part of the Python Standard Library, while external modules are third-party libraries that need to be installed separately.
    ## Internal modules are readily available and do not require any additional installation, while external modules must be installed using package managers like `pip`.

    ## Additionally, internal modules are maintained as part of the Python language, ensuring compatibility and stability, whereas external modules may vary in quality and support.

    ## Summary:
        ## Internal Modules:
            ## Built-in modules included in the Python Standard Library.
            ## Examples: `math`, `sys`, `os`.
            ## No installation required.
        ## External Modules:
            ## Third-party libraries not included in the Standard Library.
            ## Examples: `requests`, `numpy`, `pandas`.
            ## Require installation using package managers like `pip`.
"""

# Internal Module Example
import math

print("Square root of 16 using internal module 'math':", math.sqrt(16))  # Output: 4.0

# External Module Example
# Need to install it by running: pip install requests
import requests

response = requests.get("https://api.github.com")
import json

print(
    "Response from GitHub API using external module 'requests':",
    json.dumps(response.json(), indent=2),
)  # Output: JSON response


# Pyttsx3 Example
# importing the pyttsx library
import pyttsx3

# initialisation
engine = pyttsx3.init()

# testing
engine.say("My journey with Python began a few years ago. & I am loving it.")
engine.say("Thank you, everyone, for your support.")
engine.say("Jai Shree Ram, Jai Hanuman., Jai Kali Maa.")

engine.runAndWait()
