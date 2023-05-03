` `**README**

# **1. PROJECT NAME:**
- Part-of-speech tagging using Unigram Tagger in NLTK.

**2. PROJECT OVERVIEW:**

- This project demonstrates the use of the UnigramTagger in NLTK for part-of-speech tagging.
- It uses the Brown corpus for training and testing the model.
- The goal of this project is to train a model that can accurately assign a part of speech tag to each word in a given sentence.

**3. FEATURES:**

- Loads the Brown corpus using the PlaintextCorpusReader in NLTK.
- Performs part-of-speech tagging using the UnigramTagger in NLTK.
- Splits the data into training and testing sets using the train\_test\_split function.
- Calculates the accuracy of the model using the evaluate method provided by the UnigramTagger in NLTK.
- Tests the model on a sample sentence and prints the tagged tokens.

**4. USAGE:**

- To use this code, you need to have NLTK and scikit-learn installed in your environment.
- Load the Brown corpus using the PlaintextCorpusReader in NLTK.
- Preprocess the data using the sent() method provided by the PlaintextCorpusReader in NLTK.
- Split the data into training and testing sets using the train\_test\_split function.
- Train the model using the UnigramTagger in NLTK on the training data.
- Test the model on the testing data and calculate the accuracy using the evaluate method provided by the UnigramTagger in NLTK.
- To tag a new sentence, tokenize it using the word\_tokenize() function in NLTK, and then use the trained model to tag each token.
- Accuracy obtained=68.87%

**5. LICENSE:**

- This project is licensed under the MIT LICENSE.

**6.** **CONTACT INFORMATION:**

Name- Niket Virendra Patil

Email- pniket7@gmail.com



