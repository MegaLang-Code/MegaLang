import sys

class MegaLang():
    def __init__(self):
        self.vars = {
            "TRUE": True,
            "FALSE": False
        }
        self.if_condition_met = True 
        self.inside_if_block = False

    def run_file(self, filename):
        try:
            with open(filename, "r") as file:
                for line in file:
                    clean_line = line.strip()
                    if clean_line:
                        self.run_command(clean_line)
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")

    def run_command(self, command):
        parts = command.split(" ", 1)
        cmd_type = parts[0]
        args = parts[1].strip() if len(parts) > 1 else ""

        if cmd_type == "EndIf":
            self.inside_if_block = False
            return

        if cmd_type == "CheckElse":
            self.CheckElse()
            return

        if cmd_type == "If":
            self.If(args)
            return

        if self.inside_if_block and not self.if_condition_met:
            return

        if cmd_type == "Speek":
            sub_parts = args.split(",", 1)
            txt = sub_parts[0].strip()
            sticky = sub_parts[1].strip() if len(sub_parts) > 1 else "\n"
            self.Speek(txt, sticky)

        elif cmd_type == "Ask":
            self.Ask(args)

        elif cmd_type == "MakeVar":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                self.MakeVar(sub_parts[0].strip(), sub_parts[1].strip())
            else:
                print("Syntax Error: MakeVar requires 'VarName, Value'")

        elif cmd_type == "SetExistVar":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                self.SetExistVar(sub_parts[0].strip(), sub_parts[1].strip())
            else:
                print("Syntax Error: SetExistVar requires 'VarName, Value'")

        elif cmd_type == "AskInputToVar":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                self.AskInputToVar(sub_parts[0].strip(), sub_parts[1].strip())
            else:
                print("Syntax Error: AskInputToVar requires 'Prompt Text, VarName'")
        
        elif cmd_type == "ADD":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                res = self.ADD(sub_parts[0].strip(), sub_parts[1].strip())
                if res is not None:
                    print(res)
            else:
                print("Syntax Error: ADD requires 'Num1, Num2'")
        else:
            print(f"Unknown Command Error: '{cmd_type}' is not recognized.")

    def If(self, condition_arg):
        self.inside_if_block = True
        condition_val = self.vars.get(condition_arg, False)
        if str(condition_val).upper() == "TRUE" or condition_val is True:
            self.if_condition_met = True
        else:
            self.if_condition_met = False

    def CheckElse(self):
        if not self.inside_if_block:
            print("Syntax Error: CheckElse without a preceding If block")
            return
        self.if_condition_met = not self.if_condition_met

    def Speek(self, TXT, Sticky):
        resolved_txt = self.vars.get(TXT, TXT)
        print(resolved_txt, end=Sticky, flush=True)

    def Ask(self, TXT):
        if TXT == "":
            print("Error: empty Ask string")
        else:
            input(TXT + " ")

    def MakeVar(self, VarName, Value):
        if VarName in ["TRUE", "FALSE"]:
            print("Cannot overwrite system constants")
            return
        self.vars[VarName] = Value

    def SetExistVar(self, VarName, NewValue):
        if VarName in ["TRUE", "FALSE"]:
            print("Cannot set TRUE or FALSE")
            return
        if VarName in self.vars:
            self.vars[VarName] = NewValue
        else:
            print(f"Error: Variable {VarName} does not exist.")

    def AskInputToVar(self, TXT, VarName):
        if TXT == "":
            print("Error: empty Ask string")
            return
        if VarName in ["TRUE", "FALSE"]:
            print("Cannot set TRUE or FALSE")
            return
        if VarName not in self.vars:
            print(f"Error: Variable {VarName} does not exist.")
            return
        
        userTXT = input(TXT + " ")
        self.vars[VarName] = userTXT

    def ADD(self, NUM, NUM2):
        try:
            val1 = self.vars.get(NUM, NUM)
            val2 = self.vars.get(NUM2, NUM2)
            return float(val1) + float(val2)
        except ValueError:
            print("TypeError: Arguments must be numbers or variables containing numbers.")
            return None

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE ERROR: You must provide a filename!")
        print("Example:MegaLang.exe script.mega")
        sys.exit(1)

    target_file = sys.argv[1]

    interpreter = MegaLang()
    print(f"--- Running {target_file} ---")
    interpreter.run_file(target_file)
