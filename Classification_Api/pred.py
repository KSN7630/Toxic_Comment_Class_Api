from cleanText import clean_text
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd



tfidf = TfidfVectorizer(min_df=100,  max_features=10000,
            strip_accents='unicode', analyzer='word',ngram_range=(1,4),
            use_idf=1,smooth_idf=1,sublinear_tf=1,
            stop_words = 'english')
file_path = 'models/df_full_str.csv'
df_full = pd.read_csv(file_path)
# Replace NaN values with an empty string
df_full['final_string'].fillna('', inplace=True)
documents = df_full['final_string'].tolist()
tfidf_vector = tfidf.fit(documents)
# Transform documents to TF-IDF matrix
tfidf_matrix = tfidf_vector.transform(documents)

# Check the shape of the TF-IDF matrix
print(tfidf_matrix.shape)


def pred_prob(inp_str, model_arr_name):
  clean_str = clean_text(inp_str)
  test_vec = tfidf.transform([clean_str])
  tot_model = len(model_arr_name)
  cnt_1 = 0
  for curr_model in model_arr_name:
    y_pred = curr_model.predict(test_vec)
    y_pred = y_pred[0]
    if(y_pred == 1):
      cnt_1 += 1
  return round(cnt_1/tot_model, 3)

def output_report(str,models):
  out_prob_arr=[]
  for col in range(0, 6):
    out_prob_arr.append(pred_prob(str, models[col]))
  
  out_label_arr = []
  for i in range(0, 6):
    if(out_prob_arr[i] >= 0.5):
      out_label_arr.append(1)
    else:
      out_label_arr.append(0)
  report=generate_report(out_label_arr)    
  return report    


def generate_report(pred_arr):
    columns = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']
    report = {}
    fine = all(pred == 0 for pred in pred_arr)


    report['Status'] = True if fine else False
    for i, pred in enumerate(pred_arr):
        label = columns[i]
        report[label] = True if pred == 1 else False

    return report
