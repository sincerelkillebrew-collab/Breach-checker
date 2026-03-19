# SXO Password Auditor 🛡️

A high-performance Python tool to check if a password has been compromised in a data breach using the **Have I Been Pwned** API.

## 🚀 How it Works (Privacy First)
This tool uses **K-Anonymity** to ensure your actual password is never sent over the internet.
1. The password is converted into a **SHA-1 Hash** locally.
2. Only the **first 5 characters** of the hash are sent to the API.
3. The API returns a list of all leaked hashes starting with those 5 characters.
4. The tool compares the results locally on your machine.



## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `requests`, `hashlib`
- **Hardware Optimized:** Developed and tested on a Ryzen 7 5800XT system.

## 📦 Installation
1. Clone this repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/SXO-Password-Auditor.git](https://github.com/YOUR_USERNAME/SXO-Password-Auditor.git)
   Install dependencies:
   pip install requests
   Run the script and follow the on-screen prompts:

Bash
python breach_check.py

---

### **Final Pro-Tip: The `.gitignore`**
Since you were using a `.venv` (virtual environment) earlier, you **do not** want to upload that folder to GitHub. It contains thousands of tiny files that will clutter your repository.

1. Create one more file named `.gitignore`.
2. Inside that file, just type:
   ```text
   .venv/
   __pycache__/
   *.pyc
