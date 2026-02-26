import socket
import threading
import json
import queue
import time
import tkinter as tk
from tkinter import scrolledtext, font

HOST = '10.101.211.49'
PORT = 50007

# Updated palette to match the dark theme screenshot
PALETTE = {
    'bg': '#111214',           # Main dark background
    'top': '#1e1f22',          # Darker top bar
    'input_bg': '#383a40',     # Discord-like input field background
    'bubble_me': '#5865F2',    # Blue bubble for self
    'text': '#dbdee1',         # Light gray for standard text
    'muted': '#80848e'         # Muted gray for timestamps and names
}

class ChatClientUI:
    def __init__(self, master):
        self.master = master
        master.title('Dark Chat')
        master.configure(bg=PALETTE['bg'])
        master.geometry('700x550')

        # Clean, sans-serif fonts
        self.f_title = font.Font(family='Segoe UI', size=13, weight='bold')
        self.f_name = font.Font(family='Segoe UI', size=10, weight='bold')
        self.f_msg = font.Font(family='Segoe UI', size=11)
        self.f_time = font.Font(family='Segoe UI', size=9)

        # 1. Pack Top bar first
        self.topbar = tk.Frame(master, bg=PALETTE['top'], height=50)
        self.topbar.pack(fill='x', side='top')
        self.topbar.pack_propagate(False) # Keep height fixed
        
        self.title_lbl = tk.Label(self.topbar, text='Chat', bg=PALETTE['top'], fg='white', font=self.f_title)
        self.title_lbl.pack(side='left', padx=15)

        self.name_var = tk.StringVar(value='MyUser')
        self.name_entry = tk.Entry(self.topbar, textvariable=self.name_var, width=15, 
                                   bg=PALETTE['input_bg'], fg='white', bd=0, 
                                   insertbackground='white', font=self.f_name, justify='center')
        self.name_entry.pack(side='right', padx=15, ipady=6, ipadx=5)

        # 2. Pack Input area SECOND (at the bottom) so it doesn't get pushed off-screen
        self.input_frame = tk.Frame(master, bg=PALETTE['bg'])
        self.input_frame.pack(fill='x', side='bottom', padx=15, pady=15)
        
        self.entry = tk.Entry(self.input_frame, font=self.f_msg, bg=PALETTE['input_bg'], 
                              fg='white', insertbackground='white', bd=0, highlightthickness=0)
        self.entry.pack(side='left', fill='x', expand=True, ipady=12, ipadx=15)
        self.entry.bind('<Return>', self.on_send)
        
        self.send_btn = tk.Button(self.input_frame, text='Send', command=self.on_send, 
                                  bg=PALETTE['bubble_me'], fg='white', font=self.f_name, bd=0, 
                                  activebackground='#4752c4', activeforeground='white', cursor='hand2')
        self.send_btn.pack(side='right', padx=(10, 0), ipady=10, ipadx=20)

        # 3. Pack Main messages area LAST so it fills the remaining middle space
        self.container = tk.Frame(master, bg=PALETTE['bg'])
        self.container.pack(fill='both', expand=True)

        self.text = scrolledtext.ScrolledText(self.container, state='disabled', wrap='word', 
                                              bg=PALETTE['bg'], fg=PALETTE['text'], bd=0, 
                                              highlightthickness=0, font=self.f_msg, 
                                              pady=15, padx=10)
        self.text.pack(fill='both', expand=True)
        
        # Tag Configurations
        self.text.tag_configure('me', justify='right', foreground='white', background=PALETTE['bubble_me'], 
                                rmargin=15, spacing1=3, spacing3=3)
        self.text.tag_configure('other', justify='left', foreground=PALETTE['text'], 
                                lmargin1=15, lmargin2=15, spacing1=2, spacing3=8)
        self.text.tag_configure('other_name', justify='left', foreground=PALETTE['muted'], 
                                font=self.f_name, lmargin1=15, spacing1=12)
        self.text.tag_configure('timestamp', justify='center', foreground=PALETTE['muted'], 
                                font=self.f_time, spacing1=20, spacing3=10)
        self.text.tag_configure('system', justify='center', foreground=PALETTE['muted'], 
                                font=self.f_time, spacing1=10, spacing3=10)

        # Networking & State
        self.last_time = ""
        self.sock = None
        self.recv_thread = None
        self.running = True
        self.msg_queue = queue.Queue()

        self.master.protocol('WM_DELETE_WINDOW', self.on_close)
        self.connect()
        self.master.after(100, self.process_queue)

    def connect(self):
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((HOST, PORT))
            self.recv_thread = threading.Thread(target=self.recv_loop, daemon=True)
            self.recv_thread.start()
        except Exception as e:
            self.append_system(f'Could not connect: {e}')

    def recv_loop(self):
        buf = b''
        try:
            while self.running:
                data = self.sock.recv(4096)
                if not data:
                    self.msg_queue.put({'type':'system', 'text':'Server closed connection'})
                    break
                buf += data
                while b'\n' in buf:
                    line, buf = buf.split(b'\n', 1)
                    if not line:
                        continue
                    try:
                        obj = json.loads(line.decode('utf-8'))
                    except Exception:
                        obj = {'type':'message', 'name':'', 'text': line.decode('utf-8', errors='ignore'), 'time': time.strftime('%Y-%m-%d %H:%M:%S')}
                    self.msg_queue.put(obj)
        except Exception:
            self.msg_queue.put({'type':'system', 'text':'Connection error'})

    def process_queue(self):
        while not self.msg_queue.empty():
            obj = self.msg_queue.get()
            if obj.get('type') == 'history':
                for item in obj.get('items', []):
                    self.display_message(item)
            elif obj.get('type') == 'message':
                self.display_message(obj)
            elif obj.get('type') == 'system':
                self.append_system(obj.get('text'))
        if self.running:
            self.master.after(100, self.process_queue)

    def display_message(self, item):
        name = item.get('name') or 'Unknown'
        text = item.get('text') or ''
        t = item.get('time') or ''
        is_me = (name == self.name_var.get())

        self.text.config(state='normal')

        try:
            time_obj = time.strptime(t, '%Y-%m-%d %H:%M:%S')
            formatted_time = time.strftime('%I:%M %p', time_obj).lstrip("0")
        except Exception:
            formatted_time = t

        if formatted_time != self.last_time:
            self.text.insert('end', f'{formatted_time}\n', ('timestamp',))
            self.last_time = formatted_time

        if is_me:
            padded_text = f"  {text}  "
            self.text.insert('end', f"{padded_text}\n", ('me',))
        else:
            self.text.insert('end', f"{name}\n", ('other_name',))
            self.text.insert('end', f"{text}\n", ('other',))

        self.text.yview('end')
        self.text.config(state='disabled')

    def append_system(self, text):
        self.text.config(state='normal')
        self.text.insert('end', f'{text}\n', ('system',))
        self.text.yview('end')
        self.text.config(state='disabled')

    def on_send(self, event=None):
        msg = self.entry.get().strip()
        if not msg or not self.sock:
            return
        name = self.name_var.get().strip() or 'Anonymous'
        obj = {'type':'message', 'name': name, 'text': msg, 'time': time.strftime('%Y-%m-%d %H:%M:%S')}
        try:
            self.sock.sendall((json.dumps(obj, ensure_ascii=False) + '\n').encode('utf-8'))
            self.entry.delete(0, 'end')
        except Exception:
            self.append_system('Failed to send message')

    def on_close(self):
        self.running = False
        try:
            if self.sock:
                self.sock.close()
        except Exception:
            pass
        self.master.destroy()

def main():
    root = tk.Tk()
    app = ChatClientUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()