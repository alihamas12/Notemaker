from langchain.agents import AgentType, initialize_agent, Tool
from langchain.memory import ConversationBufferMemory
from tools.note_generator import NoteGeneratorTool
from config.settings import settings

# Import Google Gemini only
from langchain_google_genai import ChatGoogleGenerativeAI
from google.generativeai import list_models
import google.generativeai as genai

def get_available_models():
    """Get available models in the Google AI Studio project"""
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    models = []
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            models.append(model.name)
    return models

def get_llm():
    """Get Google Gemini LLM with the most suitable available model"""
    genai.configure(api_key=settings.GOOGLE_API_KEY)
    
    # Get available models
    available_models = get_available_models()
    
    # Look for free models in order of preference
    preferred_models = [
        "models/gemini-2.5-flash",  # Most recent free model
        "models/gemini-1.0-pro",    # Older free model
        "models/gemini-pro"         # Older free model
    ]
    
    # Find the first available preferred model
    model_to_use = None
    for preferred_model in preferred_models:
        if preferred_model in available_models:
            model_to_use = preferred_model
            break
    
    # If none of the preferred models are available, use the first available one
    if model_to_use is None and available_models:
        model_to_use = available_models[0]
        print(f"Using available model: {model_to_use}")
    elif model_to_use is None:
        raise ValueError("No suitable models found for generateContent in your Google AI Studio project")
    
    print(f"Using model: {model_to_use}")
    
    return ChatGoogleGenerativeAI(
        google_api_key=settings.GOOGLE_API_KEY,
        model=model_to_use,
        temperature=0.7  # Good for note generation
    )

def create_note_agent():
    """Create the note-taking agent"""
    
    # Initialize LLM
    llm = get_llm()
    
    # Create tools
    tools = [
        Tool(
            name="note_generator",
            func=lambda x: f"Generating notes for: {x}",
            description="Use this to generate comprehensive notes for any programming language or subject"
        ),
        Tool(
            name="pdf_processor",
            func=lambda x: f"Processing PDF: {x}",
            description="Use this to process PDF files and extract content for note generation"
        )
    ]
    
    # Add custom tools
    tools.append(NoteGeneratorTool())
    
    # Initialize memory
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    
    # Create agent
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True,
        memory=memory,
        handle_parsing_errors=True
    )
    
    return agent

def generate_notes_from_topic(topic, language):
    """Generate comprehensive notes for a specific topic and language"""
    
    llm = get_llm()
    
    prompt = f"""
    Create comprehensive notes for {language} covering the topic: {topic}.
    Include:
    - Introduction and basic concepts
    - Syntax and structure
    - Key features and functionality
    - Code examples
    - Best practices
    - Common pitfalls and solutions
    - Advanced topics
    - Summary and next steps
    
    Format the notes in markdown with proper headings and structure.
    """
    
    response = llm.invoke(prompt)
    return response.content

def generate_notes_from_pdf(pdf_content, topic=None):
    """Generate notes from PDF content"""
    
    llm = get_llm()
    
    prompt = f"""
    Create comprehensive notes from the following PDF content:
    {pdf_content}
    
    If a specific topic is mentioned, focus on that topic. Otherwise, create general notes covering the main concepts.
    Include:
    - Main concepts and theories
    - Key definitions
    - Important examples
    - Summary of each section
    - Key takeaways
    
    Format the notes in markdown with proper headings and structure.
    """
    
    response = llm.invoke(prompt)
    return response.content