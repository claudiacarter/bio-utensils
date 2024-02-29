with open(r"FILE-PATH-TO-FASTA", "r") as fasta:
    total_fasta = fasta.readlines()

    #check if file is a fasta
    isfasta = False
    deflines = total_fasta[::2]

    if all(">" in item for item in deflines):
        isfasta = True

    if isfasta == False:
        print("ERROR: Input file does not seem to be a FASTA.")
        exit()

    #set how many sequences you want per file, lines will be double this in FASTA format
    seqs_per_file = input(f"You must choose the number of sequences you would like in each file. If the number of \nsequences in the input file is not divisible by this number, the final file will contain \nfewer.\n\nEnter input here: ")
    while seqs_per_file.isnumeric() == False :
        seqs_per_file = input(f"\nInvalid input. Please enter an integer ONLY and hit Enter. Fastasplitter will split your\ninput FASTA into smaller files with this many sequences or less.\n\nEnter number here: ")
    while int(seqs_per_file) > len(deflines):
        seqs_per_file = input(f"You have requested more sequences per file than exist in the input file, please check \ninput and retry.\n\nEnter number here: ")
    lines_per_file = 2*seqs_per_file
    
    new_file_num = 0
    current_file = []
    count = 0
    while bool(total_fasta):
        for line in total_fasta:
            current_file.append(line)
            count += 1
            if count >= lines_per_file:
                break
        with open(f"fastasplit_{new_file_num}.fa", "w") as file:
             for line in current_file:
                 file.write(line)
             new_file_num += 1
        total_fasta = [line for line in total_fasta if line not in current_file]
        current_file = []
        count = 0

print(f"Split input FASTA to create {new_file_num} FASTAs, each contain {seqs_per_file} sequences or less.")
