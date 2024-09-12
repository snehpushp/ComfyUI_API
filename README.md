# ComfyUI_API
This project can be used for image generation using workflow.json of ComfyUI

## How can this project help you?

You can treat this project as a tutorial guide on How to use `ComfyUI APIs` and `workflow.json` using Python.
I'm trying to achieve a seamless experience of generating images from workflow.json


## Steps to follow:

Make sure that `ComfyUI` is installed. [Check here](https://github.com/comfyanonymous/ComfyUI)

Design the workflow that you want to execute using python.


## Rules to edit workflow.json

1. You must first locate the values that you want to keep as input.
   - For example: `Image Prompt`
2. You must replace these values in `workflow.json` as follows:
   - The replaced value is a string that starts and ends with `<<` and `>>` respectively. For example: `<<image_prompt>>`
   - By default, the type of the value is `str` but if you want to assign any particular type (say int or float), you can write `<<image_size:int>>`
   - To assign default values to these inputs in case custom value is not passed, separate it with another `:`. For example, `<<image_width:int:1024>>`
   - If you are assigning default values and type is str, you can ignore typing str. For example, `<<image_prompt::A cat sitting on wall>>`
   - For the values where you don't provide default values, they will be compulsory.
   
Please refer to `main.py` for example usage.