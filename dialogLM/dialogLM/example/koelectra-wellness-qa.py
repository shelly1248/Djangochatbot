import torch

import sys
sys.path.append('C:\\sqlite\\mysql\\code\\AI\\FINAL_project\\dialogLM\\dialogLM')
from model.kogpt2 import DialogKoGPT2
import random

from transformers import (
  ElectraConfig,
  ElectraTokenizer
)
from model.koelectra import koElectraForSequenceClassification,koelectra_input

def load_wellness_answer():
  root_path = 'C:\\sqlite\\mysql\\code\\AI\\FINAL_project\\dialogLM\\dialogLM'
  category_path = f"{root_path}/NewData/wellness_dialog_category.txt"
  answer_path = f"{root_path}/NewData/wellness_dialog_answer.txt"

  c_f = open(category_path,'r', encoding='utf8')
  a_f = open(answer_path,'r', encoding='utf8')

  category_lines = c_f.readlines()
  answer_lines = a_f.readlines()

  category = {}
  answer = {}
  for line_num, line_data in enumerate(category_lines):
    data = line_data.split('    ')
    category[data[1][:-1]]=data[0]

  for line_num, line_data in enumerate(answer_lines):
    data = line_data.split('    ')
    keys = answer.keys()
    if(data[0] in keys):
      answer[data[0]] += [data[1][:-1]]
    else:
      answer[data[0]] =[data[1][:-1]]

  return category, answer

if __name__ == "__main__":
  root_path='C:\\sqlite\\mysql\\code\\AI\\FINAL_project\\dialogLM\\dialogLM'
  checkpoint_path =f"{root_path}\\checkpoint"
  save_ckpt_path = f"{checkpoint_path}\\koelectra-wellnesee-text-classification2.pth"
  model_name_or_path = "monologg/koelectra-base-discriminator"

  #답변과 카테고리 불러오기
  category, answer = load_wellness_answer()

  ctx = "cuda" if torch.cuda.is_available() else "cpu"
  device = torch.device(ctx)

  # 저장한 Checkpoint 불러오기
  checkpoint = torch.load(save_ckpt_path, map_location=device)

  # Electra Tokenizer
  tokenizer = ElectraTokenizer.from_pretrained(model_name_or_path)

  electra_config = ElectraConfig.from_pretrained(model_name_or_path)
  model = koElectraForSequenceClassification.from_pretrained(pretrained_model_name_or_path=model_name_or_path,
                                                             config=electra_config,
                                                             num_labels=359)
  model.load_state_dict(checkpoint['model_state_dict'])
  model.to(device)
  model.eval()


  while 1:
    sent = input('\nQuestion: ') # '요즘 기분이 우울한 느낌이에요'
    data = koelectra_input(tokenizer,sent, device,512)
    # print(data)

    output = model(**data)

    logit = output[0]
    softmax_logit = torch.softmax(logit, dim=-1)
    softmax_logit = softmax_logit.squeeze()

    max_index = torch.argmax(softmax_logit).item()
    max_index_value = softmax_logit[torch.argmax(softmax_logit)].item()

    answer_list = answer[category[str(max_index)]]
    answer_len = len(answer_list) - 1
    answer_index = random.randint(0, answer_len)
    print(f'Answer: {answer_list[answer_index]}, index: {max_index}, softmax_value: {max_index_value}')
    print('-' * 50)
  # print('argmin:',softmax_logit[torch.argmin(softmax_logit)])