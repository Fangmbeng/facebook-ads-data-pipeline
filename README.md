# 📊 **facebook-ads-data-pipeline**  

### **Description**  
This project automates the extraction, storage, and analysis of **Facebook Ads performance data** using the **Facebook Graph API, MongoDB, and Pandas**. It retrieves **campaign, ad set, and ad metrics** and stores them in MongoDB for further analysis.  

---

### **Key Features**  
✅ **Automated Facebook Ads Data Fetching** – Retrieves data on **campaigns, ad sets, and ads**, including performance insights (**spend, impressions, clicks, CTR, CPM, conversions**).  
✅ **MongoDB Integration** – Stores structured ad data in **MongoDB**, preventing duplicates for efficient storage.  
✅ **Pandas DataFrames for Analysis** – Converts MongoDB collections into **Pandas DataFrames** for further processing.  
✅ **Error Handling** – Handles API errors and prevents redundant data inserts.  

---

### **How to Use**  

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/yourusername/facebook-ads-data-pipeline.git
cd facebook-ads-data-pipeline
```

2️⃣ **Install Dependencies**  
```bash
pip install facebook-sdk pymongo pandas
```

3️⃣ **Set Up API Credentials**  
- Replace **`YOUR_ACCESS_TOKEN`** and **`YOUR_ACCOUNT_ID`** in `app.py` with your **Facebook API credentials**.

4️⃣ **Run the Script**  
```bash
python app.py
```

5️⃣ **Verify Data in MongoDB**  
```bash
mongo
use facebook_data
db.campaigns.find().pretty()
```

---

### **File Structure**  
```
facebook-ads-data-pipeline/
│── app.py              # Main script for fetching and storing data
│── requirements.txt    # Add the Required Python packages
│── README.md           # Documentation
```

---

### **Future Improvements**  
🚀 **Schedule Automated Data Fetching** (using `cron` or `Celery`)  
📊 **Integrate with Dash or Streamlit** for real-time data visualization  
📥 **Export Data to CSV** for further analysis  

This project is ideal for **marketers, data analysts, and developers** who want to automate **Facebook Ads performance tracking**. 🚀
