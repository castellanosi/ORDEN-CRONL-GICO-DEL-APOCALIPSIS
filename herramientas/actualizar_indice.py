"""Regenera navegación y tarjetas después de editar estudios.json (Python 3)."""
from pathlib import Path
import json,re,html
root=Path(__file__).resolve().parents[1]
data=json.loads((root/'estudios.json').read_text(encoding='utf-8'))
for item in data:
    if not (root/item['archivo']).is_file(): raise SystemExit('Falta el archivo: '+item['archivo'])
def esc(s): return html.escape(s,quote=True)
for page in root.glob('*.html'):
    source=page.read_text(encoding='utf-8')
    nav='<a class="study-link" href="index.html">⌂ &nbsp; Todos los estudios</a>'
    for i,x in enumerate(data):
        current=x['archivo']==page.name
        nav+=f'<a class="study-link {"selected" if current else ""}" href="{esc(x["archivo"])}" {"aria-current=page" if current else ""}><span class="dot d{i%2}"></span>{esc(x["titulo"])}<span class="arrow">↗</span></a>'
    source=re.sub(r'(<nav aria-label="Estudios">).*?(</nav>)',lambda m:m[1]+nav+m[2],source,flags=re.S)
    if page.name=='index.html':
        cards=''
        for i,x in enumerate(data):
            cards+=f'<a class="card card-{i%2}" href="{esc(x["archivo"])}"><div class="card-top"><span>ESTUDIO {i+1:02}</span><span>↗</span></div><div class="card-symbol">✧</div><div class="eyebrow">{esc(x["etiqueta"])}</div><h2>{esc(x["titulo"])}</h2><p>{esc(x["descripcion"])}</p><div class="card-bottom">Comenzar lectura <span>→</span></div></a>'
        source=re.sub(r'(<div class="cards">).*?(</div><div class="home-note">)',lambda m:m[1]+cards+m[2],source,flags=re.S)
        source=re.sub(r'\d+ disponibles',str(len(data))+' disponibles',source)
    else:
        match=re.search(r'(<article class="article">)(.*?)(</article>)',source,re.S)
        if match:
            entries=[];counter=[0]
            def heading(m):
                tag,attrs,label=m.groups(); ident='section-'+str(counter[0]);counter[0]+=1
                attrs=re.sub(r'\s+id="[^"]*"','',attrs)
                entries.append(f'<li class="{tag}"><a href="#{ident}">{re.sub("<[^>]+>","",label)}</a></li>')
                return f'<{tag}{attrs} id="{ident}">{label}</{tag}>'
            article=re.sub(r'<(h[23])([^>]*)>(.*?)</h[23]>',heading,match[2],flags=re.S)
            source=source[:match.start(2)]+article+source[match.end(2):]
            source=re.sub(r'(<ol class="toc">).*?(</ol>)',lambda m:m[1]+''.join(entries)+m[2],source,flags=re.S)
    page.write_text(source,encoding='utf-8')
print('Índice actualizado en todas las páginas.')
