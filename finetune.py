import gpt_2_simple as gpt2

#gpt2.download_gpt2()
#sess = gpt2.start_tf_sess()
#gpt2.finetune(sess, 'animal_summaries_corpus.txt', steps=5)
#gpt2.generate(sess)

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)
gpt2.generate(sess, nsamples=1, prefix="####")
