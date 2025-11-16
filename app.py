import streamlit as st
from agents.note_agent import generate_notes_from_topic, generate_notes_from_pdf
from utils.file_handler import save_uploaded_file, save_note_content, list_notes, read_note_content, update_note_content, delete_note_file
from utils.text_processor import extract_key_points, format_as_markdown, generate_summary
from config.settings import settings
import os
import tempfile
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Preformatted, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import io

st.set_page_config(
    page_title="Note Maker",
    page_icon="📝",
    layout="wide"
)

st.markdown("""
<style>
    /* Main background and container styling */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Header styling */
    .header {
        text-align: center;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 3rem;
        font-weight: bold;
        margin-bottom: 2rem;
        padding: 1rem;
        border-radius: 15px;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
    }
    
    /* Note container styling */
    .note-container {
        background: linear-gradient(145deg, #ffffff, #e6e6e6);
        padding: 25px;
        border-radius: 15px;
        border-left: 6px solid #667eea;
        box-shadow: 0 8px 32px rgba(31, 38, 135, 0.2);
        margin: 20px 0;
        backdrop-filter: blur(4px);
        -webkit-backdrop-filter: blur(4px);
    }
    
    /* Button styling */
    .stButton > button {
        border-radius: 25px;
        padding: 10px 20px;
        margin: 5px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    
    /* Download button */
    .stDownloadButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 20px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stDownloadButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.1);
        color: white;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div > select {
        color: white;
    }
    
    [data-testid="stSidebar"] .stSelectbox > div > div > select option {
        color: black;
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        border-radius: 10px 10px 0 0;
        background: rgba(255, 255, 255, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(255, 255, 255, 0.2);
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    
    .stTextArea > div > div > textarea {
        border-radius: 10px;
        border: 2px solid #667eea;
    }
    
    /* Markdown styling */
    .markdown-body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        line-height: 1.6;
    }
    
    .markdown-body h1, .markdown-body h2, .markdown-body h3 {
        color: #667eea;
        margin-top: 1.5em;
        margin-bottom: 0.5em;
    }
    
    .markdown-body ul, .markdown-body ol {
        padding-left: 2em;
    }
    
    .markdown-body code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    
    .markdown-body pre {
        background-color: #f4f4f4;
        padding: 1em;
        border-radius: 5px;
        overflow-x: auto;
    }
    
    /* Progress bar styling */
    .stProgress > div > div > div {
        background-color: #667eea;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Warning message styling */
    .stWarning {
        background: linear-gradient(45deg, #ff9800, #f57c00);
        color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Info message styling */
    .stInfo {
        background: linear-gradient(45deg, #2196F3, #0b7dda);
        color: white;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    
    /* Card-like containers */
    .card {
        background: white;
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    /* Footer styling */
    .footer {
        text-align: center;
        padding: 20px;
        color: #666;
        font-size: 0.9em;
        margin-top: 50px;
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .header {
            font-size: 2rem;
        }
        
        .note-container {
            padding: 15px;
        }
    }
</style>
""", unsafe_allow_html=True)

if 'current_note' not in st.session_state:
    st.session_state.current_note = ""
if 'current_filename' not in st.session_state:
    st.session_state.current_filename = ""
if 'editing' not in st.session_state:
    st.session_state.editing = False
if 'notes_list' not in st.session_state:
    st.session_state.notes_list = list_notes()
if 'delete_confirmation' not in st.session_state:
    st.session_state.delete_confirmation = {}

