from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


class Answerer:
    def __init__(self, model="microsoft/DialoGPT-large"): #my model by default
        self.tokenizer, self.model = self.load_tokenizer_and_model(model=model)
        self.chat_round = 0
        self.chat_history_ids = None # response of our model is a chat_history_ids

    @staticmethod
    def load_tokenizer_and_model(model):
        """
          Load tokenizer and model instance for some specific DialoGPT model.
        """
        # Initialize tokenizer and model
        print("Loading model...")
        tokenizer = AutoTokenizer.from_pretrained(model)
        model = AutoModelForCausalLM.from_pretrained(model)

        # Return tokenizer and model
        return tokenizer, model

    def reset_dialog(self):
        self.chat_round = 0
        self.chat_history_ids = None

    def generate_response(self, new_mes):
        """
          Generate a response to some user input.
        """
        # Encode user input and End-of-String (EOS) token
        new_input_ids = self.tokenizer.encode(new_mes + self.tokenizer.eos_token, return_tensors='pt')

        # Append tokens to chat history
        bot_input_ids = torch.cat([self.chat_history_ids, new_input_ids], dim=-1) if self.chat_round > 0 else new_input_ids

        # Generate response given maximum chat length history of 1250 tokens
        chat_history_ids = self.model.generate(bot_input_ids, max_length=1250, pad_token_id=self.tokenizer.eos_token_id)

        # Print response
        # print("DialoGPT: {}".format(
        #     self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
        # print(self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0]))
        org_string = self.tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0])
        size = len(org_string)
        # Slice string to remove last 3 characters from string
        mod_string = org_string[:size - 13]
        # print(mod_string)
        self.chat_round += 1
        self.chat_history_ids = chat_history_ids
        # Return the chat history ids
        return mod_string


if __name__ == '__main__':
    answerer = Answerer()
    response = answerer.generate_response('Hi, I\'m Elfo')
    print(response)
    #response = answerer.generate_response('what to do?')
    #print(response)
   # response = answerer.generate_response('I\'m scared')
    #print(response)
    #response = answerer.generate_response('do you like the weather?')
    #print(response)
    #answerer.reset_dialog()
    #response = answerer.generate_response('Hi, I\'m Elfo')
    #print(response)
        #print(chat_for_n_rounds(1))
