




import os
""" First change the following directory link to where all input files do exist """
os.chdir("C:\\Users\\prata\\Documents\\book_codes\\NLP_DL")

import numpy as np
import pandas as pd


# File reading

with open('bot.txt', 'r') as content_file:
    botdata = content_file.read()
    
   
Questions = []
Answers = []

for line in botdata.split("</pattern>"):
    if "<pattern>" in line:
        Quesn = line[line.find("<pattern>")+len("<pattern>"):]
        Questions.append(Quesn.lower())
        

for line in botdata.split("</template>"):
    if "<template>" in line:
        Ans = line[line.find("<template>")+len("<template>"):]
        Ans = Ans.lower()
        Answers.append(Ans.lower())
  

QnAdata = pd.DataFrame(np.column_stack([Questions,Answers]),columns = ["Questions","Answers"])
QnAdata["QnAcomb"] = QnAdata["Questions"]+" "+QnAdata["Answers"]


print(QnAdata.head())


# Creating Vocabulary
import nltk
import collections

counter = collections.Counter()

for i in range(len(QnAdata)):
    for word in nltk.word_tokenize(QnAdata.iloc[i][2]):
        counter[word]+=1

word2idx = {w:(i+1) for i,(w,_) in enumerate(counter.most_common())}        
idx2word = {v:k for k,v in word2idx.items()}


idx2word[0] = "PAD"

vocab_size = len(word2idx)+1

print "\n\nVocabulary size:",vocab_size


def encode(sentence, maxlen,vocab_size):
    indices = np.zeros((maxlen, vocab_size))
    for i, w in enumerate(nltk.word_tokenize(sentence)):
        if i == maxlen: break
        indices[i, word2idx[w]] = 1
    return indices


def decode(indices, calc_argmax=True):
    if calc_argmax:
        indices = np.argmax(indices, axis=-1)
    return ' '.join(idx2word[x] for x in indices)


question_maxlen = 10
answer_maxlen = 20



def create_questions(question_maxlen,vocab_size):
    question_idx = np.zeros(shape=(len(Questions),question_maxlen,vocab_size))
    
    for q in range(len(Questions)):
        question = encode(Questions[q],question_maxlen,vocab_size)

        question_idx[i] = question 
    return question_idx

quesns_train = create_questions(question_maxlen=question_maxlen,vocab_size=vocab_size)


def create_answers(answer_maxlen,vocab_size):
    answer_idx = np.zeros(shape=(len(Answers),answer_maxlen,vocab_size))
    
    for q in range(len(Answers)):
        answer = encode(Answers[q],answer_maxlen,vocab_size)

        answer_idx[i] = answer 
    return answer_idx

answs_train = create_answers(answer_maxlen=answer_maxlen,vocab_size=vocab_size)



# Model was working fine with correct architecture

from keras.layers import Input,Dense,Dropout,Activation
from keras.models import Model
from keras.layers.recurrent import LSTM
from keras.layers.wrappers import Bidirectional
from keras.layers import RepeatVector,TimeDistributed,ActivityRegularization



n_hidden = 128


question_layer = Input(shape=(question_maxlen,vocab_size))

encoder_rnn = LSTM(n_hidden,dropout=0.2,recurrent_dropout=0.2)(question_layer)

repeat_encode = RepeatVector(answer_maxlen)(encoder_rnn)

dense_layer = TimeDistributed(Dense(vocab_size))(repeat_encode)

regularized_layer = ActivityRegularization(l2=1)(dense_layer)
    
softmax_layer = Activation('softmax')(regularized_layer)


model = Model([question_layer],[softmax_layer])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print (model.summary())


# Readers encouraged to try this
#encoder_rnn = Bidirectional(LSTM(n_hidden,dropout=0.2,recurrent_dropout=0.2),merge_mode='concat')(question_layer)

# Model Training
quesns_train_2 = quesns_train.astype('float32')
answs_train_2 = answs_train.astype('float32')

model.fit(quesns_train_2, answs_train_2,batch_size=32,epochs=30,validation_split=0.05)


# Model preidciton
ans_pred = model.predict(quesns_train_2[0:3])

print (decode(ans_pred[0]))
print (decode(ans_pred[1]))


