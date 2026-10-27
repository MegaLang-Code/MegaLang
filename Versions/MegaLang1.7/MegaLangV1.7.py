import sys
import gc

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
                    if clean_line and not clean_line.startswith("#"):
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
            if len(sub_parts) > 1:
                sticky = sub_parts[1].strip().replace("\\n", "\n").replace("\\t", "\t")
            else:
                sticky = "\n"
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

        elif cmd_type == "SUB":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                res = self.SUB(sub_parts[0].strip(), sub_parts[1].strip())
                if res is not None:
                    print(res)
            else:
                print("Syntax Error: SUB requires 'Num1, Num2'")
    
        elif cmd_type == "DIV":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                res = self.DIV(sub_parts[0].strip(), sub_parts[1].strip())
                if res is not None:
                    print(res)
            else:
                print("Syntax Error: DIV requires 'Num1, Num2'")

        elif cmd_type == "MULTI":
            sub_parts = args.split(",", 1)
            if len(sub_parts) == 2:
                res = self.MULTI(sub_parts[0].strip(), sub_parts[1].strip())
                if res is not None:
                    print(res)
            else:
                print("Syntax Error: MULTI requires 'Num1, Num2'")

        elif cmd_type == "AutoVarClean":
            self.AutoVarClean(args)

        elif cmd_type == "VarMemClean":
            self.VarMemClean()

        elif cmd_type == "DelVar":
            self.DelVar(args)
            print(args)

        elif cmd_type == "StartServerDev":
            self.StartServerDev(args)

        elif cmd_type == "StartServerProduct":
            self.StartServerProduct(args)

        elif cmd_type == "exit":
            sys.exit(1)

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
        sticky_lookup = str(Sticky).strip().upper()
        resolved_sticky = self.vars.get(sticky_lookup, Sticky)
        if resolved_sticky is True:
            end_char = ""
        elif resolved_sticky is False:
            end_char = "\n"
        else:
            end_char = Sticky
        print(resolved_txt, end=end_char, flush=True)

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

    def SUB(self, NUM, NUM2):
        try:
            val1 = self.vars.get(NUM, NUM)
            val2 = self.vars.get(NUM2, NUM2)
            return float(val1) - float(val2)
        except ValueError:
            print("TypeError: Arguments must be numbers or variables containing numbers.")
            return None

    def DIV(self, NUM, NUM2):
        try:
            val1 = self.vars.get(NUM, NUM)
            val2 = self.vars.get(NUM2, NUM2)
            return float(val1) / float(val2)
        except ValueError:
            print("TypeError: Arguments must be numbers or variables containing numbers.")
            return None

    def MULTI(self, NUM, NUM2):
        try:
            val1 = self.vars.get(NUM, NUM)
            val2 = self.vars.get(NUM2, NUM2)
            return float(val1) * float(val2)
        except ValueError:
            print("TypeError: Arguments must be numbers or variables containing numbers.")
            return None

    def AutoVarClean(self, State):
        if State == "Off":
            gc.disable()
        if State == "On":
            gc.enable()
    
    def VarMemClean(self):
        gc.collect()

    def DelVar(self, VarName):
        if VarName in ["TRUE", "FALSE"]:
            print("Cannot overwrite system constants")
            return
        if VarName in self.vars:
            del self.vars[VarName]
        else:
            print(f"Error: Variable '{VarName}' does not exist.")

    def StartServerDev(self, port):
        if port == str(port).strip():
            print("Error value not allowed.")
            exit()
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        server_address = ('127.0.0.1', int(port)) 
        try:
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f'Serving on "http://localhost:{port}/"')
            print("press CTRL + C to stop server")
            httpd.serve_forever()
        except OSError:
            print(f"Network Error: Port {port} is already taken or restricted!")
        except KeyboardInterrupt:
            print("\n")

    def StartServerProduct(self, port):
        if port == str(port).strip():
            print("Error value not allowed.")
            exit()
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        import socket
        try:
            temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            temp_socket.connect(("8.8.8.8", 80))
            local_ip = temp_socket.getsockname()[0]
            temp_socket.close()
        except Exception:
            local_ip = "127.0.0.1"
        server_address = ('0.0.0.0', int(port)) 
        try:
            httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
            print(f'[+] Server started.')
            print(f'[*] Local access:  http://localhost:{port}/')
            print(f'[*] LAN access: http://{local_ip}:{port}/')
            print("press CTRL + C to stop server")
            httpd.serve_forever()
        except OSError:
            print(f"[-]Network Error: Port {port} is already taken or restricted.")
        except KeyboardInterrupt:
            print("\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        import MegaLangREPL
    else:
        target_file = sys.argv[1]
        interpreter = MegaLang()
        print(f"interpreting: {target_file}")
        interpreter.run_file(target_file)
