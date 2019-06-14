## Examples
Title: Dog
> Dog is an English word which refers to a dog, usually a service animal, trained to do a particular task, most often to assist with human interaction, and used for identification. Dogs are generally considered to be part of the “pet” category of pets and are not subject to the same animal welfare criteria as humans.
> Common uses of the word include “dog”, “doggy”, “doggy-dog”, “doggie”, “dog-like”, “doglike-dog”, “dog odour”, “dog-like-dog”, “dog-like-dog”, “dog-like-dog”, and “dog that can sniff”.

You can also give it a completely made-up title.

Title: The Barkwatoracus
> The Barkwatoracus is a genus of insects in the family Aplysia in the order Aplysia. Commonly known in the United States as beeswax-hipped beeswax, the genus is found in temperate regions of southeast and western South America. All species are found from Central America, but the genus is rapidly spreading to temperate regions.
> The species has been described in North America, Europe and Asia. The name “Barkwatoracus” derives from the shape of this species’ antennae, which is similar to the shape of the keen eye of a bumble bee.


## Dependencies

Tensorflow: https://www.tensorflow.org/install

GPT-2-Simple: https://github.com/minimaxir/gpt-2-simple

Wikipedia-API: https://pypi.org/project/Wikipedia-API/

## How it works

1. `generate_corpus.py` scrapes wikipedia for (title : summary) pairs from randomly selected articles.
2. `gather_corpus.py` puts all generated corpuses into one file called `all_text.txt`.
3. `download_and_train_gpt2.py` downloads the 345M parameter model and fine-tunes it on `all_text.txt`.
4. `generate_summaries.py` requests a user-input title and generates fake wikipedia summaries.
