import gpt_2_simple as gpt2


sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

while True:
    title = input('title > ')
    generations = gpt2.generate(
        sess,
        prefix='---###<title>###---' + title + '---###<summary>###---',
        include_prefix=True,
        nsamples=16,
        batch_size=16,
        truncate="---###<end>###---",
        temperature=0.75,
        return_as_list=True
    )
    for generation in generations:
        summary = generation.split("-###<title>###---" + title + "---###<summary>###---")[1]
        summary = summary.split("---###<end>###---")[0]
        print(title, '\n')
        print(summary, '\n')
        print('\n\n\n')
