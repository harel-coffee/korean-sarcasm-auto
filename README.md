## Kocasm : korean automatic sarcasm detection

- Why this name? **Kocasm** is blend word, Korean + sarcasm

### Why Irony detection is important?

Because it converts or distorts literal meaning of sentence, sarcasm is highly related to Sentiment Classification.

### Preparing the data

- HTML data gathered from a twitter
- Data is composed of label 1,0.
  - label 1: sarcasm, label0: randomly gatherd
- korean data, queries for hashtags such as **역설, 아무말, 운수좋은날, 笑, 뭐래 아닙니다, 그럴리없다, 어그로, irony sarcastic, sarcasm** was labeled as True data.(so still has lots of noise)
- And pre-processed dataset (1) user anonymous (2) removing hashtag (3) removing url process.
<img src="https://github.com/SpellOnYou/korean-sarcasm/blob/master/img/pipeline_clean_tokens.png" width="500" height="700" alt="preprocessing-pipeline" >
If you have any other questions with corpus, please contacts me</br>- jiwon.kim.096@gmail.com

If you want to compare with other dataset, refer: [English] </br>

 - ghosh: This english dataset collected by Aniruddha Ghosh and Tony Veale. See their [repository](https://github.com/AniSkywalker/SarcasmDetection) and [paper, Fracking Sarcasm using Neural Network](http://www.aclweb.org/anthology/W16-0425)
 
### Language Model (It is still being editting)

- [`bag_of_words.py`](https://github.com/SpellOnYou/korean-sarcasm/blob/master/models/bag_of_words.py): Basic bayesian model
- [`dl_models.py`](https://github.com/SpellOnYou/korean-sarcasm/blob/master/models/dl_models.py): Model classes for a general transformer
- [`tf_attention_models.py`](https://github.com/SpellOnYou/korean-sarcasm/blob/master/models/tf_attention_models.py) : Tensorflow attentive rnn model
* I'm strongly inspired by [MirunaPislar](https://github.com/MirunaPislar/Sarcasm-Detection)'s code and I referred a lot to that codes, but I tried to make my codes more pythonic and pytorchic style. Actually, I am still modifying the code.
        
* Kokasm is compatible with: Python 2.7-3.7


### In case with your own data, clone this repository and...

```
export DATA_DIR=/path/to/data
export PREP_DIR=/path/to/preprocess
export SAVE_DIR=/path/to/save

python tf_attention_models.py \
    --mode train \
    --model_cfg config/attention_base.json \
    --data_file $DATA_DIR/jiwon/train.csv \
    --test_file $DATA_DIR/jiwon/test.csv \
    --pretrain_file $BERT_PRETRAIN \
    --vocab PREP_DIR/vocab.txt \
    --save_dir $SAVE_DIR \
    --max_len 128
```

## Citation

If you found this dataset useful, please cite as:

```bibtex
@misc{kim2019kocasm,
  author = {Kim, Jiwon and Cho, Won Ik},
  title = {Kocasm: Korean Automatic Sarcasm Detection},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/SpellOnYou/korean-sarcasm}}
}
```

## See also

### linguistic, computer science related to sarcasm
   * [universal irony detection model with czech](https://pdfs.semanticscholar.org/0c27/64756299a82659605b132aef9159f61a4171.pdf)
   * [Chinese and attentive-RNN](https://link.springer.com/chapter/10.1007/978-3-319-56608-5_45)
   * [Focus on meaning conflict with hashtags](https://www.researchgate.net/publication/255729692_The_perfect_solution_for_detecting_sarcasm_in_tweets_not)
   
   Implementation as proposed by Yang et al. in "Hierarchical Attention Networks for Document Classification" (2016)
  
### Kaggle - [Twitter Inory Detection](https://www.aclweb.org/anthology/S18-1005/)

