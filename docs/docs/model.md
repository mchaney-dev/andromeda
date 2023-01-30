# `Model()`

> `Model(model_type, model_path)`

> The base class for a text generation model.

> **Parameters**:

> - `model_type` (string): Optional. The type of model to use. Defaults to `GPT-NEO`.

> - `model_path` (string): Optional. The path to the model to use. Defaults to `mchaney/andromeda`, the custom model used in development, but can be any model from the HuggingFace model hub, or a path to a local folder containing the model's files.

> **Returns:**

> A `Model` object.

## Attributes

### `Model.name`
> The name of the model.

> **Type:** `string`

---

### `Model.path`
> The location where the model's files are stored once downloaded. Defaults to `[Python package location]/[andromeda folder]/andromeda-latest`.

> **Type:** `string`

---

### `Model.train_args`
> Training arguments for the model. Wrapper for HappyTransformer's `GENTrainArgs` class.

> **Properties:**

> - `Model.train_args.learning_rate`: defaults to `5e-05`
> - `Model.train_args.num_train_epochs`: defaults to `3`
> - `Model.train_args.batch_size`: defaults to `1`
> - `Model.train_args.adam_beta1`: defaults to `0.9`
> - `Model.train_args.adam_beta2`: defaults to `0.999`
> - `Model.train_args.adam_epsilon`: defaults to `1e-08`
> - `Model.train_args.max_grad_norm`: defaults to `1.0`
> - `Model.train_args.save_preprocessed_data`: defaults to `False`
> - `Model.train_args.save_preprocessed_data_path`: defaults to `''`
> - `Model.train_args.load_preprocessed_data`: defaults to `False`
> - `Model.train_args.load_preprocessed_data_path`: defaults to `''`
> - `Model.train_args.preprocessing_processes`: defaults to `1`
> - `Model.train_args.mlm_probability`: defaults to `0.15`
> - `Model.train_args.fp16`: defaults to `False`

> **Type:** `GENTrainArgs` object

---

### `Model.eval_args`

> Training arguments for the model. Wrapper for HappyTransformer's `GENEvalArgs` class.

> **Properties:**

> - `Model.eval_args.batch_size`: defaults to `1`
> - `Model.eval_args.save_preprocessed_data`: defaults to `False`
> - `Model.eval_args.save_preprocessed_data_path`: defaults to `''`
> - `Model.eval_args.load_preprocessed_data`: defaults to `False`
> - `Model.eval_args.load_preprocessed_data_path`: defaults to `''`
> - `Model.eval_args.preprocessing_processes`: defaults to `1`
> - `Model.eval_args.mlm_probability`: defaults to `0.15`

> **Type:** `GENEvalArgs` object

---

### `Model.config`

> The model configuration. Wrapper for HappyTransformer's `GENSettings` class.

> **Properties:**

> - `Model.config.min_length`: defaults to `10`
> - `Model.config.max_length`: defaults to `50`
> - `Model.config.do_sample`: defaults to `False`
> - `Model.config.early_stopping`: defaults to `False`
> - `Model.config.num_beams`: defaults to `1`
> - `Model.config.temperature`: defaults to `1`
> - `Model.config.top_k`: defaults to `50`
> - `Model.config.no_repeat_ngram_size`: defaults to `0`
> - `Model.config.top_p`: defaults to `1`
> - `Model.config.bad_words`: defaults to `None`

> **Type:** `GENSettings` object

## Methods

### `Model.train()`

> Trains the model. Training arguments can be configured using the `train_args` attribute.

> **Parameters:**

> - `input_filepath` (string): The path to the file containing the training data.

> **Returns:**

> `None`.

---

### `Model.evaluate()`

> Trains the model. Training arguments can be configured using the `eval_args` attribute.

> **Parameters:**

> - `input_filepath` (string): The path to the file containing the evaluation data.

> **Returns:**

> `loss` (float).

---

### `Model.generate()`

> Generates text using the model. Generation arguments can be configured using the `config` attribute.

> **Parameters:**

> - `text` (string): The text to use as the prompt for the model.
> - `raw` (bool): Optional. Whether to return the raw output from the model. Defaults to False.

> **Returns:**

> The generated text as a string, or the raw output from the model (an object of type `GenerationResult`).

---

### `Model.save()`

> Saves the model to disk, overwriting any previously saved files. The model will be saved to the `path` attribute, along with any configuration changes.

> **Parameters:**

> - None

> **Returns:**

> - `None`.