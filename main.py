import json
from urllib import request
from workflow_parser import workflow_parser


def queue_prompt(prompt: str):
    p = {"prompt": prompt}
    data = json.dumps(p).encode('utf-8')
    req = request.Request("http://localhost:8188/prompt", data=data)
    request.urlopen(req)


if __name__ == "__main__":
    with open("workflows/flux_workflow_api.json", "r") as file:
        json_data = file.read()

    variables = {
        "image_width": 1024,
        "image_height": 1024,
        "sampler": "euler",
        "scheduler": "simple",
        "steps": 30,
        "image_prompt": "A cat sitting on a wall"
    }

    prompt_dict = json.loads(workflow_parser(json_data, variables))
    queue_prompt(prompt_dict)
