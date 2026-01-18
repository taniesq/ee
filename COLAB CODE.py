# please note that all of this code was run on Google Colab
# and therefore it must only be run there.

##### BLOC 1 #####

# data loading + preprocessing (put the data in Google Drive and load from there)
# train-test split (80% train, 20% test)

import re
import pandas as pd
from sklearn.model_selection import train_test_split
from google.colab import drive

drive.mount('/content/drive')

corpus_path = "/content/drive/MyDrive/ColabNotebooks/corpus.txt"

with open(corpus_path, "r") as f:
    text = f.read()

df = pd.DataFrame({"text": lines})
train_df, test_df = train_test_split(df, test_size = 0.2, random_state = 64)

##### BLOC 2 #####

# model training (check if the model file already exists)
#   ~5 to 10 epochs
# save the file to Drive directly

from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from datasets import Dataset

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

train_dataset = Dataset.from_pandas(train_df)
test_dataset = Dataset.from_pandas(test_df)

def tokenize_function(examples):
    tokens = tokenizer(examples["text"], truncation = True, padding = "max_length", max_length = 32)
    tokens["labels"] = tokens["input_ids"].copy()
    return tokens

tokenized_train = train_dataset.map(tokenize_function, batched = True)
tokenized_test = test_dataset.map(tokenize_function, batched = True)

data_collator = DataCollatorForLanguageModeling(tokenizer = tokenizer, mlm = False)

training_args = TrainingArguments(
    output_dir = "/content/drive/MyDrive/ColabNotebooks/llm_model",
    overwrite_output_dir = True,
    num_train_epochs = 5,
    per_device_train_batch_size = 16,
    gradient_accumulation_steps = 1,
    save_strategy = "no",
    logging_steps = 50,
    fp16 = True
)

trainer = Trainer(
    model = model,
    args = training_args,
    train_dataset = tokenized_train,
    eval_dataset = tokenized_test,
    data_collator = data_collator
)

trainer.train()
trainer.save_model("/content/drive/MyDrive/ColabNotebooks/llm_model")

##### BLOC 3 #####

# inference & outputting

from transformers import pipeline, AutoTokenizer

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

generator = pipeline(
    "text-generation",
    model = "/content/drive/MyDrive/ColabNotebooks/llm_model",
    tokenizer = tokenizer,
    device = 0
)

num_lines = 100
generated_lines = []

for _ in range(num_lines):
    output = generator(
        " ",
        max_new_tokens = 15,
        do_sample = True,
        top_p = 0.9,
        temperature = 0.8,
        pad_token_id = tokenizer.eos_token_id
    )
    generated_lines.append(output[0]['generated_text'].strip())

generated_lines = list(dict.fromkeys(generated_lines))

output_path = "/content/drive/MyDrive/ColabNotebooks/llm_out.txt"
with open(output_path, "w") as f:
    for line in generated_lines:
        f.write(line + "\n")