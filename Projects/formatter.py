import re
import pyperclip  # For clipboard functionality

def format_levels(text):
    # Split the text into levels
    levels = re.split(r'(.+?: Level \d+)', text)
    levels = [level.strip() for level in levels if level.strip()]
    
    formatted_output = []
    
    # Process each level
    for i in range(0, len(levels), 2):
        if i+1 >= len(levels):
            break
            
        level_header = levels[i]
        level_content = levels[i+1]
        
        # Clean up the content
        # Remove extra newlines and spaces
        cleaned_content = ' '.join(line.strip() for line in level_content.split('\n') if line.strip())
        # Join sentences without spaces before periods
        cleaned_content = cleaned_content.replace(' .', '.').replace(' ,', ',')
        
        # Format as a box
        box = f"**{level_header}**\n```\n{cleaned_content}\n```"
        formatted_output.append(box)
    
    # Join all boxes with double newlines
    final_output = '\n\n'.join(formatted_output)
    
    # Copy to clipboard
    pyperclip.copy(final_output)
    print("Formatted text has been copied to your clipboard!")
    print("\nHere's the output preview:\n")
    print(final_output)

# Example usage:
input_text = """Threat intelligence: Level 2
Contributes to routine threat intelligence gathering tasks.

Monitors and detects potential security threats and escalates in accordance with relevant procedures and standards.

Threat intelligence: Level 3
Performs routine threat intelligence gathering tasks.

Transforms collected information into a data format that can be used for operational security activities.

Cleans and converts quantitative information into consistent formats."""

format_levels(input_text)