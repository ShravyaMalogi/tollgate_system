
<div align="center">
    
# Project Architecture

Vehicle Image Upload  
↓  
YOLOv8 License Plate Detection  
↓  
License Plate Cropping  
↓  
Text Extraction using Tesseract OCR  
↓  
Vehicle Number Verification in Database  
↓  
Toll Deduction and Payment Logging

</div>

---
 
<div align="center">
    
# Project Structure </div>

```
tollgate_system
│
├── app.py
├── plate_detection.py
├── database.py
├── best.pt
├── requirements.txt
│
└── data
    ├── balance.csv
    ├── payments.csv
    └── users.csv
```

---

<div align="center">
    
# Setup Instructions (macOS) </div>

## 1. Clone the Repository

```
git clone https://github.com/yourusername/tollgate_system.git
cd tollgate_system
```

---

## 2. Install Python Dependencies

Create a virtual environment :

```
python3 -m venv venv
source venv/bin/activate
```

Install required packages:

```
pip install -r requirements.txt
```

---

## 3. Install Homebrew 

Check if Homebrew is installed:

```
brew --version
```

If not installed:

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

---

## 4. Install Tesseract OCR

```
brew install tesseract
```

Verify installation:

```
tesseract --version
```

---

## 5. Download YOLO License Plate Detection Model

Install gdown:

```
pip install gdown
```

Download trained weights:

```
gdown "https://drive.google.com/uc?id=1dIyJooVaowaNUj0R1Q-HUnu-utiGsEj8&confirm=t"
```

This will download:

```
best.pt
```

Place the file in the project root directory.

---

## 6. Run the Application

Start the Streamlit app:

```
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

Upload a vehicle image and the system will:

1. Detect the license plate using YOLOv8
2. Extract the plate number using Tesseract OCR
3. Check the vehicle balance
4. Deduct the toll amount
5. Save the transaction in the payments database
