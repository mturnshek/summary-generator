import gpt_2_simple as gpt2


model_name = "345M"
gpt2.download_gpt2(model_name=model_name)
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              'downloaded_summaries/all_text.txt',
              model_name=model_name,
              steps=2000)   # steps is max number of training steps

gpt2.generate(sess)