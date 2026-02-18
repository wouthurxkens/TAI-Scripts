import os
from tivars.types import TIProgram

# Ensure bin directory exists
os.makedirs("bin", exist_ok=True)

for filename in os.listdir("src"):
    if filename.endswith(".txt"):
        src_path = os.path.join("src", filename)
        
        # TI names must be uppercase and max 8 characters
        ti_name = os.path.splitext(filename)[0][:8].upper()
        dest_path = os.path.join("bin", f"{ti_name}.8xp")
        
        with open(src_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Create TI Program from string
        my_program = TIProgram(content, name=ti_name)
        my_program.save(dest_path)
        print(f"Converted: {filename} -> {dest_path}")
