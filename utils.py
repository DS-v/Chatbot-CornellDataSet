import nltk
import pickle
import re
import numpy as np
import compress_pickle
nltk.download('stopwords')
from nltk.corpus import stopwords

# Paths for all resources for the bot.
RESOURCE_PATH = {
		"TOKENIZER":"tokenizer",
		"CHECKPOINT":"checkpoint"
}


def text_prepare(text):
    """Performs tokenization and simple preprocessing."""

    replace_by_space_re = re.compile('[/(){}\[\]\|@,;]')
    bad_symbols_re = re.compile('[^0-9a-z #+_]')
    stopwords_set = set(stopwords.words('english'))

    text = text.lower()
    text = replace_by_space_re.sub(' ', text)
    text = bad_symbols_re.sub('', text)
    text = ' '.join([x for x in text.split() if x and x not in stopwords_set])

    return text.strip()


def load_embeddings(embeddings_path):
    """Loads pre-trained word embeddings from tsv file.

    Args:
      embeddings_path - path to the embeddings file.

    Returns:
      embeddings - dict mapping words to vectors;
      embeddings_dim - dimension of the vectors.
    """

    # Hint: you have already implemented a similar routine in the 3rd assignment.
    # Note that here you also need to know the dimension of the loaded embeddings.
    # When you load the embeddings, use numpy.float32 type as dtype

    starspace_embeddings = dict()
    for line in open(embeddings_path, encoding='utf-8'):
        row = line.strip().split('\t')
        starspace_embeddings[row[0]]=np.array(row[1:],dtype=np.float32)
    return starspace_embeddings,100
    # remove this when you're done
    raise NotImplementedError(
        "Open utils.py and fill with your code. In case of Google Colab, download"
        "(https://github.com/hse-aml/natural-language-processing/blob/master/project/utils.py), "
        "edit locally and upload using '> arrow on the left edge' -> Files -> UPLOAD")


def question_to_vec(question, embeddings, dim):
    """Transforms a string to an embedding by averaging word embeddings."""

    # Hint: you have already implemented exactly this function in the 3rd assignment.
    ans=np.zeros(dim)
    c=0
    words=question.split()
    for word in words:
        if word in embeddings:
            emb=embeddings[word]
            ans+=emb
            c+=1
    #print(ans)
    if c==0:
        return ans
    return ans/c

    # remove this when you're done
    raise NotImplementedError(
        "Open utils.py and fill with your code. In case of Google Colab, download"
        "(https://github.com/hse-aml/natural-language-processing/blob/master/project/utils.py), "
        "edit locally and upload using '> arrow on the left edge' -> Files -> UPLOAD")


def unpickle_file(filename):
    """Returns the result of unpickling the file content."""
    return compress_pickle.load(filename, compression="lzma", set_default_extension=False)
    with open(filename, 'rb') as f:
        return pickle.load(f)
