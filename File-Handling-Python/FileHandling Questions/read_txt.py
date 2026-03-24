with open("data.txt", "r") as f:
    print("read()  :  ", f.read())
"""read()  :   The rain arrived quietly, like a secret slipping through the cracks of a busy afternoon.
People hurried under awnings, clutching their belongings as if the sky had suddenly turned unpredictableâ€”which, in truth, it had.
Somewhere in the distance, a dog barked in protest while a lone bicycle leaned against a rusted gate, slowly gathering droplets along its frame.        
The scent of wet earth rose into the air, grounding everything in a strange calm, as if the world had paused just long enough to breathe."""

with open("data.txt", "r") as f:
    print("readline()  :  ", f.readline())
    """readline()  :   The rain arrived quietly, like a secret slipping through the cracks of a busy afternoon."""


with open("data.txt", "r") as f:
    print("readlines()  :  ", f.readlines())
    """readlines()  :   ['The rain arrived quietly, like a secret slipping through the cracks of a busy afternoon.  \n', 'People hurried under awnings, clutching their belongings as if the sky had suddenly turned unpredictableâ€”which, in truth, it had.  \n', 'Somewhere in the distance, a dog barked in protest while a lone bicycle leaned against a rusted gate, slowly gathering droplets along its frame.  \n', 'The scent of wet earth rose into the air, grounding everything in a strange calm, as if the world had paused just long enough to breathe.']"""
