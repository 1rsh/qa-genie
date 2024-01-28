from hugchat import hugchat
from hugchat.login import Login
import pandas as pd
from tqdm.auto import tqdm
import time

tqdm.pandas()

def get_generator(email: str, pwd: str, model: str = "meta"):
    sign = Login(email, pwd)
    cookies = sign.login()

    cookie_path_dir = ".cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)

    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

    model_decode = {
        "meta" : 0,
        "oasst" : 1
    }

    assert model in model_decode.keys(), f"Invalid model name passed - {model}!\n(should be one of meta or oasst)"

    chatbot.switch_llm(model_decode[model])

    return chatbot



def extract_qa(chatbot, text: str, num_qn: int = 3, same_conv = False):
    assert num_qn <= len(text)//20, "Please reduce num_qn or increase size of text"
    msg = f"Generate exactly {num_qn} questions and their answers from the following text that someone related to the text might ask in the format Q1) Q2) Q3) A1) A2) A3)\n{text}\nNo need to add any greeting or saying these are the questions just give Q1), Q2), Q3)"
    
    try:
        all_qna = chatbot.query(msg).text
        
    except Exception as e:
        if(str(e)=='Failed to parse response: {"message":"Conversation not found"}'):
            _id = chatbot.new_conversation()
            chatbot.change_conversation(_id)
            all_qna = chatbot.query(msg).text
            

    questions = []
    answers = []
    
    j = 1
    
    while j<num_qn+1:
    
        try:
            check = all_qna
        except Exception as e:
            all_qna = chatbot.query(msg).text
            
        
        q_index = all_qna.find(f"Q{j})") + 4
        a_index = all_qna.find(f"A{j})") + 4
        
        if all_qna.find(f"Q{j+1})")==-1:
            next_q_index = -1
        else:
            next_q_index = all_qna.find(f"Q{j+1})") - 2 if j<num_qn+1 else -1
        
        questions.append(all_qna[q_index : a_index - 5])
        if(next_q_index==-1):
            answers.append(all_qna[a_index :])
        else:
            answers.append(all_qna[a_index : next_q_index])
            
        j+=1
    
    if(not(same_conv)):
        chatbot.delete_conversation()
    
    return pd.DataFrame({"questions": questions[:num_qn], "answers": answers[:num_qn], "context":[text]*num_qn})



def extract_qas(chatbot, texts: list, num_qn_each: int = 3, same_conv = True, time_to_sleep = 2):
    
    if len(texts) == 1:
        print("Only one text found, use extract_qn instead!")
    
    frames = []
    for text in tqdm(texts, "Generating"):
        ds = extract_qa(chatbot, text, num_qn_each, same_conv)
        frames.append(ds)
        time.sleep(time_to_sleep)
        
    df = pd.concat(frames).reset_index(drop = True)
    
    return df

