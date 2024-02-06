import json
import os

output_dir = "json-text"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

data = {
    "expected response" : ["a list of phrases, sentences, or intents"]
}

jsonl_data = []
a = []


for category, values in data.items():

    for value in values:
        json_obj = {
            "messages": [
                {
                    "role": "system",
                    "content": "request from for the system" #! не забудь поменять
                },
                {
                    "role": "user",
                    "content": value
                },
                {
                    "role": "assistant",
                    "content": category
                }
            ]
        }
        jsonl_data.append(json.dumps(json_obj, ensure_ascii=False))
with open("json-text/output.jsonl", "w", encoding="UTF-8") as outfile:
    outfile.write("\n".join(jsonl_data))

print("Успешно")
