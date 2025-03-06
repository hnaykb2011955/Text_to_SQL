# **Project Title: Text-to-SQL Query System with Multi-Source Data**

## **Table of Contents**
- [Introduction](#introduction)
- [Latest Updates](#updates)
- [Model Used](#model-used)
- [Contact](#contact)
- [Contributers](#contributers)

## **Introduction**
This project is a **Text-to-SQL Query System with Multi-Source Data**. It converts natural language queries into SQL queries that can retrieve data from  MySQL databases . The system leverages machine learning models (specifically, the T5-small model) to facilitate intuitive query generation.

I explored several text generative models, including Olama, BERT, T5-base, Seq2Seq, and T5-small. Due to my laptop's specifications, I had to choose a model that was compatible without consuming too much time or GPU resources. I ultimately selected T5-small.

However, I encountered an issue where the model generated correct SQL queries but was unable to relate them properly to the database. To address this, I fine-tuned the model on the WikiSQL dataset. Initially, I achieved 92% Rouge score after the first training session. Unfortunately, I could not save the model, necessitating a second round of training. Due to limitations on Google Colab, the training process was interrupted midway, taking around five hours to train for just half the epochs. Each time, the session was disconnected, which forced me to save the partially trained model[Link Text](https://huggingface.co/darshikaaaa/Text_to_SQL), but it still resulted in errors.

While I have the ML model ready, its performance is limited by the available GPU resources. I then explored other pre-trained models on Hugging Face, but their accuracy matched that of my half-trained model, making them unhelpful. I also discovered the **pandas-nql** library, which is promising but requires a ChatGPT key. I believe that with access to a proper GPU, I can complete the remaining work to achieve better accuracy.
### Model Performance (Zero Shot vs. Fine-tuned)

| Metric      | Zero Shot Model | Fine-tuned Model |
|-------------|-----------------|------------------|
| Rouge-1     | 0.03197         | 0.92336          |
| Rouge-2     | 0.00500         | 0.88633          |
| Rouge-L     | 0.03070         | 0.91765          |
| Rouge-Lsum  | 0.03121         | 0.91821          |


## **Model Used**
For the backend, I utilized **Flask** to create a REST API, connecting it to my SQL database where my files are stored. I used **Postman** to test the functionality of my API. My approach effectively searches through the database, and the 92% Rouge score machine learning model is included in this repository under the name `fine_tuned_model.ipynb`, along with the Flask app in `app.py`.
## **Latest Updates**  
The model has been fine-tuned using a **P100 GPU** notebook updated https://github.com/Darshikartisto/Text_To_SQL/edit/main/texttossql-ipynb.ipynb, and the complete version is now available. It is fully operational and can be tested using **FastAPI** for integration. Further updates and enhancements will be added soon.

## **Contributors**    
- **Darshika** ([Darshikartisto](https://github.com/Darshikartisto))

- **Vaishali** ([vaishali312003](https://github.com/vaishali312003)) ([Kaggle Notebook](https://www.kaggle.com/code/vasthetic/texttossql-ipynb))  


## My Biggest Challenge

My biggest challenge was fine-tuning the model without access to a proper GPU. Over the past three days, I kept myself busy tackling this issue.

On the first day, I set up the environment, connected to my SQL database, and researched various models that would fit best with my laptop's specifications and the requirements of the project.

On the second day, I developed the API in `app.py` and successfully connected it to my database.

By the third day, I focused on fine-tuning my model, which took around five hours for the half-trained model.

## Challenge Overcome  
Utilizing a better GPU, we successfully completed model training with improved optimization.  
📅 **Update: 2nd March 2025**  

## Training Progress  

| Step  | Training Loss | Validation Loss |
|-------|--------------|----------------|
| 500   | 0.060800     | 0.042019       |
| 1000  | 0.040200     | 0.030493       |
| 1500  | 0.036500     | 0.025905       |
| 2000  | 0.030900     | 0.022786       |
| 2500  | 0.024600     | 0.020304       |
| 3000  | 0.025800     | 0.018751       |
| 3500  | 0.028700     | 0.017546       |
| 4000  | 0.022300     | 0.016787       |
| 4500  | 0.023800     | 0.016067       |
| 5000  | 0.020200     | 0.015377       |
| 5500  | 0.019500     | 0.014977       |
| 6000  | 0.020900     | 0.014771       |
| 6500  | 0.024200     | 0.014634       |
| 7000  | 0.023900     | 0.014581       |

✅ **Training completed successfully!** 🎉  

### **Performance Metrics**  
- **CPU Time**: User - 2h 24min 29s, System - 27min 16s  
- **Total Execution Time**: 2h 51min 46s  
- **Wall Time**: 2h 51min 37s  

---

## Next Steps  
- Enhance model accuracy with additional fine-tuning  
- Deploy the model for real-time SQL query generation  
- Optimize performance for lower latency  

## How to Run This Project

To run the Text-to-SQL Query System with Multi-Source Data, follow these steps:

 **Clone the Repository**:
   Clone the project repository to your local machine then pip install -r requirements.txt , connect to sql database , you may connect yours and then python app.py
https://github.com/user-attachments/assets/50261a4a-f954-4cac-827c-a3ebb7b08892



