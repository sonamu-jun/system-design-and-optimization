"""Generate compact PSO method flowcharts."""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent
INK, BLUE, TEAL, GRAY = '#193449', '#326aab', '#168779', '#7e93a2'

def text(x, y, value, color=INK):
    return f'<text x="{x}" y="{y}" text-anchor="middle" fill="{color}">{escape(value)}</text>'

def box(y, lines, fill='#ffffff', color=BLUE, x=74, width=292, height=52):
    content=f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="10" fill="{fill}" stroke="{color}" stroke-opacity=".35"/>'
    start=y+height/2-(len(lines)-1)*10+5
    return content+''.join(text(x+width/2,start+i*20,line) for i,line in enumerate(lines))

def arrow(points, color=GRAY):
    d=' '.join(('M' if i==0 else 'L')+f'{x},{y}' for i,(x,y) in enumerate(points))
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="1.6" stroke-linejoin="round" marker-end="url(#arrow)"/>'

def diamond(y, label):
    return f'<path d="M220,{y} L320,{y+31} L220,{y+62} L120,{y+31} Z" fill="#edf6f3" stroke="#8ebdb3"/>'+text(220,y+37,label)

def save(name,height,body):
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="440" height="{height}" viewBox="0 0 440 {height}">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 1 L9 5 L1 9 Z" fill="{GRAY}"/></marker></defs>
<rect x="1" y="1" width="438" height="{height-2}" rx="16" fill="#fafcfd" stroke="#e1e8ee"/>
<g font-family="Noto Sans CJK KR, Malgun Gothic, sans-serif" font-size="16">{body}</g></svg>'''
    (ROOT/f'{name}.svg').write_text(svg)

def loop(name,evaluation,result):
    initial = '위치 및 속도 난수 설정' if name == 'pso_method_flow' else '위치 평가·속도 난수 설정'
    s=box(16,[initial,'pbest 및 gbest 설정' if name == 'pso_method_flow' else 'pbest·gbest 설정'],fill='#eef4fa')
    s+=arrow([(220,68),(220,88)])
    movement=['속도·위치 갱신, 경계 처리'] if name=='pso_method_flow' else ['입자 이동·범위 처리']
    s+=box(88,movement)
    s+=arrow([(220,140),(220,160)])
    s+=box(160,evaluation)
    s+=arrow([(220,212),(220,232)])
    updates=['개인 최적 위치 pbest 갱신','전역 최적 위치 gbest 갱신'] if name=='pso_method_flow' else ['더 좋은 pbest 갱신','모든 pbest에서 gbest 선택']
    s+=box(232,updates)
    s+=arrow([(220,284),(220,305)])
    stop='종료 조건 충족?' if name=='pso_method_flow' else '횟수 한도 도달?'
    s+=diamond(305,stop)
    s+=arrow([(120,336),(38,336),(38,114),(74,114)])
    s+=text(75,325,'아니요',GRAY)
    s+=arrow([(220,367),(220,401)])+text(242,391,'예',TEAL)
    s+=box(401,result,fill='#eaf5f0',color=TEAL)
    save(name,472,s)

def economics():
    s=box(16,['허용 후보 평가·속도 난수 설정','pbest·gbest 설정'],fill='#eef4fa')
    s+=arrow([(220,68),(220,86)])
    s+=box(86,['입자 이동·범위 처리','0·1 선택으로 변환'])
    s+=arrow([(220,138),(220,158)])
    s+=diamond(158,'비용 ≤ 예산 7?')
    s+=arrow([(120,189),(102,189),(102,249)])+text(81,220,'아니요',GRAY)
    s+=arrow([(320,189),(338,189),(338,249)])+text(356,220,'예',TEAL)
    s+=box(249,['평가값 ∞','최선 기록 제외'],fill='#f1f3f5',color=GRAY,x=24,width=156)
    s+=box(249,['순편익의 음수','작을수록 좋음'],fill='#eaf5f0',color=TEAL,x=260,width=156)
    s+=arrow([(102,301),(102,323),(220,323),(220,343)])
    s+=arrow([(338,301),(338,323),(220,323)])
    s+=box(343,['더 좋은 허용 후보만 갱신','모든 pbest에서 gbest 선택'])
    s+=arrow([(220,395),(220,413)])
    s+=diamond(413,'횟수 한도 도달?')
    s+=arrow([(120,444),(10,444),(10,112),(74,112)])
    s+=text(74,433,'아니요',GRAY)
    s+=arrow([(220,475),(220,507)])+text(242,497,'예',TEAL)
    s+=box(507,['gbest를 사업 선택으로 변환','비용·순편익 반환'],fill='#eaf5f0',color=TEAL)
    save('economics_flow',578,s)

def generate():
    loop('pso_method_flow',['목적함수값 계산'],['전역 최적 위치 gbest와','목적함수값 반환'])
    loop('biology_flow',['0·1·2 단계로 변환','표에서 생장량 조회 → 음수'],['gbest를 단계로 변환','조명·양액과 생장량 반환'])
    economics()
    loop('assignment_flow',['0·1 배정으로 변환','두 컴퓨터의 부하 중 큰 값'],['gbest를 컴퓨터 배정으로 변환','배정·부하·완료 시간 반환'])

if __name__=='__main__':
    generate()
