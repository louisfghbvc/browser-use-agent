# browser-use-agent
An intelligent agent system based on browser automation

## Project Overview
This is an intelligent agent system developed using the LangChain framework, capable of executing various tasks through browser interfaces and supporting multiple large language models.

## Features
- OpenAI API interface support
- DeepSeek-V3 model integration
- Browser automation capabilities
- Intelligent task processing

## Requirements
- Python 3.8+
- See requirements.txt for package dependencies

## Installation

### 1. Install Required Packages
```bash
pip install langchain-openai python-dotenv
```

### 2. Environment Variables Setup
Create a `.env` file in the project root directory and set the following variables:
```plaintext
OPENAI_BASE_URL=your_api_base_url
OPENAI_API_KEY=your_api_key
```

## Usage

### Basic Testing
Run the following command to test if the LLM is working properly:
```bash
python agent.py
```

### Agent Usage
Set your task in `agent.py`:
```python
agent = Agent(
    task="your_task_description",
    llm=llm,
)
```

## Important Notes
- Ensure all environment variables are properly configured
- Keep your API keys secure and never commit them to version control
- Run the test program first to verify your environment setup

## Troubleshooting
1. API Connection Issues
   - Verify environment variable settings
   - Check network connectivity
   - Validate API key validity

2. Browser-related Issues
   - Ensure browser driver versions are compatible
   - Verify browser settings are correct

## Development
- Issues and Pull Requests are welcome
- Follow PEP 8 coding style guidelines
- Include test cases for new features

## License
This project is licensed under the MIT License - see the LICENSE file for details
