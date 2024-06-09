import tkinter as tk
import wmi
import cpuinfo

def get_processor_info():
    info = cpuinfo.get_cpu_info()
    return info['brand_raw']

def get_os_info():
    computer = wmi.WMI()
    os_info = computer.Win32_OperatingSystem()[0]
    return f"OS Name: {os_info.Name.split('|')[0]}"

def get_cpu_info():
    computer = wmi.WMI()
    cpu_info = computer.Win32_Processor()[0]
    return f"CPU: {cpu_info.Name}"

def get_gpu_info():
    computer = wmi.WMI()
    gpu_info = computer.Win32_VideoController()[0]
    return f"GPU: {gpu_info.Name}"

def get_ram_info():
    computer = wmi.WMI()
    ram_info = computer.Win32_ComputerSystem()[0]
    ram_gb = round((float(ram_info.TotalPhysicalMemory) / (1024 ** 3)), 2)
    return f"RAM: {ram_gb} GB"

def close_app(event):
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("System Information")
    root.geometry("400x300")

    os_info = get_os_info()
    cpu_info = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_info = get_ram_info()

    info_label = tk.Label(root, text=f"System Information:\n\n{os_info}\n\nComponents info:\n{cpu_info}\n{gpu_info}\n{ram_info}", justify=tk.LEFT)
    info_label.pack(padx=10, pady=10)

    # Associazione dell'evento di pressione del tasto 'q' alla funzione close_app
    root.bind('<q>', close_app)

    root.mainloop()
