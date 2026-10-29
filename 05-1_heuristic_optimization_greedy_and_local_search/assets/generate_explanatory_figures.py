"""Compact diagrams using the notebooks' fixed costs; positions are schematic."""
from pathlib import Path
from html import escape
ROOT=Path(__file__).parent
BLUE='#2078ba';ORANGE='#db7417';GRAY='#8b9199';GREEN='#198568'
class Diagram:
 def __init__(self,h):
  self.parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="440" height="{h}" viewBox="0 0 440 {h}"><rect width="440" height="{h}" fill="white"/><defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto"><path d="M0 0 L10 5 L0 10" fill="none" stroke="context-stroke"/></marker></defs>']
 def text(self,x,y,s,color='#252b32',anchor='middle'):
  self.parts.append(f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Arial, sans-serif" font-size="16" fill="{color}">{escape(str(s))}</text>')
 def line(self,x,y,X,Y,color=BLUE,dash=False,arrow=False):
  self.parts.append(f'<path d="M{x} {y} L{X} {Y}" fill="none" stroke="{color}" stroke-width="2"'+(' stroke-dasharray="5 4"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>')
 def node(self,x,y,label,color=BLUE):
  self.parts.append(f'<circle cx="{x}" cy="{y}" r="16" fill="white" stroke="{color}" stroke-width="2"/>');self.text(x,y+5,label,color)
 def save(self,name): (ROOT/name).write_text(''.join(self.parts)+'</svg>')
 def route(self,seq,y,costs=None,changed=(),muted=()):
  for i in range(len(seq)-1):
   color=ORANGE if i in changed else GRAY if i in muted else BLUE
   self.line(42+72*i,y,78+72*i,y,color,i in muted,True)
   if costs:self.text(60+72*i,y-11,costs[i],color)
  for i,v in enumerate(seq):self.node(24+72*i,y,v)

# Compare routes using identical schematic city positions and fixed distances.
positions={1:(95,55),0:(315,55),4:(365,155),3:(225,235),2:(80,185)}
distances=[[0,2,9,10,7],[2,0,8,5,6],[9,8,0,4,3],[10,5,4,0,1],[7,6,3,1,0]]

def route_panel(route,labels,filename,missing_return=False):
 p=Diagram(275)
 for (a,b),(lx,ly) in zip(zip(route,route[1:]),labels):
  x,y=positions[a];X,Y=positions[b]
  length=((X-x)**2+(Y-y)**2)**0.5
  ux,uy=(X-x)/length,(Y-y)/length
  color=ORANGE if b==1 else BLUE
  p.line(x+18*ux,y+18*uy,X-20*ux,Y-20*uy,color,arrow=True)
  p.parts.append(f'<rect x="{lx-11}" y="{ly-15}" width="22" height="20" rx="3" fill="white"/>')
  p.text(lx,ly,distances[a][b],color)
 if missing_return:
  p.line(82,165,93,77,GRAY,dash=True)
  p.text(48,127,'누락',GRAY)
 for city,(x,y) in positions.items():p.node(x,y,city)
 p.text(95,23,'출발',BLUE)
 p.save(filename)

route_panel([1,2,0,3,4,1],[(58,123),(175,120),(288,153),(313,216),(224,92)],'longer_route.svg')
route_panel([1,0,4,3,2,1],[(205,43),(357,104),(312,215),(144,229),(59,122)],'feasible_return.svg')
route_panel([1,0,4,3,2],[(205,43),(357,104),(312,215),(144,229)],'incomplete_route.svg',missing_return=True)
p=Diagram(245);p.text(10,22,'Build a tour',BLUE,'start');p.route([1,0,'…'],60);p.text(10,115,'Improve a complete tour',ORANGE,'start');p.route([1,0,4,3,2,1],150);p.route([1,0,4,2,3,1],218,changed=[2,4]);p.line(420,164,420,200,ORANGE,arrow=True);p.save('construction_improvement.svg')
p=Diagram(250);p.text(12,23,'Current city: 1',ORANGE,'start')
for city,cost,y in [(0,2,58),(2,8,115),(3,5,172),(4,6,229)]:
 col=ORANGE if city==0 else GRAY;p.line(75,145,344,y,col,city!=0,True);p.node(365,y,city,col);p.text(210,(145+y)/2-8,cost,col)
p.node(60,145,1,ORANGE);p.text(390,63,'pick',ORANGE,'start');p.save('nearest_choice.svg')
p=Diagram(220);p.text(10,22,'Nearest neighbor: 22',ORANGE,'start');p.route([1,0,4,3,2,1],66,[2,7,1,4,8]);p.text(10,133,'Best of all 24 tours: 20',GREEN,'start');p.route([1,0,2,4,3,1],178,[2,9,3,1,5]);p.save('tour_quality.svg')
# Compare insertion candidates with the same endpoints and display scale.
for city, left_cost, right_cost, filename in [
 (2,8,9,'insertion_city_2.svg'),
 (3,5,10,'insertion_city_3.svg'),
 (4,6,7,'insertion_cost.svg'),
]:
 p=Diagram(225)
 p.line(65,167,375,167,GRAY,True)
 p.text(220,192,'remove: 2',GRAY)
 p.line(65,167,220,55,ORANGE,arrow=True)
 p.line(220,55,375,167,ORANGE,arrow=True)
 p.node(65,167,1);p.node(220,55,city,ORANGE);p.node(375,167,0)
 p.text(122,98,left_cost,ORANGE);p.text(317,98,right_cost,ORANGE)
 p.text(220,218,f'Increase = {left_cost} + {right_cost} − 2 = {left_cost+right_cost-2}',ORANGE)
 p.save(filename)
p=Diagram(255)
for seq,y,cost in [([1,0,1],45,4),([1,4,0,1],103,15),([1,3,4,0,1],161,15),([1,3,4,2,0,1],219,20)]:
 for i,v in enumerate(seq):
  if i:p.line(25+(i-1)*56+14,y,25+i*56-14,y,BLUE,arrow=True)
  p.node(25+i*56,y,v)
 p.text(420,y+5,cost,ORANGE,'end')
p.text(420,18,'Cost',ORANGE,'end');p.save('insertion_growth.svg')
p=Diagram(220);p.text(10,22,'Before: 22',BLUE,'start');p.route([1,0,4,3,2,1],66,[2,7,1,4,8],muted=[2,4]);p.text(10,132,'Reverse (3, 2): 21',ORANGE,'start');p.route([1,0,4,2,3,1],178,[2,7,3,4,5],changed=[2,4]);p.save('two_opt_reversal.svg')
p=Diagram(255);p.text(10,21,'Distance',anchor='start');baseline=212
for value in [0,20,40]:
 y=baseline-4*value;p.line(46,y,419,y,'#dfe3e7');p.text(36,y+5,value,GRAY,'end')
for i,value in enumerate([30,33,21,24,22]):
 x=70+72*i;y=baseline-4*value;p.parts.append(f'<rect x="{x}" y="{y}" width="36" height="{4*value}" fill="#b8c6d0"/>');p.text(x+18,y-6,value);p.text(x+18,236,f'N{i+1}')
p.line(46,132,419,132,ORANGE,True);p.text(419,21,'Current: 20',ORANGE,'end');p.save('neighbor_stopping.svg')
