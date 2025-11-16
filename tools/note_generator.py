from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class NoteGeneratorInput(BaseModel):
    topic: str = Field(description="The topic for which to generate notes")
    language: str = Field(description="Programming language or subject for notes")

class NoteGeneratorTool(BaseTool):
    name: str = "note_generator"
    description: str = "Generate comprehensive notes for any programming language or subject"
    args_schema: Type[BaseModel] = NoteGeneratorInput

    def _run(self, topic: str, language: str) -> str:
        # This will be handled by the main agent
        return f"Generating comprehensive notes for {language} on topic: {topic}"
    
    async def _arun(self, topic: str, language: str):
        raise NotImplementedError("NoteGeneratorTool does not support async")

def get_note_template():
    return """
# {language} - Complete Notes

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Concepts](#basic-concepts)
3. [Syntax and Structure](#syntax-and-structure)
4. [Data Types and Variables](#data-types-and-variables)
5. [Control Structures](#control-structures)
6. [Functions and Methods](#functions-and-methods)
7. [Advanced Topics](#advanced-topics)
8. [Best Practices](#best-practices)
9. [Common Examples](#common-examples)
10. [FAQ](#faq)

## Introduction
{introduction}

## Basic Concepts
{basic_concepts}

## Syntax and Structure
{syntax_structure}

## Data Types and Variables
{data_types_variables}

## Control Structures
{control_structures}

## Functions and Methods
{functions_methods}

## Advanced Topics
{advanced_topics}

## Best Practices
{best_practices}

## Common Examples
{examples}

## FAQ
{faq}

## Additional Resources
- Official Documentation: [Link]
- Tutorials: [Links]
- Community: [Links]
"""