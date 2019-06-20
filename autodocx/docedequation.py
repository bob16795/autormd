from io import BytesIO
import string
from pathlib import Path
import random
import os
import matplotlib.pyplot as plt


def renderLatex(formula, fontsize=10, dpi=300, format='svg', file=None, path='./'):
    """Renders LaTeX formula into image or prints to file.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)

    output = BytesIO() if file is None else file
    # with warnings.catch_warnings():
    #    warnings.filterwarnings('ignore', category=MathTextWarning)
    os.chdir(path)
    fig.savefig(output, dpi=dpi, transparent=True, format=format,
                bbox_inches='tight', pad_inches=0.0)

    plt.close(fig)

    return f'{Path(path) / file }'


def add_equation(doc, docdir, equation):
    Docdir = Path(docdir)
    Imgdir = Docdir / "img"
    #name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + ".png"
    name = equation.replace("\\", "").replace(
        " ", "").replace(">", "") + ".png"
    lol = renderLatex(equation, format='png', file=name,
                      path=str(Imgdir)
                      )
    p = doc.add_picture(lol)
    return p
