import re


def workflow_parser(text: str, variables: dict = None):
    """
    Replaces variables in a string with their corresponding values.

    Args:
        text: The string of json workflow.
        variables: A dictionary of variable names and their values.

    Returns:
        The string with variables replaced.

    Raises:
        ValueError: If a required variable is not provided.
    """

    if variables is None:
        variables = {}

    for match in re.findall(r'("<<.*?>>")', text):
        var_str = match[3:-3]  # Removing "<< and >>" from start and end
        var_parts = var_str.split(":")
        if len(var_parts) > 3:
            raise ValueError(f"The input values in the workflow is not properly formatted. Please confirm {match}")

        var_name = var_parts[0].strip()
        var_type = "str"
        if len(var_parts) > 2:
            var_type = var_parts[1].strip() or "str"  # Default type as str

        # Check if variable is provided
        if var_name not in variables:
            if len(var_parts) != 3:  # No default value provided
                raise ValueError(f"Missing required variable: {var_name}")
            else:
                var_value = var_parts[2].strip()
                if var_type == "int":
                    var_value = int(var_value)
                elif var_type == "float":
                    var_value = float(var_value)
                elif var_type == "bool":  # TODO: Implementation needs to be changed for bool value. json accepts true/false
                    var_value = var_value.lower() == "true"  # Convert string to bool
        else:
            # If value is provided by the user, we just need to insure the type of the value.
            var_value = variables[var_name]
            if type(var_value).__name__ != var_type:
                raise ValueError(f"Value provided for {var_name} is not of correct type."
                                 f"Expected {var_type}, Got {var_value} of type {type(var_value)}!")

        if var_type == "str":
            var_value = '"' + var_value + '"'  # Adding "" to make it string as we've matched ""
        text = text.replace(match, str(var_value), 1)

    return text


if __name__ == "__main__":
    with open("workflows/flux_workflow.json", "r") as file:
        json_data = file.read()

    variables = {
        "image_height": 512,
        "sampler": "ddim",
        "scheduler": "dpm_solver",
        "steps": 30,
        "image_prompt": "A cat sitting on a wall"
    }

    result = workflow_parser(json_data, variables)
    print(result)
