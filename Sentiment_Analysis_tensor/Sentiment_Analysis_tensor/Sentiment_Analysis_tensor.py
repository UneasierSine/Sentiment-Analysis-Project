
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

from keras.datasets import imdb
from keras.preprocessing import sequence
from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, Dropout

#Choose the word vector file to use
Tk().withdraw()
filePath = askopenfilename()

#Open the GloVe file
f = open(filePath,mode='r',encoding="utf-8")

#Feed the GloVe into a numpy array of vector[word]
words = {}
for line in f:
    splitLine = line.split()
    word = splitLine[0]
    embedding = np.array([float(val) for val in splitLine[1:]])
    words[word] = embedding
    print ("Done.",len(words)," words loaded!")

vocabulary_size = len(words)
(X_train, y_train), (X_test, y_test) = imdb.load_data(num_words = vocabulary_size)
print('Loaded dataset with {} training samples, {} test samples'.format(len(X_train), len(X_test)))

max_words = 500
X_train = sequence.pad_sequences(X_train, maxlen=max_words)
X_test = sequence.pad_sequences(X_test, maxlen=max_words)
print("Padded the testing and training data to 500 words")

embedding_size = len(words['the'])
model = Sequential()
model.add(Embedding(vocabulary_size, embedding_size, input_length=max_words))
model.add(LSTM(500))
model.add(Dense(1, activation='sigmoid'))

print(model.summary())
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

batch_size = 64
num_epochs = 5

X_valid, y_valid = X_train[:batch_size], y_train[:batch_size]
X_train2, y_train2 = X_train[batch_size:], y_train[batch_size:]

model.fit(X_train2, y_train2, validation_data=(X_valid, y_valid), batch_size=batch_size, epochs=num_epochs)

scores = model.evaluate(X_test, y_test)
print('Test Accuracy: ', scores[1])