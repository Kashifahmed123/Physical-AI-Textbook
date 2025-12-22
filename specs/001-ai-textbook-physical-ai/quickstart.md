# Quickstart Guide: Physical AI & Humanoid Robotics Textbook

## Overview
This guide provides a quick introduction to the Physical AI & Humanoid Robotics textbook project. It covers the basic setup, architecture, and how to contribute to the content and features.

## Project Structure
```
book/
├── docs/                    # Markdown source files for textbook
│   ├── module-1-foundations/
│   ├── module-2-ros/
│   ├── module-3-simulations/
│   ├── module-4-nvidia-isaac/
│   ├── module-5-vla/
│   ├── module-6-locomotion/
│   ├── module-7-conversational/
│   └── module-8-capstone/
├── docusaurus.config.js     # Docusaurus configuration
├── package.json             # Dependencies for documentation site
├── src/
│   └── components/          # Custom React components for textbook features
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI application
│   │   ├── models/          # Data models
│   │   ├── routes/          # API endpoints
│   │   └── services/        # Business logic
│   └── requirements.txt     # Python dependencies
└── tests/                   # Test files for validation
```

## Prerequisites
- Node.js 18+ for Docusaurus
- Python 3.9+ for backend services
- Git for version control
- Basic knowledge of Markdown and Python

## Setting Up the Textbook Content

### 1. Clone the Repository
```bash
git clone <repository-url>
cd book
```

### 2. Install Docusaurus Dependencies
```bash
cd book
npm install
```

### 3. Run the Textbook Locally
```bash
npm start
```
This will start the development server and open the textbook in your browser at http://localhost:3000.

## Setting Up the Backend Services

### 1. Navigate to Backend Directory
```bash
cd backend
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables
Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key
QDRANT_URL=your_qdrant_cloud_url
QDRANT_API_KEY=your_qdrant_api_key
DATABASE_URL=your_postgres_connection_string
```

### 5. Run the Backend Server
```bash
uvicorn app.main:app --reload
```

## Contributing Content

### Adding a New Section to a Module
1. Navigate to the appropriate module directory in `docs/`
2. Create a new Markdown file with descriptive name
3. Follow the standard section template:
```markdown
---
title: Your Section Title
sidebar_position: X
---

# Your Section Title

## Learning Objectives

- Objective 1
- Objective 2

## Content

Your content here...

## Summary

Key takeaways from this section.

## Review Questions

1. Question 1?
2. Question 2?
```

### Adding Citations
All factual claims must have APA citations. Use this format:
```
According to Smith et al. (2023), Physical AI represents a significant advancement in robotics research.
```
And include the full citation in the References section of the module.

## Using the AI Features

### Chatbot Integration
The RAG chatbot is accessible on every page of the textbook. Users can:
- Ask questions about the current page content
- Select text and ask specific questions about it
- Receive answers sourced only from the textbook content

### Personalization
The system adapts content based on the learner's background (university student, software engineer, AI practitioner). When contributing content, consider how it might be adapted for different audiences.

### Translation
Use the translation button to convert content to Urdu. The system uses cached translations for efficiency.

## Validation and Quality Checks

### Running Content Validation
```bash
npm run validate-content
```
This checks for:
- Missing citations
- APA format compliance
- Readability metrics
- Link validation

### Running Backend Tests
```bash
cd backend
python -m pytest
```

## Deployment

### Building the Static Site
```bash
npm run build
```

### Deploying to GitHub Pages
The site is automatically deployed when changes are pushed to the main branch, provided all validation checks pass.

## Key Technologies

- **Frontend**: Docusaurus (React-based static site generator)
- **Backend**: FastAPI (Python web framework)
- **Vector Store**: Qdrant Cloud (for RAG chatbot)
- **Database**: Neon Serverless Postgres (for user data)
- **Authentication**: Better Auth (for user management)
- **Translation**: AI-powered translation services

## Troubleshooting

### Common Issues
- **Content not appearing**: Ensure the `sidebar_position` is set correctly in the Markdown frontmatter
- **Chatbot not responding**: Check that the backend server is running and API keys are configured
- **Translation not working**: Verify translation cache and API connectivity

### Getting Help
- Check the detailed documentation in the `/docs` directory
- Review the implementation plan in `specs/001-ai-textbook-physical-ai/plan.md`
- Consult the data models in `specs/001-ai-textbook-physical-ai/data-model.md`