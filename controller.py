import re, psutil, hashlib
def reader():
    global white_list, Black_list, hash_pin_code, mode, pin_symb
    try:
        with open("tet.txt", "r", encoding='utf-8') as file:
            new_file = file.read().split("\n")
            new_fil = []
            for lst in new_file:
                new_fil.append(lst.split(":"))
            new_file = []
            for j in range(len(new_fil)):
                new_file.append([])
                for i in range(0, len(new_fil[j])):
                    new_file[j].append(new_fil[j][i].split(","))
            white_list = new_file[0][1]
            Black_list = new_file[1][1]
            hash_pin_code = new_file[2][1][0]
            mode = new_file[4][1][0]
            if new_file[3][1][0] == "BL":
                pin_symb = "🔒"
            else:
                pin_symb = "🔓"
            return white_list, Black_list, hash_pin_code, mode, pin_symb
    except:
        print("Файл повреждён")
        return False
def writer(mode, pin_code):
    global white_list, Black_list, hash_pin_code, pin_symb
    print(pin_code)
    with open("tet.txt", "w", encoding = "utf-8") as file:
        wl_st = lp_st = ""
        for string in white_list:
            wl_st+= string + ","
        for string in Black_list:
            lp_st+= string + ","
        if pin_symb == "🔒":
            pm = "BL"
        else:
            pm = "UNBL"

        hash_object = hashlib.sha256(pin_code.encode())
        pc = hash_object.hexdigest()
        file.write(f"WL:{wl_st[:len(wl_st)-1:]}\n"
                   f"BL:{lp_st[:len(lp_st)-1:]}\n"
                   f"PC:{pc}\n"
                   f"PM:{pm}\n"
                   f"WM:{mode}\n")
def normalize(name):
    name = name.lower().strip()
    name = re.sub(r'\.(exe|app|msi|bat|cmd)$', '', name)
    name = re.sub(r'[^a-z0-9]', '', name)
    return name


def find_process(app_name):
    normal_app_name = normalize(app_name)

    for proc in psutil.process_iter(['name']):
        try:
            proc_name = proc.info['name']
            normal_proc = normalize(proc_name)
            if (normal_app_name == normal_proc or
                    normal_app_name in normal_proc or
                    normal_proc in normal_app_name):
                return proc_name
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return False