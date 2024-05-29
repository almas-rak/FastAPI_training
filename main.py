from datetime import datetime
from enum import Enum
from typing import List, Optional, Union

from fastapi import FastAPI, Depends
from pydantic import BaseModel, Field

app = FastAPI(
    title="trading App"
)


