import subprocess
import os

output_dir = "json-text"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

prepared_file = os.path.join(output_dir, "output_prepared.jsonl")
if os.path.exists(prepared_file):
    os.remove(prepared_file)

command = 'openai tools fine_tunes.prepare_data -f json-text/output.jsonl'
subprocess.run(command, shell=True)