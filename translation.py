from transformers import MBartForConditionalGeneration, MBart50Tokenizer

model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-one-to-many-mmt")
tokenizer = MBart50Tokenizer.from_pretrained("facebook/mbart-large-50-one-to-many-mmt",src_lang="en_XX")


article_en = "How are You?"

model_inputs = tokenizer(article_en,return_tensors="pt")

generated_tokens = model.generate(**model_inputs,forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"])


translation = tokenizer.batch_decode(generated_tokens,skip_special_tokens=True)

print(translation)