def clean_markdown_text(text):
    """Remove markdown formatting symbols to make text cleaner"""
    text = text.replace('**', '')

    text = text.replace('*', '')
    text = text.replace('`', '')
    text = text.replace('___', ' ')
    text = text.replace('__', ' ')
    text = text.replace('---', ' ')
    import re
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def markdown_to_pdf(markdown_text, filename):
    """Convert markdown text to PDF using reportlab (Unicode compatible) with cleaned formatting"""

    buffer = io.BytesIO()
    

    doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=0.5*inch, bottomMargin=0.5*inch)
    
  
    styles = getSampleStyleSheet()
    
    heading1_style = ParagraphStyle(
        'Heading1',
        parent=styles['Heading1'],
        fontSize=18,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=10,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    heading3_style = ParagraphStyle(
        'Heading3',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=8,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'Normal',
        parent=styles['Normal'],
        fontSize=12,
        spaceAfter=6,
        alignment=0
    )
    
    lines = markdown_text.split('\n')
    
    elements = []
    
    for line in lines:
        cleaned_line = clean_markdown_text(line)
        
        if line.startswith('# '):  
            elements.append(Paragraph(cleaned_line.replace('# ', ''), heading1_style))
        elif line.startswith('## '): 
            elements.append(Paragraph(cleaned_line.replace('## ', ''), heading2_style))
        elif line.startswith('### '):  
            elements.append(Paragraph(cleaned_line.replace('### ', ''), heading3_style))
        elif line.startswith('- ') or line.startswith('* '): 
    
            elements.append(Paragraph(f"• {cleaned_line[2:]}", normal_style))
        elif line.strip() == '': 
            elements.append(Spacer(1, 0.2*inch))
        else:  
            clean_text = cleaned_line.replace('<', '<').replace('>', '>')
            elements.append(Paragraph(clean_text, normal_style))
    
    doc.build(elements)
    
    pdf_data = buffer.getvalue()
    buffer.close()
    
    return pdf_data

def main():
    st.markdown('<div class="header">📝Notes Maker</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h3 style="color: #667eea; font-weight: bold;">
            Your Notes Creation Assistant
        </h3>
        <p style="color: #666; font-size: 1.1em;">
            Generate comprehensive notes from text prompts or PDF files using AI
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("### 🧭 Navigation")
        option = st.radio(
            "Choose an option:",
            ("📝 Create New Notes", "📚 View Existing Notes", "⚙️ Settings")
        )
        

        st.markdown("---")
        
        st.markdown("""
        <div style="color: white; font-size: 0.8em; opacity: 0.7; margin-top: 2rem;">
            Powered by AI<br>
            Made for learners and developers
        </div>
        """, unsafe_allow_html=True)
    
    if option == "📝 Create New Notes":
        create_notes_section()
    elif option == "📚 View Existing Notes":
        view_notes_section()
    elif option == "⚙️ Settings":
        settings_section()

def create_notes_section():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📝 Create New Notes")
    
    # Two options: Text input or File upload
    tab1, tab2 = st.tabs(["📝 Text Input", "📄 File Upload"])
    
    with tab1:
        st.subheader("Generate Notes from Text")
        col1, col2 = st.columns(2)
        
        with col1:
            topic = st.text_input("Enter topic for notes:", placeholder="e.g.,Functions", help="Enter the topic you want notes about")
        
        with col2:
            language = st.selectbox(
                "Select language/subject:",
                ["Python", "JavaScript", "Java", "C++", "HTML/CSS", "React", "Machine Learning", "Data Science", "Mathematics", "Physics", "Chemistry", "Biology", "History", "Geography", "Other"],
                help="Select the programming language or subject for your notes"
            )
        
        if st.button("✨ Generate Notes", key="generate_text", use_container_width=True):
            if topic and language:
                with st.spinner(f"🤖 Generating notes for {language} on '{topic}'..."):
                    notes = generate_notes_from_topic(topic, language)
                    st.session_state.current_note = notes
                    import datetime
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    st.session_state.current_filename = f"{language}_{topic.replace(' ', '_')}_{timestamp}.md"
                    
                    # Save note
                    file_path = save_note_content(notes, st.session_state.current_filename)
                    
                    st.success("✅ Notes generated successfully!")
                    
                    # Option to automatically download after generation
                    auto_download = st.checkbox("📥 Download notes automatically after generation", key="auto_download_text")
                    
                    if auto_download:
                        # Create PDF version for download
                        pdf_bytes = markdown_to_pdf(notes, st.session_state.current_filename.replace('.md', '.pdf'))
                        st.download_button(
                            label="📥 Download Generated Notes (PDF)",
                            data=pdf_bytes,
                            file_name=st.session_state.current_filename.replace('.md', '.pdf'),
                            mime="application/pdf",
                            key=f"auto_download_{st.session_state.current_filename}"
                        )
                    
                    display_note_options(notes, st.session_state.current_filename)
            else:
                st.warning("⚠️ Please enter both topic and select a language.")
    
    with tab2:
        st.subheader("Upload File for Note Generation")
        uploaded_file = st.file_uploader(
            "Choose a PDF file",
            type=['pdf'],
            help="Upload a PDF file to generate notes from its content"
        )
        
        if uploaded_file is not None:
            st.success(f"✅ File uploaded: {uploaded_file.name}")
            
            if st.button("🚀 Process File and Generate Notes", key="process_file", use_container_width=True):
                with st.spinner(f"🤖 Processing {uploaded_file.name} and generating notes..."):
                    # Save uploaded file
                    file_path = save_uploaded_file(uploaded_file)
                    
                    # Process PDF
                    with open(file_path, 'rb') as f:
                        import pdfplumber
                        content = ""
                        with pdfplumber.open(f) as pdf:
                            for page in pdf.pages:
                                text = page.extract_text()
                                if text:
                                    content += text + "\n"
                    
                    # Generate notes from PDF content
                    notes = generate_notes_from_pdf(content)
                    st.session_state.current_note = notes
                    import datetime
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    st.session_state.current_filename = f"PDF_Notes_{uploaded_file.name.replace('.pdf', '')}_{timestamp}.md"
                    
                    # Save note
                    note_file_path = save_note_content(notes, st.session_state.current_filename)
                    
                    st.success("✅ Notes generated from PDF successfully!")
                    
                    # Option to automatically download after PDF generation
                    auto_download = st.checkbox("📥 Download PDF notes automatically after generation", key="auto_download_pdf")
                    
                    if auto_download:
                        # Create PDF version for download
                        pdf_bytes = markdown_to_pdf(notes, st.session_state.current_filename.replace('.md', '.pdf'))
                        st.download_button(
                            label="📥 Download PDF Notes (PDF)",
                            data=pdf_bytes,
                            file_name=st.session_state.current_filename.replace('.md', '.pdf'),
                            mime="application/pdf",
                            key=f"auto_download_pdf_{st.session_state.current_filename}"
                        )
                    
                    display_note_options(notes, st.session_state.current_filename)
    
    st.markdown('</div>', unsafe_allow_html=True)

def view_notes_section():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("📚 View Existing Notes")
    
    # Refresh notes list
    st.session_state.notes_list = list_notes()
    
    if st.session_state.notes_list:
        selected_note = st.selectbox(
            "Select a note to view:",
            st.session_state.notes_list,
            help="Choose a note from your saved notes"
        )
        
        if selected_note:
            content = read_note_content(selected_note)
            st.session_state.current_note = content
            st.session_state.current_filename = selected_note
            
            st.markdown("### 📝 Note Content")
            
            # Display note in a styled container
            st.markdown('<div class="note-container markdown-body">', unsafe_allow_html=True)
            st.markdown(content)
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action buttons for existing note
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                # Download as PDF
                pdf_bytes = markdown_to_pdf(content, selected_note.replace('.md', '.pdf'))
                st.download_button(
                    label="📥 Download (PDF)",
                    data=pdf_bytes,
                    file_name=selected_note.replace('.md', '.pdf'),
                    mime="application/pdf",
                    key=f"download_pdf_view_{selected_note}",
                    use_container_width=True
                )
            
            with col2:
                # Download as Markdown
                st.download_button(
                    label="📄 Download (MD)",
                    data=content,
                    file_name=selected_note,
                    mime="text/markdown",
                    key=f"download_md_view_{selected_note}",
                    use_container_width=True
                )
            
            with col3:
                if st.button("✏️ Edit Note", key=f"edit_view_{selected_note}", use_container_width=True):
                    st.session_state.editing = True
                    st.session_state.current_note = content
                    st.session_state.current_filename = selected_note
            
            with col4:
                # Delete button with confirmation
                delete_key = f"delete_{selected_note}"
                confirm_key = f"confirm_delete_{selected_note}"
                
                if st.button("🗑️ Delete Note", key=delete_key, type="secondary", use_container_width=True):
                    st.session_state.delete_confirmation[selected_note] = True
                
                if st.session_state.delete_confirmation.get(selected_note, False):
                    st.warning(f"⚠️ Are you sure you want to delete '{selected_note}'?")
                    col_confirm1, col_confirm2 = st.columns(2)
                    with col_confirm1:
                        if st.button("✅ Confirm Delete", key=confirm_key, type="primary", use_container_width=True):
                            if delete_note_file(selected_note):
                                st.success(f"✅ Note '{selected_note}' deleted successfully!")
                                st.session_state.delete_confirmation[selected_note] = False
                                # Refresh the notes list
                                st.session_state.notes_list = list_notes()
                                st.rerun()
                            else:
                                st.error(f"❌ Failed to delete note '{selected_note}'")
                                st.session_state.delete_confirmation[selected_note] = False
                    with col_confirm2:
                        if st.button("❌ Cancel", key=f"cancel_delete_{selected_note}", use_container_width=True):
                            st.session_state.delete_confirmation[selected_note] = False
                            st.rerun()
            
            # Edit mode
            if st.session_state.editing and st.session_state.current_filename == selected_note:
                st.markdown("### ✏️ Edit Note")
                edited_content = st.text_area(
                    "Edit your note:",
                    value=st.session_state.current_note,
                    height=400
                )
                
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("💾 Save Changes", use_container_width=True):
                        update_note_content(st.session_state.current_filename, edited_content)
                        st.session_state.current_note = edited_content
                        st.session_state.editing = False
                        st.success("✅ Changes saved successfully!")
                        st.rerun()
                
                with col2:
                    if st.button("❌ Cancel Edit", use_container_width=True):
                        st.session_state.editing = False
                        st.rerun()
    else:
        st.info("📚 No notes found. Create some notes first!")
    
    st.markdown('</div>', unsafe_allow_html=True)

def settings_section():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.header("⚙️ Settings")
    
    st.subheader("Current Configuration")
    st.write(f"**Provider:** Google Gemini (Free)")
    st.write("**Model:** Automatically selected")
    
    st.subheader("API Configuration")
    if settings.GOOGLE_API_KEY:
        st.info(f"✅ Using Google API key (first 6 chars): {settings.GOOGLE_API_KEY[:6]}...")
    else:
        st.error("❌ Google API Key not found!")
    
    st.subheader("About This App")
    st.markdown("""
    **Smart Note Maker** is an AI-powered note creation assistant that helps you:
    - Generate comprehensive notes from text prompts
    - Convert PDF files into structured notes
    - Download notes in PDF or Markdown format
    - Edit and manage your saved notes
    - All for free using Google's AI technology
    """)
    
    st.markdown('</div>', unsafe_allow_html=True)

def display_note_options(content, filename):
    """Display note content with download and edit options"""
    
    st.markdown("### 📝 Generated Notes")
    
    # Display note in a styled container
    st.markdown('<div class="note-container markdown-body">', unsafe_allow_html=True)
    st.markdown(content)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Action buttons
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Download as PDF (cleaned)
        pdf_bytes = markdown_to_pdf(content, filename.replace('.md', '.pdf'))
        st.download_button(
            label="📥 Download Note (PDF)",
            data=pdf_bytes,
            file_name=filename.replace('.md', '.pdf'),
            mime="application/pdf",
            key=f"download_pdf_{filename}",
            use_container_width=True
        )
    
    with col2:
        # Download as Markdown
        st.download_button(
            label="📄 Download Note (MD)",
            data=content,
            file_name=filename,
            mime="text/markdown",
            key=f"download_md_{filename}",
            use_container_width=True
        )
    
    with col3:
        if st.button("✏️ Edit Note", key=f"edit_{filename}", use_container_width=True):
            st.session_state.editing = True
            st.session_state.current_note = content
            st.session_state.current_filename = filename
    
    # Edit mode
    if st.session_state.editing:
        st.markdown("### ✏️ Edit Note")
        edited_content = st.text_area(
            "Edit your note:",
            value=st.session_state.current_note,
            height=400
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("💾 Save Changes", use_container_width=True):
                update_note_content(st.session_state.current_filename, edited_content)
                st.session_state.current_note = edited_content
                st.session_state.editing = False
                st.success("✅ Changes saved successfully!")
        
        with col2:
            if st.button("❌ Cancel Edit", use_container_width=True):
                st.session_state.editing = False
                st.rerun()

if __name__ == "__main__":
    main()