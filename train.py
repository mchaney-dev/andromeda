from main import andromeda
from transformers import TrainingArguments, Trainer
import datasets
import nvidia_smi

# train_data = datasets.load_dataset('oscar', 'unshuffled_deduplicated_en', split='train', streaming=True)
# eval_data = datasets.load_dataset('oscar', 'unshuffled_deduplicated_en', split='eval', streaming=True)
nvidia_smi.nvmlInit()
count = nvidia_smi.nvmlDeviceGetCount()
print(count)

# training_args = TrainingArguments(
#     output_dir=f'{andromeda.path}/training',
#     overwrite_output_dir=True,
#     do_train=True,
#     log_level='info',
#     logging_dir=f'{andromeda.path}/logs',
#     logging_strategy='steps',
#     num_train_epochs=1,
#     optim='adamw_torch',
#     per_device_train_batch_size=1
# )

# trainer = Trainer(
#     model=andromeda.model,
#     args=training_args,
#     train_dataset=,
#     tokenizer=andromeda.tokenizer
#     )