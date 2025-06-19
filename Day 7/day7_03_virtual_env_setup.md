# Day 7 – Task 03: Set Up a Virtual Environment and Install `requests`

This guide walks you through creating a virtual environment for a Python project and installing the `requests` package within it.

---

## 🧱 Step 1: Navigate to Your Project Directory

Open your terminal or command prompt and move into the folder where you want to create your Python environment:

```bash
cd path/to/your/project
```

---

## 🌀 Step 2: Create a Virtual Environment

Run the following command to create a virtual environment named `venv`:

```bash
python -m venv venv
```

> This will create a folder called `venv` containing the Python environment.

---

## ▶️ Step 3: Activate the Virtual Environment

### On **Windows**:

```bash
venv\Scripts\activate
```

### On **macOS/Linux**:

```bash
source venv/bin/activate
```

> After activation, your terminal prompt should change to indicate you're now working inside the virtual environment.

---

## 📦 Step 4: Install the `requests` Library

Once the environment is active, install the `requests` package using pip:

```bash
pip install requests
```

You should see an installation success message.

---

## ✅ Step 5: Verify Installation

To confirm that `requests` is installed correctly:

```bash
pip show requests
```

> This will display version, location, and other package metadata.

---

## 🚪 Step 6: Deactivate the Environment (Optional)

When you're done, you can deactivate the virtual environment with:

```bash
deactivate
```

---

## 💡 Why Use a Virtual Environment?

- Keeps dependencies isolated
- Prevents version conflicts across projects
- Makes project setup reproducible and clean

---

That's it! You've successfully created a virtual environment and installed a Python package within it.