To quickly generate text, try the following:

```
from andromeda import Model

model = Model()
model.generate('The quick brown fox jumped over the lazy dog.')
```

If no other model is specified, the [default model](https://huggingface.co/mchaney/andromeda) will be downloaded from Huggingface.

The model configuration can be easily changed:

```
model.config.do_sample = True
```

Finally, save the model (changes to the config will be saved as well):

```
model.save()
```