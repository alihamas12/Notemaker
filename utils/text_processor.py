def extract_key_points(text, max_points=10):
    """Extract key points from text"""
    lines = text.split('\n')
    key_points = []
    
    for line in lines:
        line = line.strip()
        if line.startswith(('#', '##', '###', '- ', '* ', '1. ', '2. ')):
            if len(key_points) < max_points:
                key_points.append(line)
    
    return '\n'.join(key_points)

def format_as_markdown(content):
    """Format content as markdown"""

    formatted = content.replace('\n\n', '\n\n')
    return formatted

def generate_summary(text, max_length=500):
    """Generate a summary of the text"""
    words = text.split()
    if len(words) > max_length:
        return ' '.join(words[:max_length]) + '...'
    return text