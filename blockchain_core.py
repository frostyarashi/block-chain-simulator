import hashlib
import tkinter as tk
from tkinter import scrolledtext

# Blockchain Logic
class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return hashlib.sha256((str(self.data) + str(self.previous_hash)).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", "0")
    
    def add_block(self, new_block):
        new_block.previous_hash = self.chain[-1].hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)
    
    def print_chain(self):
        chain_data = ""
        for i, block in enumerate(self.chain):
            chain_data += f"Block #{i}:\n"
            chain_data += f"Data: {block.data}\n"
            chain_data += f"Hash: {block.hash}\n"
            chain_data += f"Previous Hash: {block.previous_hash}\n"
            chain_data += "------------------------------\n"
        return chain_data

# GUI Code
class BlockchainGUI:
    def __init__(self, root):
        self.blockchain = Blockchain()  # Initialize blockchain
        self.root = root
        self.root.title("Blockchain Simulator")
        self.root.geometry("500x400")

        # Title Label
        self.title_label = tk.Label(root, text="Blockchain Simulator", font=("Arial", 16))
        self.title_label.pack(pady=10)

        # Entry for Block Data
        self.data_label = tk.Label(root, text="Enter data for new block")
        self.data_label.pack()

        self.data_entry = tk.Entry(root, width=50)
        self.data_entry.pack(pady=5)

        # Add Block Button
        self.add_block_button = tk.Button(root, text="Add Block", command=self.add_block)
        self.add_block_button.pack(pady=5)

        # Display Blockchain Button
        self.display_button = tk.Button(root, text="Display Blockchain", command=self.display_blockchain)
        self.display_button.pack(pady=5)

        # Text Box to Display the Blockchain
        self.chain_display = scrolledtext.ScrolledText(root, width=60, height=15)
        self.chain_display.pack(pady=10)

        # Exit Button
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack(pady=5)

    # Add Block Function
    def add_block(self):
        data = self.data_entry.get()
        if data:
            new_block = Block(data, self.blockchain.chain[-1].hash)
            self.blockchain.add_block(new_block)
            self.chain_display.insert(tk.END, f"Block added: {data}\n")
        else:
            self.chain_display.insert(tk.END, "Please enter block data.\n")

    # Display Blockchain Function
    def display_blockchain(self):
        self.chain_display.delete(1.0, tk.END)  # Clear display
        chain_data = self.blockchain.print_chain()
        self.chain_display.insert(tk.END, chain_data)

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = BlockchainGUI(root)
    root.mainloop()
