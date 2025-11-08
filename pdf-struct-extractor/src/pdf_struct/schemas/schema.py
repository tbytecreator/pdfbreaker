from pydantic import BaseModel
from typing import List, Optional

class ExtractedData(BaseModel):
    title: str
    author: Optional[str]
    content: str
    keywords: List[str]

class PDFSchema(BaseModel):
    data: ExtractedData
    page_count: int
    extraction_date: str