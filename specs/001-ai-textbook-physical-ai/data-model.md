# Data Model: Physical AI & Humanoid Robotics Textbook

## Core Entities

### Learner
- **Attributes**:
  - id: Unique identifier for the learner
  - background: String representing learner background (university student, software engineer, AI practitioner)
  - preferences: JSON object containing content preferences
  - progress: JSON object tracking module completion status
  - createdAt: Timestamp of account creation
  - updatedAt: Timestamp of last update

- **Relationships**:
  - Has many: LearningSessions
  - Has many: ContentInteractions

- **Validation Rules**:
  - background must be one of the specified values
  - createdAt must be a valid timestamp
  - id must be unique

### TextbookModule
- **Attributes**:
  - id: Unique identifier for the module
  - title: Title of the module
  - slug: URL-friendly identifier
  - content: Markdown content of the module
  - learningObjectives: Array of learning objectives
  - reviewQuestions: Array of review questions
  - prerequisites: Array of prerequisite module IDs
  - createdAt: Timestamp of creation
  - updatedAt: Timestamp of last update

- **Relationships**:
  - Has many: ContentSections
  - Has many: ReviewQuestions
  - Belongs to many: Learners (through progress tracking)

- **Validation Rules**:
  - title and slug must be unique
  - content must be valid Markdown
  - learningObjectives must be non-empty array

### ContentSection
- **Attributes**:
  - id: Unique identifier for the section
  - moduleId: Reference to parent module
  - title: Title of the section
  - content: Markdown content of the section
  - sectionType: Type of section (conceptual, practical, diagram, etc.)
  - order: Position within the module
  - createdAt: Timestamp of creation
  - updatedAt: Timestamp of last update

- **Relationships**:
  - Belongs to: TextbookModule
  - Has many: ContentInteractions

- **Validation Rules**:
  - moduleId must reference existing module
  - order must be unique within module
  - sectionType must be valid type

### ContentInteraction
- **Attributes**:
  - id: Unique identifier for the interaction
  - learnerId: Reference to the learner
  - moduleId: Reference to the module
  - sectionId: Reference to the section (optional)
  - interactionType: Type of interaction (read, quiz, simulation, chatbot query)
  - content: Content of the interaction (for chatbot queries)
  - response: Response to the interaction (for chatbot responses)
  - timestamp: When the interaction occurred
  - duration: How long the interaction lasted

- **Relationships**:
  - Belongs to: Learner
  - Belongs to: TextbookModule
  - Belongs to: ContentSection (optional)

- **Validation Rules**:
  - learnerId must reference existing learner
  - moduleId must reference existing module
  - timestamp must be valid

### ChatbotQuery
- **Attributes**:
  - id: Unique identifier for the query
  - learnerId: Reference to the learner
  - queryText: The text of the learner's question
  - responseText: The chatbot's response
  - sourceContent: The book content used to generate the response
  - confidenceScore: Confidence level of the response (0-1)
  - timestamp: When the query was made
  - isFromSelection: Whether the query was based on selected text

- **Relationships**:
  - Belongs to: Learner
  - Has many: SourceReferences

- **Validation Rules**:
  - queryText must be non-empty
  - confidenceScore must be between 0 and 1
  - timestamp must be valid

### SourceReference
- **Attributes**:
  - id: Unique identifier for the reference
  - chatbotQueryId: Reference to the chatbot query
  - moduleId: Reference to the module containing the source
  - sectionId: Reference to the section containing the source
  - contentSnippet: The specific content used in the response
  - relevanceScore: How relevant this content was to the query (0-1)

- **Relationships**:
  - Belongs to: ChatbotQuery
  - Belongs to: TextbookModule
  - Belongs to: ContentSection

- **Validation Rules**:
  - chatbotQueryId must reference existing query
  - relevanceScore must be between 0 and 1

### TranslationCache
- **Attributes**:
  - id: Unique identifier for the cached translation
  - originalContentId: Reference to the original content (could be module or section)
  - originalContent: The original English content
  - translatedContent: The Urdu translation
  - language: Target language code (e.g., "ur")
  - createdAt: When the translation was created
  - updatedAt: When the translation was last updated

- **Relationships**:
  - Belongs to: TextbookModule (or ContentSection)

- **Validation Rules**:
  - language must be valid language code
  - originalContentId must reference existing content
  - createdAt and updatedAt must be valid timestamps

## State Transitions

### Learner Progress Tracking
- Initial State: Unregistered
- Transition 1: Unregistered → Registered (when account is created)
- Transition 2: Registered → Module Started (when learner begins first module)
- Transition 3: Module Started → Module Progressing (when learner interacts with content)
- Transition 4: Module Progressing → Module Completed (when all requirements for module are met)
- Transition 5: Module Completed → Next Module Available (when prerequisites are satisfied)

### Content Interaction States
- Initial State: Not Interacted
- Transition 1: Not Interacted → Read (when content is viewed)
- Transition 2: Read → Quiz Attempted (when review questions are accessed)
- Transition 3: Quiz Attempted → Quiz Completed (when all questions are answered)
- Transition 4: Read → Simulation Accessed (when simulation examples are used)
- Transition 5: Read → Chatbot Query Made (when chatbot is used for content)

## Data Validation Rules

### Content Integrity
- All module content must be valid Markdown
- All learning objectives must be specific and measurable
- All review questions must have valid answers
- Content references must point to existing modules/sections

### User Data Privacy
- Learner personal information must be encrypted
- Learning progress data must be associated only with authenticated users
- Chatbot queries must be anonymized when used for system improvement

### Citation Compliance
- All factual claims in content must have valid source references
- At least 50% of sources must be peer-reviewed
- All citations must follow APA format
- Source metadata must be preserved for verification