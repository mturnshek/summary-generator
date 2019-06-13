import gpt_2_simple as gpt2


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

while True:
    title = input('title > ')
    generations = gpt2.generate(sess, prefix='---###<title>###---' + title + '---###<summary>###---', include_prefix=True, nsamples=5, batch_size=5, truncate="---###<end>###---", return_as_list=True)
    for generation in generations:
        print(generation)