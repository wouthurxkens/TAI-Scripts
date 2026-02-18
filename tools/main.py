import sys
import argparse
import os
from compiler import Compiler

def main():
    parser = argparse.ArgumentParser(
        description="TI-BASIC Compiler",
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    # Make filename optional (nargs='?') so '-a' can be run without it
    parser.add_argument("filename", nargs='?', help="Input file (required unless -a is used)")
    # Add action="store_true" so it behaves as a flag
    parser.add_argument("-a", "--all", action="store_true", help="Compile all .txt files in src/ and place .8xp in bin/")
    parser.add_argument("-d", "--decompile", action="store_true", help="Decompile")
    parser.add_argument("-o", "--output", help="Output file")
    
    args = parser.parse_args()
    compiler = Compiler()

    # --- BATCH COMPILATION MODE ---
    if args.all:
        src_dir = "src"
        bin_dir = "bin"
        
        if not os.path.exists(src_dir):
            print(f"Error: Source directory '{src_dir}' not found.")
            sys.exit(1)
            
        # Ensure the bin directory exists, create it if it doesn't
        os.makedirs(bin_dir, exist_ok=True)
        
        success_count = 0
        for file in os.listdir(src_dir):
            if file.endswith(".txt"):
                in_file = os.path.join(src_dir, file)
                base, _ = os.path.splitext(file)
                out_file = os.path.join(bin_dir, base + ".8xp")
                
                print(f"Compiling {in_file} -> {out_file}...")
                res = compiler.compile(in_file, out_file)
                
                if not res:
                    print(f"Error: Compilation failed for {in_file}.")
                else:
                    success_count += 1
                    
        print(f"Info: Successfully compiled {success_count} files in batch mode.")
        sys.exit(0)

    # --- SINGLE FILE MODE ---
    # If not using -a, a filename must be provided
    if not args.filename:
        parser.error("the following arguments are required: filename (unless -a is used)")

    in_file = args.filename
    out_file = args.output
    b_decompile = args.decompile
    
    # Automatic renaming logic
    if not out_file:
        base, _ = os.path.splitext(in_file)
        out_file = base + (".tib" if b_decompile else ".8xp")
        
    # Run based on mode
    if b_decompile:
        res = compiler.decompile(in_file, out_file)
    else:
        res = compiler.compile(in_file, out_file)
        
    if not res:
        print("Error: Compilation failed.")
        sys.exit(1)
        
    print(f"Info: Successfully {'decompiled' if b_decompile else 'compiled'} {in_file} -> {out_file}")

if __name__ == "__main__":
    main()