"""Original SVG diagrams for the PSO lecture.

References for the vector-sum explanation (redrawn, not copied):
https://liacs.leidenuniv.nl/~nijssensgr/CI/2012/10%20pso.pdf
https://learn.microsoft.com/en-us/archive/msdn-magazine/2011/august/artificial-intelligence-particle-swarm-optimization

Korean terminology: personal/global best positions follow
https://doi.org/10.14801/jkiit.2025.23.11.283
Cognitive/social terms follow the terminology in the SNU thesis:
https://s-space.snu.ac.kr/bitstream/10371/123525/1/000000137089.pdf

Application figures are shared copies of the corresponding 05-2 assets.
Notebook embeddings deliberately use assets/... paths for local preview.
"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
INK, MUTED = '#193449', '#65788a'
BLUE, TEAL, PURPLE, ORANGE = '#326aab', '#168779', '#8968ad', '#d47b32'

def label(x, y, text, color=INK, anchor='start', weight=400):
    return (f'<text x="{x}" y="{y}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{weight}">{escape(text)}</text>')

def path(points, color=MUTED, width=2, arrow=False, dash=False, opacity=1):
    coords=' '.join(('M' if i==0 else 'L')+f'{x},{y}' for i,(x,y) in enumerate(points))
    return (f'<path d="{coords}" stroke="{color}" stroke-width="{width}" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"'
            + (' stroke-dasharray="4 5"' if dash else '')
            + (f' marker-end="url(#{color[1:]})"' if arrow else '') + '/>')

def dot(x, y, color, r=5):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="white" stroke-width="2"/>'

def save(name, height, body):
    colors=[INK,MUTED,BLUE,TEAL,PURPLE,ORANGE]
    defs=''.join(f'<marker id="{c[1:]}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="{c}"/></marker>' for c in colors)
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="{height}" viewBox="0 0 440 {height}" role="img">
<defs>{defs}</defs>
<rect x="1" y="1" width="438" height="{height-2}" rx="16" fill="#fafcfd" stroke="#e1e8ee"/>
<g font-family="Inter, Segoe UI, Arial, sans-serif" font-size="16">{body}</g>
</svg>'''
    (ROOT/f'{name}.svg').write_text(svg)

def generate():
    # Three actual displacement vectors, all drawn from the same origin.
    # Translated dashed copies form the parallelogram for their exact sum.
    current=(64,229)
    inertia=(66,12)
    personal=(35,-104)
    social=(138,-48)
    add=lambda a,b:(a[0]+b[0],a[1]+b[1])
    a,b,c=[add(current,v) for v in (inertia,personal,social)]
    ab=add(a,personal)
    next_position=add(ab,social)
    s=''
    for x in range(44,420,40):s+=path([(x,40),(x,264)],'#edf1f5',1)
    for y in range(44,265,40):s+=path([(30,y),(410,y)],'#edf1f5',1)
    s+=f'<path d="M{current[0]},{current[1]} L{a[0]},{a[1]} L{ab[0]},{ab[1]} L{next_position[0]},{next_position[1]} Z" fill="#eaf1f7" opacity="0.7"/>'
    s+=path([a,ab],BLUE,1.5,False,True,.65)
    s+=path([ab,next_position],TEAL,1.5,False,True,.65)
    s+=path([current,a],PURPLE,2.5,True)
    s+=path([current,b],BLUE,2.5,True)
    s+=path([current,c],TEAL,2.5,True)
    s+=path([current,next_position],INK,3,True)
    s+=dot(*current,ORANGE,6)+dot(*next_position,BLUE,6)
    s+=label(34,213,'Current',ORANGE,weight=500)
    s+=label(130,265,'Inertia term',PURPLE,'middle')
    s+=label(48,108,'Cognitive term',BLUE)
    s+=label(214,185,'Social term',TEAL)
    s+=label(next_position[0]+14,next_position[1]+4,'Next',BLUE,weight=500)
    s+=label(210,65,'Updated velocity',INK,'middle',500)
    s+=path([(210,73),(210,143.5)],MUTED,1)
    s+=path([(28,288),(412,288)],'#e1e8ee',1)
    s+=label(28,315,'Cognitive → pbest',BLUE)
    s+=label(244,315,'Social → gbest',TEAL)
    save('movement',334,s)


if __name__=='__main__':
    generate()
