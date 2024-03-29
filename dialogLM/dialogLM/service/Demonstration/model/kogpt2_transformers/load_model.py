from transformers import GPT2LMHeadModel, GPT2TokenizerFast

def get_kogpt2_model(model_path=None):
    if not model_path:
        model_path = 'taeminlee/kogpt2'
    model = GPT2LMHeadModel.from_pretrained(model_path)
    return model

def get_kogpt2_tokenizer(model_path=None):
    if not model_path:
        model_path = 'taeminlee/kogpt2'
    tokenizer = GPT2TokenizerFast.from_pretrained(model_path)
    return tokenizer

# from transformers import GPT2LMHeadModel, GPT2TokenizerFast

# def get_kogpt2_model(model_path=None):
#     if not model_path:
#         model_path = 'kakaobrain/kogpt'
#     model = GPT2LMHeadModel.from_pretrained(model_path)
#     return model

# def get_kogpt2_tokenizer(model_path=None):
#     if not model_path:
#         model_path = 'kakaobrain/kogpt'
#     tokenizer = GPT2TokenizerFast.from_pretrained(model_path)
#     return tokenizer
