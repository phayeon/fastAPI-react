import os

import tensorflow
from keras_preprocessing import sequence
from tensorflow.python.keras.models import load_model

from app.admin.path import dir_path
from app.services.food_intent.utils.Preprocess import Preprocess
# 단어 시퀀스 벡터 크기
from app.services.food_intent.config.GlobalParams import MAX_SEQ_LEN

intent_labels = {0: "인사", 1: "욕설", 2: "주문", 3: "예약", 4: "기타"}


class ModelTest:
    def __init__(self):
        self.query = "탕수육 1개 예약할게요."
        # self.query = "안녕하세요?"

    def test(self):
        print('작업 시작')
        query = self.query
        # 의도 분류 모델 불러오기
        model = load_model(os.path.join(dir_path('models'), 'intent', 'intent_model.h5'))
        p = Preprocess(word2index_dic=os.path.join(dir_path('train_tools'), 'dict', 'chatbot_dict.bin'),
                       userdic=os.path.join(dir_path('utils'), 'user_dic.tsv'))
        pos = p.pos(query)
        keywords = p.get_keywords(pos, without_tag=True)
        seq = p.get_wordidx_sequence(keywords)
        sequences = [seq]
        padded_seqs = sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

        predict = model.predict(padded_seqs)
        predict_class = tensorflow.math.argmax(predict, axis=1)
        print(query)
        print("의도 예측 점수 : ", predict)
        print("의도 예측 클래스 : ", predict_class.numpy())
        print("의도  : ", intent_labels[predict_class.numpy()[0]])


if __name__ == '__main__':
    ModelTest().test()
