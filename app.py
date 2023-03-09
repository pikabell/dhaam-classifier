# AUTOGENERATED! DO NOT EDIT! File to edit: ../app.ipynb.

# %% auto 0
__all__ = ['categories', 'image', 'label', 'examples', 'intf', 'classify_image']

# %% ../app.ipynb 1
from fastai.vision.all import *
import gradio as gr

# %% ../app.ipynb 6
learn = load_learner('export.pkl')
categories = ['badrinath', 'gangotri', 'kedarnath', 'yamunotri']
def classify_image(img):
    pred , idx , probs = learn.predict(img)
    return dict(zip(categories , map(float,probs)))

# %% ../app.ipynb 8
image = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['gangotri.jpg','yamunotri.jpg','kedarnath.jpg','badrinath.jpg']

intf = gr.Interface(fn=classify_image,inputs=image,outputs=label,examples=examples)
intf.launch(inline=False)
