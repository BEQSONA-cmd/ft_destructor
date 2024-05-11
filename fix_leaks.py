import os
import time

RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[33m"
LIGHT_YELLOW = "\033[37m"
RESET = "\033[0m"


def usleep(mlsec):
    sec = mlsec / 1000000.0
    time.sleep(sec)

# function will return all .c files in the project
# except files in ./ft_destructor directory

def all_c_files():
    all_files = []
    for root, dirs, files in os.walk("."):
        if "./ft_destructor" in root or any("./ft_destructor" in d for d in dirs):
            continue
        for file in files:
            if not file.endswith('.c'):
                continue
            all_files.append(os.path.join(root, file))

    return all_files

# function will return all .h files in the project
# except files in ft_destructor folder

def all_h_files():
    all_files = []
    for root, dirs, files in os.walk("."):
        if "./ft_destructor" in root or any("./ft_destructor" in d for d in dirs):
            continue
        for file in files:
            if not file.endswith('.h'):
                continue
            all_files.append(os.path.join(root, file))

    return all_files

# if line starts with $(CC) in the end of the line add ./ft_destructor/ft_alloc.a
# for example:        $(CC) $(CFLAGS) $(OBJ) 
# should be:          $(CC) $(CFLAGS) $(OBJ) ./ft_destructor/ft_alloc.a

def add_library_in_makefile():
    i = 0
    library = "./ft_destructor/ft_alloc.a"
    makefile = "Makefile"
    # check if library is already added
    with open(makefile, "r") as file:
        lines = file.readlines()
        for line in lines:
            if library in line:
                return

    # add library in the end of the line
    with open(makefile, "r") as file:
        lines = file.readlines()
    with open(makefile, "w") as file:
        for line in lines:
            if line.startswith("\t$(CC)") and i == 0:
                line = line.strip() + " " + library + "\n"
                line = "\t" + line
                i += 1
            file.write(line)

header1 = '# include "./ft_destructor/ft_alloc.h"'
header2 = '# include "../ft_destructor/ft_alloc.h"'
header3 = '# include "../../ft_destructor/ft_alloc.h"'

# fuction will get number of / in the path
# and based on that will add the header
# for example: if path is ./header.h
# it will add # include "./ft_destructor/ft_alloc.h"
# if path is ./incl/minishell.h
# it will add # include "../ft_destructor/ft_alloc.h"
# if path have more than 3 / it will just skip it

def add_header_in_one_file(file_path):
    # check if header is already added
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            if header1 in line or header2 in line or header3 in line:
                return
    # count number of / in the path
    count_slash = file_path.count("/")
    if count_slash == 1:
        header = header1
    elif count_slash == 2:
        header = header2
    elif count_slash == 3:
        header = header3
    else:
        return
    # add header in the file
    i = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
    with open(file_path, "w") as file:
        for line in lines:
            if line.startswith("# include") or line.startswith("#include"):
                if i != 0:
                    file.write(line)
                else:
                    file.write(line)
                    file.write(header + "\n")
                    i += 1
            else:
                file.write(line)
        
# function will use add_header_in_one_file(file) for all h files

def add_header_in_h_files(h_files):
    # h_files may have only one string
    if isinstance(h_files, str):
        add_header_in_one_file(h_files)
        return
    for file in h_files:
        add_header_in_one_file(file)

# function will look all malloc functions in the file
# and will replace string malloc with ft_malloc
# if there is ft_malloc it will skip and continue to the next malloc

def add_ft_malloc_in_one_file(file_path):
    malloc = "malloc"
    ft_malloc = "ft_malloc"
    for line in open(file_path):
        if malloc in line and ft_malloc not in line:
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    file.write(line.replace(malloc, ft_malloc))
            break

# function will use add_ft_malloc_in_one_file(file) for all c files

def add_ft_malloc_in_c_files(c_files):
    # c_files may have only one string
    if isinstance(c_files, str):
        add_ft_malloc_in_one_file(c_files)
        return
    for file in c_files:
        add_ft_malloc_in_one_file(file)

# function will look all free functions in the file
# and will replace string free with ft_free
# if there is ft_free it will skip and continue to the next free

def add_ft_free_in_one_file(file_path):
    free = "free"
    ft_free = "ft_free"
    for line in open(file_path):
        if free in line and ft_free not in line:
            with open(file_path, "r") as file:
                lines = file.readlines()
            with open(file_path, "w") as file:
                for line in lines:
                    file.write(line.replace(free, ft_free))
            break

# function will use add_ft_free_in_one_file(file) for all c files

def add_ft_free_in_c_files(c_files):
    # c_files may have only one string
    if isinstance(c_files, str):
        add_ft_free_in_one_file(c_files)
        return
    for file in c_files:
        add_ft_free_in_one_file(file)

# function will find main function in the project
# and will return the path to the file

def find_main_c_files(c_files):
    i = 0
    main_files = []
    for file in c_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "main(" in line:
                    i += 1
                    main_files.append(file)
                    break
    if i > 1:
        input_file = 0
        while input_file <= 0 or input_file > len(main_files):
            print(f"{RED}There are more than one main functions in the project{RESET}")
            for i, file in enumerate(main_files):
                print(f"{RED}{i + 1}.{GREEN} {file}{RESET}")
            try:
                input_file = int(input(f"\n{BLUE}type the number of the main function you want to use: {RESET}"))
            except:
                input_file = 0
            if input_file > 0 and input_file <= len(main_files):
                return main_files[input_file - 1]
    elif i == 1:
        return main_files[0]
    else:
        print(f"{RED}There is no main function in the project{RESET}")
        return None

ft_alloc_init =  "\tft_alloc_init();"
ft_destructor =  "\tft_destructor();"

def put_functions(main_file):
    if main_file is None:
        return
    
    # check if functions are already there

    with open(main_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if ft_alloc_init in line or ft_destructor in line:
                return
    
    # add functions in the main function
    # we will add ft_alloc_init() in the beginning of the main function after {
    # and ft_destructor() in the end of the main function before return 0;

    i = 0
    ft_alloc = 0
    ft_destruct = 0
    count_brackets = 0
    with open(main_file, "r") as file:
        lines = file.readlines()
    with open(main_file, "w") as file:
        for line in lines:
            if "main(" in line:
                i += 1
            if i > 0 and "{" in line:
                count_brackets += 1
            if i > 0 and "{" in line and ft_alloc == 0:
                file.write(line)
                file.write(ft_alloc_init + "\n")
                ft_alloc = 1
            elif i > 0 and "return" in line:
                file.write(ft_destructor + "\n")
                file.write(line)
                ft_destruct = 1
            elif i > 0 and "}" in line and ft_destruct == 0:
                if count_brackets == 1:
                    file.write(ft_destructor + "\n")
                    file.write(line)
                    ft_destruct = 1
                else:
                    file.write(line)
                    count_brackets -= 1
            else:
                file.write(line)
                
def press_eter_to_continue(message):
    print(message)
    input(f"\n{BLUE}Press {RED}[Enter]{BLUE} to continue...{RESET}\n")

if __name__ == "__main__":
    h_files = all_h_files()
    c_files = all_c_files()
    add_library_in_makefile()
    press_eter_to_continue(f"{CYAN}ADDING LIBRARY IN {GREEN}(Makefile) {RESET}")
    add_header_in_h_files(h_files)
    press_eter_to_continue(f"{CYAN}ADDING HEADER IN {GREEN}(.h) {CYAN}FILES {RESET}")
    add_ft_malloc_in_c_files(c_files)
    press_eter_to_continue(f"{CYAN}REPLACING {LIGHT_YELLOW}malloc{YELLOW}() {CYAN}WITH {LIGHT_YELLOW}ft_malloc{YELLOW}() {RESET}")
    add_ft_free_in_c_files(c_files)
    press_eter_to_continue(f"{CYAN}REPLACING {LIGHT_YELLOW}free{YELLOW}() {CYAN}WITH {LIGHT_YELLOW}ft_free{YELLOW}() {RESET}")
    main_file = find_main_c_files(c_files)
    put_functions(main_file)
    press_eter_to_continue(f"{CYAN}ADDING {LIGHT_YELLOW}ft_alloc_init{YELLOW}() {CYAN}AND {LIGHT_YELLOW}ft_destructor{YELLOW}() {CYAN}IN {GREEN}(" + main_file +")")
    print(f"{GREEN}[All leaks are fixed]{RESET}")
