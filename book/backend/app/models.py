from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import uuid
from datetime import datetime

class Learner(Base):
    __tablename__ = "learners"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    background = Column(String, nullable=False)  # university_student, software_engineer, ai_practitioner
    preferences = Column(JSON, default={})
    progress = Column(JSON, default={})
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    interactions = relationship("ContentInteraction", back_populates="learner")
    chatbot_queries = relationship("ChatbotQuery", back_populates="learner")

class TextbookModule(Base):
    __tablename__ = "textbook_modules"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False, unique=True)
    content = Column(Text, nullable=False)
    learning_objectives = Column(JSON, default=[])
    review_questions = Column(JSON, default=[])
    prerequisites = Column(JSON, default=[])
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    sections = relationship("ContentSection", back_populates="module")
    interactions = relationship("ContentInteraction", back_populates="module")
    source_references = relationship("SourceReference", back_populates="module")

class ContentSection(Base):
    __tablename__ = "content_sections"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    module_id = Column(String, ForeignKey("textbook_modules.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    section_type = Column(String, nullable=False)  # conceptual, practical, diagram, etc.
    order = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    # Relationships
    module = relationship("TextbookModule", back_populates="sections")
    interactions = relationship("ContentInteraction", back_populates="section")
    source_references = relationship("SourceReference", back_populates="section")

class ContentInteraction(Base):
    __tablename__ = "content_interactions"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    learner_id = Column(String, ForeignKey("learners.id"), nullable=False)
    module_id = Column(String, ForeignKey("textbook_modules.id"), nullable=False)
    section_id = Column(String, ForeignKey("content_sections.id"), nullable=True)
    interaction_type = Column(String, nullable=False)  # read, quiz, simulation, chatbot_query
    content = Column(Text)  # Content of the interaction (for chatbot queries)
    response = Column(Text)  # Response to the interaction (for chatbot responses)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    duration = Column(Integer)  # Duration in seconds

    # Relationships
    learner = relationship("Learner", back_populates="interactions")
    module = relationship("TextbookModule", back_populates="interactions")
    section = relationship("ContentSection", back_populates="interactions")

class ChatbotQuery(Base):
    __tablename__ = "chatbot_queries"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    learner_id = Column(String, ForeignKey("learners.id"), nullable=False)
    query_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    source_content = Column(Text)  # The book content used to generate the response
    confidence_score = Column(Integer)  # Confidence level of the response (0-100)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    is_from_selection = Column(Boolean, default=False)  # Whether query was based on selected text

    # Relationships
    learner = relationship("Learner", back_populates="chatbot_queries")
    source_references = relationship("SourceReference", back_populates="chatbot_query")

class SourceReference(Base):
    __tablename__ = "source_references"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    chatbot_query_id = Column(String, ForeignKey("chatbot_queries.id"), nullable=False)
    module_id = Column(String, ForeignKey("textbook_modules.id"), nullable=False)
    section_id = Column(String, ForeignKey("content_sections.id"), nullable=False)
    content_snippet = Column(Text, nullable=False)
    relevance_score = Column(Integer)  # How relevant this content was to the query (0-100)

    # Relationships
    chatbot_query = relationship("ChatbotQuery", back_populates="source_references")
    module = relationship("TextbookModule", back_populates="source_references")
    section = relationship("ContentSection", back_populates="source_references")

class TranslationCache(Base):
    __tablename__ = "translation_cache"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    original_content_id = Column(String, nullable=False)  # Reference to module or section
    original_content = Column(Text, nullable=False)
    translated_content = Column(Text, nullable=False)
    language = Column(String, nullable=False)  # e.g., "ur" for Urdu
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())