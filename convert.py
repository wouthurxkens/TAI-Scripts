import os
from tivars.types import TIProgram

def main():
    src_dir = "src"
    bin_dir = "bin"

    if not os.path.exists(bin_dir):
        os.makedirs(bin_dir)

    for filename in os.listdir(src_dir):
        if filename.endswith(".txt"):
            src_path = os.path.join(src_dir, filename)
            
            # TI-83/84 names: Max 8 chars, uppercase, must start with letter
            ti_name = os.path.splitext(filename)[0]
            ti_name = "".join(filter(str.isalnum, ti_name))[:8].upper()
            
            if not ti_name[0].isalpha():
                ti_name = "A" + ti_name[1:8]

            dest_path = os.path.join(bin_dir, f"{ti_name}.8xp")

            with open(src_path, 'r', encoding='utf-8') as f:
                content = f.read()

            try:
                # TIProgram constructor tokenizes the string automatically
                prog = TIProgram(content, name=ti_name)
                prog.save(dest_path)
                print(f"Success: {filename} -> {dest_path}")
            except Exception as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    main()
