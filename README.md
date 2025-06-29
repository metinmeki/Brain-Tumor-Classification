# 🧠 Brain Tumor Classification

🚀 **Project Overview**  
Brain Tumor Classification is a deep learning-powered web application that classifies brain tumors from MRI scans using a Convolutional Neural Network (CNN). It detects Glioma, Meningioma, Pituitary tumors, or absence of tumor

⚙️ **Key Features**  
- High-accuracy CNN model trained on a curated MRI dataset  
- Simple, user-friendly Flask-based web interface  
- Supports JPEG, PNG MRI image uploads  

🛠️ **Technologies & Tools**  
- Python 3.2  
- TensorFlow / Keras  
- Flask  
- OpenCV  
- Pillow (PIL)  
- NumPy  

📁 **Project Structure**  
Brain-Tumor-Classification/
├── app.py # Flask web application
├── model/ # Pre-trained CNN model (.h5)
├── static/ # Static files like CSS and uploads
│ ├── uploads/ # Uploaded MRI images and heatmaps
│ └── style.css # CSS stylesheet
├── templates/ # HTML templates
│ └── index.html # Main interface
├── requirements.txt # Project dependencies
└── README.md # This file


📖 **How It Works**  
- Loads the trained CNN model from `model/`  
- Receives MRI image uploads via web form  
- Preprocesses images and predicts tumor type  
- Generates Grad-CAM heatmaps to visualize attention  
- Displays results and heatmaps in the browser  

🔮 **Future Improvements**  
- Add batch processing of MRI folders  
- Implement user accounts and save history  
- Optimize model size for faster inference  
- Add voice feedback and multilingual support  

📄 **License**  
This project is licensed under the MIT License. You are free to use, modify, and distribute it with attribution.

© 2025 Metin Meki

📬 **Contact**  
Developed by Metin Meki  
Email: metinmeki99@gmail.com  
GitHub: [https://github.com/metinmeki](https://github.com/metinmeki)

⭐ If you find this project useful, please consider starring the repository!
