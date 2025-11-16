import os
import uuid
from datetime import datetime
from config.settings import settings
import streamlit as st

def save_uploaded_file(uploaded_file):
    """Save uploaded file to uploads folder"""
    file_id = str(uuid.uuid4())
    file_extension = uploaded_file.name.split('.')[-1]
    file_path = os.path.join(settings.UPLOAD_FOLDER, f"{file_id}.{file_extension}")
    
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    return file_path

def save_note_content(content, filename=None):
    """Save generated notes to file"""
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"note_{timestamp}.md"
    
    file_path = os.path.join(settings.NOTES_FOLDER, filename)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    return file_path

def list_notes():
    """List all generated notes"""
    notes = []
    for filename in os.listdir(settings.NOTES_FOLDER):
        if filename.endswith(('.md', '.txt')):
            notes.append(filename)
    return sorted(notes, reverse=True)

def read_note_content(note_filename):
    """Read content of a note file"""
    file_path = os.path.join(settings.NOTES_FOLDER, note_filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def update_note_content(note_filename, new_content):
    """Update content of an existing note"""
    file_path = os.path.join(settings.NOTES_FOLDER, note_filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return file_path

def delete_note_file(note_filename):
    """Delete a note file"""
    file_path = os.path.join(settings.NOTES_FOLDER, note_filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return True
    return False