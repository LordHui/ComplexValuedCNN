import torch 
from src.complex import CPLX




def concat(axis=-1, *args):

    x_r = torch.cat([j.r for j in args], axis=axis)
    x_i = torch.cat([j.i for j in args], axis=axis)

    return CPLX(x_r, x_i)

def loss(labels, predictions, loss_function, use_magnitude=True):
    if isinstance(labels, CPLX):
        return  loss_function(labels.r, predictions.r) + loss_function(labels.i, predictions.i)
    elif use_magnitude:
        return loss_function(labels, predictions.magnitude())
    

        
