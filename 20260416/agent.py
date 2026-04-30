from __future__ import annotations
import os
import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import List

from dotenv import load_dotenv
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel

# load .env from same directory as this script
here = Path(__file__).parent
load_dotenv(here / ".env")

# 1. Define the structured output
class CodeImprovement(BaseModel):
    file_path: str = Field(description="The path to the file being reviewed")
    issue: str = Field(description="Description of the identified problem")
    suggestion: str = Field(description="Specific recommendation or refactored code")
    priority: str = Field(description="Priority level: High, Medium, or Low")


@dataclass
class ProjectContext:
    root_dir: Path

# 2. Configure the Model
model = AnthropicModel('claude-sonnet-4-6')

# 3. Initialize the Agent
analyst_agent = Agent(
    model,
    deps_type=ProjectContext,
    system_prompt=(
        "You are an expert Senior Engineer. Use your tools to audit the codebase. "
        "First, list files to see the structure, then read relevant files. "
        "Finally, provide structured improvements."
    ),
)

# --- Tools ---

@analyst_agent.tool
def list_dir(ctx: RunContext[ProjectContext], subdir: str = ".") -> List[str]:
    """Lists files in the project directory."""
    try:
        target = ctx.deps.root_dir / subdir
        print(f"STATUS: list_dir -> {target}", flush=True)
        return [f.name for f in target.iterdir() if not f.name.startswith('.')]
    except Exception as e:
        print(f"STATUS: list_dir error -> {e}", flush=True)
        return [f"Error listing {subdir}: {str(e)}"]


@analyst_agent.tool
def read_file(ctx: RunContext[ProjectContext], file_path: str) -> str:
    """Reads the full content of a file."""
    try:
        full_path = ctx.deps.root_dir / file_path
        print(f"STATUS: read_file -> {full_path}", flush=True)
        return full_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"STATUS: read_file error -> {e}", flush=True)
        return f"Error reading {file_path}: {str(e)}"


@analyst_agent.tool
def write_file(ctx: RunContext[ProjectContext], file_path: str, content: str) -> str:
    """Overwrites or creates a file with new content."""
    try:
        full_path = ctx.deps.root_dir / file_path
        print(f"STATUS: write_file -> {full_path}", flush=True)
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(content, encoding='utf-8')
        print(f"STATUS: write_file success -> {file_path}", flush=True)
        return f"Successfully updated {file_path}"
    except Exception as e:
        print(f"STATUS: write_file error -> {e}", flush=True)
        return f"Error writing {file_path}: {str(e)}"


# --- Execution ---

async def main():
    # Adjust this base path as needed
    base_path = Path("c:/Users/samol/Documents/TUES/hackthons/HackGorski12")
    deps = ProjectContext(root_dir=base_path)

    print(f"--- Starting Claude 4.6 Analysis on {base_path} ---", flush=True)
    print("STATUS: preparing to invoke agent.run", flush=True)

    try:
        # We pass the output_type in the .run() call
        result = await analyst_agent.run(
            "Scan the project directory and suggest code improvements.",
            deps=deps,
            output_type=List[CodeImprovement]
        )

        print("\n" + "="*50)
        print("REVIEW RESULTS")
        print("="*50)
        print("STATUS: analysis finished, formatting results", flush=True)

        for item in result.data:
            print(f"\n[{item.priority}] {item.file_path}")
            print(f"Issue: {item.issue}")
            print(f"Fix: {item.suggestion}")
            print(flush=True)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    asyncio.run(main())
