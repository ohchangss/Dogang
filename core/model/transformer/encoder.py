import torch
import math
import torch.nn as nn
import torch.functional as F
import copy

class Encoder(nn.Module):

    def __init__(self, encoder_block, n_layer):  # n_layer: num of encoder blocks 
        super(Encoder, self).__init__()
        self.layers = []
        for i in range(n_layer):
            self.layers.append(copy.deepcopy(encoder_block))


    def forward(self, x):
        out = x
        for layer in self.layers:
            out = layer(out)
        return out
    

class EncoderBlock(nn.Module):

    def __init__(self, self_attention, position_ff):
        super(EncoderBlock, self).__init__()
        self.self_attention = self_attention 
        self.position_ff = position_ff


    def forward(self, x):
        out = x
        out = self.self_attention(out)
        out = self.position_ff(out)
        return out
    
def calculate_attention(query, key, value, mask):
    # n_batch : batch size using in pytorch 
    # seq_len : len of size word embedding 
    # d_k : demmension of key(input word emmbedding size)

    # query, key, value -> (n_batch, seq_len, d_k)
    # mask: (n_batch, seq_len, seq_len)

    d_k = key.shape[-1]
    attention_score = torch.matmul(query, key.transpose(-2, -1)) # Q x K^T, (n_batch, seq_len, seq_len)
    attention_score = attention_score / math.sqrt(d_k)
    if mask is not None:
        attention_score = attention_score.masked_fill(mask==0, -1e9)
    attention_prob = F.softmax(attention_score, dim=-1) # (n_batch, seq_len, seq_len)
    out = torch.matmul(attention_prob, value) # (n_batch, seq_len, d_k)
    return out