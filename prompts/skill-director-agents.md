1. The Skill Creator Director (skill-director-agents.md)
This agent sits between the main Project Director and the labor. It is the "Architect of Capabilities."

Input: A gap analysis from the Project Director (e.g., "We have jCodeMunch but no skill for the specific boto3 patterns used here").

Process: 1.  Inventory Check: Scans skills/ to see if a similar skill exists to use as a base (Standardization).
2.  Spec Gathering: Uses jDocMunch to find the "Source of Truth" for the new skill.
3.  Drafting the "Blueprints": Creates the specific worker-instructions.md for the builder.

Output: A high-precision prompt for the Skill Creator Worker.