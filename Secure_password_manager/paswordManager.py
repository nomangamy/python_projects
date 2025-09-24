import tkinter as tk
from tkinter import messagebox

def add_Auth_Details():
    username = username_input.get()
    password = password_input.get()
    website_visited =website_input.get()
    if username and password and website_visited:
        with open("auth_bin.txt", "a") as file:
            file.write(f"{username} | {password} | {website_visited}\n")
            messagebox.showinfo("Success", "Backed up successfully!")

    else:
        messagebox.showwarning("Input Error", "Please fill in all fields.") 



def get_Auth_Details():
    username = username_input.get()

    password = {}
    try:
        with open("auth_bin.txt", "r") as file:
            for line in file : 
                if line.startswith(username):
                    messagebox.showinfo("Credentials Found", f"Credentials: {line.strip()}")
                    return password
                else:
                    messagebox.showwarning("Not Found", "No credentials found for the given username.")
                    return None
    except FileNotFoundError:
        messagebox.showerror("File Error", "No credentials stored yet.")
        return None


def get_Auth_List():
    try:
        with open("auth_bin.txt", "r") as file:
            auth_list = file.readlines()
            if auth_list:
                auth_str = "".join(auth_list)
                messagebox.showinfo("All Credentials", f"Credentials:\n{auth_str}")
            else:
                messagebox.showinfo("No Credentials", "No credentials stored yet.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "No credentials stored yet.")

def delete_Auth_Details():

    username =username_input.get()
    file = "auth_bin.txt"
    try:
        with open("auth_bin.txt", "r") as file:
            for line in file:
                if line.startswith(username):
                    lines =file.split(line)
                    if lines != username:
                        print(lines)
                        with open("auth_bin.txt", "w") as file:
                            file.writelines(lines)
                            messagebox.showinfo("Deleted", "Credentials deleted successfully.")
                            return
            messagebox.showwarning("Not Found", "No credentials found for the given username.")
    except FileNotFoundError:
        messagebox.showerror("File Error", "No credentials stored yet.")



if __name__ =="__main__":
    root = tk.Tk()
    root.title("Noman's Password Manager")
    root.geometry("400x300")

    tk.Label(root, text="Enter the Username:").pack(pady=5)
    username_input = tk.Entry(root)
    username_input.pack(pady=5)

    tk.Label(root, text="Kindly provide the Password:").pack(pady=5)
    password_input = tk.Entry(root, show="*")
    password_input.pack(pady=5)

    tk.Label(root, text="which Website did you visit?").pack(pady=5)
    website_input = tk.Entry(root)
    website_input.pack(pady=5)

    tk.Button(root, text="Add Auth Details", command=add_Auth_Details).pack(pady=5)
    tk.Button(root, text="Get Auth Details", command=get_Auth_Details).pack(pady=5)
    tk.Button(root, text="Get Auth List", command=get_Auth_List).pack(pady=5)
    tk.Button(root, text="Delete Auth Details", command=delete_Auth_Details).pack(pady=5)

    root.mainloop()