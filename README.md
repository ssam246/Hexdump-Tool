# **Hexdump Tool**

A robust and feature-rich hexdump tool for analyzing binary files. This tool provides a detailed and customizable view of file content in hexadecimal or binary format, with additional options for formatting and grouping bytes.

---

## **Features**

- **Hexadecimal and Binary Output**:  
  Display file contents in hexadecimal (default) or binary format with the `-b` flag.  

- **Customizable Group Size**:  
  Specify the number of bytes to display per row with the `-g` flag.  

- **Error Handling**:  
  Provides detailed error messages for file not found, permission issues, and invalid inputs.  

- **File Size Information**:  
  Displays the file size in bytes and hexadecimal format.  

- **Modular and Flexible**:  
  Built for maintainability and extensibility, with clean and modular code design.

---

## **Prerequisites**

- Python 3.10.10 installed on your system.

---

## **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ssam246/Hexdump-Tool
   cd hexdump-tool
   ```

2. **Make the Script Executable** (Optional on UNIX-like systems):
   ```bash
   chmod +x hexdump.py
   ```

---

## **Usage**

### **Basic Hexdump**:
Run the tool to view a file's contents in hexadecimal format:
```bash
python hexdump.py example.txt
```

### **Display Bytes in Binary**:
Use the `-b` or `--binary` flag to show binary representation:
```bash
python hexdump.py example.txt -b
```

### **Customize Bytes Per Row**:
Specify the number of bytes to display per row with the `-g` or `--group-size` flag:
```bash
python hexdump.py example.txt -g 32
```

---

## **Command-Line Options**

| Option             | Description                                                        |
|--------------------|--------------------------------------------------------------------|
| `FILE`             | The file to be dumped.                                            |
| `-b, --binary`     | Display bytes in binary instead of hexadecimal.                   |
| `-g, --group-size` | Number of bytes per row (default: 16).                            |

---

## **Output Examples**

### **Hexadecimal Output**:
```plaintext
Size example.txt: 1024 bytes - 0x00000400
00000000  48 65 6c 6c 6f 20 57 6f 72 6c 64 0a 00 00 00 00  |Hello World.....|
00000010  44 61 74 61 20 42 6c 6f 63 6b 0a 00 00 00 00 00  |Data Block......|
```

### **Binary Output**:
```plaintext
Size example.txt: 1024 bytes - 0x00000400
00000000  01001000 01100101 01101100 01101100 01101111 00100000  |Hello |
00000010  01010111 01101111 01110010 01101100 01100100 00001010  |World.|
```

---

## **Error Handling**

- **File Not Found**:  
  If the file does not exist, an appropriate error message is displayed:
  ```plaintext
  Error: File 'missing.txt' not found.
  ```

- **Permission Issues**:  
  If the file is inaccessible:
  ```plaintext
  Error: Permission denied for file 'restricted.txt'.
  ```

- **Invalid Group Size**:  
  If the specified group size is not valid:
  ```plaintext
  Error: Group size must be a positive integer.
  ```

---

## **Contributing**

Contributions are welcome! To contribute:
1. Fork the repository.
2. Implement your changes or fix issues.
3. Submit a pull request with a detailed description of your improvements.

---

## **License**

This project is licensed under the **MIT License**.  

---

## **Disclaimer**

This tool is intended for **educational and analytical purposes only**.  
The author does not condone the use of this tool for illegal activities or malicious purposes.  
Ensure you have proper authorization before analyzing files.

---

### **Made with 💻 and 🔍 by Stephen**

