import os
import re


def validate_wiki_references(wiki_dir, code_dir):
    # Regex to find Stable IDs in Markdown (e.g., `sample_app/src/core/auth.ts::validateSession#func`)
    id_pattern = re.compile(r"((?:sample_app|prompts|skills|wiki)/.*?)")

    for root, _, files in os.walk(wiki_dir):
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    refs = id_pattern.findall(f.read())
                    for ref in refs:
                        # Extract file path from Stable ID (before the first '::')
                        target_file = ref.split("::")[0]
                        full_path = os.path.join(os.getcwd(), target_file)

                        if not os.path.exists(full_path):
                            print(f"🚨 GHOST LINK: {file} references non-existent {target_file}")
                        else:
                            print(f"✅ VERIFIED: {ref}")


# validate_wiki_references('wiki', 'sample_app')
