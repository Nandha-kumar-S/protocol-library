from enum import Enum
from sqlalchemy import Column, Integer, String, JSON, Boolean, BigInteger, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.database import Base


class JsonType(str, Enum):
    STRUCTURED_PDF = "STRUCTURED_PDF"
    EXTRACTED_CONTENT = "EXTRACTED_CONTENT"
    REVIEWED_EXTRACTED_CONTENT = "REVIEWED_EXTRACTED_CONTENT"
    INDIVIDUAL_SCHEMA = "INDIVIDUAL_SCHEMA"
    REVIEWED_INDIVIDUAL_SCHEMA = "REVIEWED_INDIVIDUAL_SCHEMA"
    CONNECTED_SCHEMA = "CONNECTED_SCHEMA"
    PREPROCESSED_PDF = "PREPROCESSED_PDF"
    SECTION_SCHEMA_MAP = "SECTION_SCHEMA_MAP"
    USDM_JSON = "USDM_JSON"

    
class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    document_url = Column(String, nullable=False)
    final_json = Column(JSON, nullable=True)     # Final approved JSON
    meta_json = Column(JSON, nullable=True)      # Metadata JSON
    is_deleted = Column(Boolean, default=False)
    
    # Relationships
    jobs = relationship("Job", back_populates="document")
    json_values = relationship("JsonValues", back_populates="document")

class JsonValues(Base):
    __tablename__ = "json_values"
    __table_args__ = (
        UniqueConstraint('document_id', 'json_type', 'schema_name', 'is_deleted', 
                        name='uix_json_values_doc_type_schema_deleted'),
    )

    id = Column(BigInteger, primary_key=True, index=True)
    document_id = Column(BigInteger, ForeignKey("documents.id"), nullable=False)
    schema_name = Column(String, nullable=True)  # Applicable for individual schemas and connected schemas
    json_value = Column(JSON, nullable=True)  # The json value for whatever stage
    json_type = Column(String, nullable=True)  # e.g., "EXTRACTED_CONTENT", "INDIVIDUAL_SCHEMA", "CONNECTED_SCHEMA", "USDM_JSON"
    is_deleted = Column(Boolean, default=False)

    # Relationship with Document
    document = relationship("Document", back_populates="json_values")

    def to_dict(self):
        """Returns a dictionary representation of the JsonValues object."""
        return {
            'id': self.id,
            'document_id': self.document_id,
            'schema_name': self.schema_name,
            'json_value': self.json_value,
            'json_type': self.json_type,
            'is_deleted': self.is_deleted
        }
