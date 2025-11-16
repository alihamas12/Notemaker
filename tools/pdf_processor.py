from langchain.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import pdfplumber
import os

class PDFProcessorInput(BaseModel):
    file_path: str = Field(description="Path to the PDF file to process")

class PDFProcessorTool(BaseTool):
    name: str = "pdf_processor"
    description: str = "Process PDF files and extract content for note generation"
    args_schema: Type[BaseModel] = PDFProcessorInput

    def _run(self, file_path: str) -> str:
        try:
            content = []
            with pdfplumber.open(file_path) as pdf:
                for page in pdf.pages:
                    text = page.extract_text()
                    if text:
                        content.append(text)
            
            full_content = "\n".join(content)
            
            # Limit content size to avoid token limits
            if len(full_content) > 10000:
                full_content = full_content[:10000] + "... (truncated)"
            
            return full_content
        except Exception as e:
            return f"Error processing PDF: {str(e)}"
    
    async def _arun(self, file_path: str):
        raise NotImplementedError("PDFProcessorTool does not support async")