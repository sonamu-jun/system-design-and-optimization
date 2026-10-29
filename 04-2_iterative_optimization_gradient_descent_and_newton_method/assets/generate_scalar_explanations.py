"""Scalar teaching diagrams; typography is sized for a 440px embedding."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).parent
plt.rcParams.update({'font.size':15,'mathtext.fontset':'stix','svg.fonttype':'path','lines.solid_capstyle':'round'})
BLUE='#2078ba';GRAY='#8b9199';ORANGE='#db7417';GREEN='#198568';PURPLE='#8354b3'
def canvas():
 fig,ax=plt.subplots(figsize=(5.5,3.9),dpi=160);fig.subplots_adjust(left=.10,right=.96,bottom=.17,top=.76)
 ax.set_xticks([]);ax.set_yticks([])
 for sp in ['top','right']:ax.spines[sp].set_visible(False)
 ax.set_xlabel('$x$',loc='right');ax.set_ylabel('$f(x)$',rotation=0,loc='top',labelpad=8)
 return fig,ax
def save(fig,name):fig.savefig(ROOT/(name+'.svg'));fig.savefig(ROOT/(name+'.png'));plt.close(fig)
def legend(fig,approx=True):
 fig.text(.12,.94,'Actual objective: $f(x)$',color=BLUE)
 if approx:fig.text(.12,.85,'Local quadratic: $q_k(x)$',color=GRAY)
for name,quadratic,compare in [('newton_scalar_comparison',False,True),('newton_scalar_constant',True,False),('newton_scalar_local',False,False)]:
 fig,ax=canvas();f=(lambda x:.5*x*x) if quadratic else (lambda x:.5*x*x+.25*x**4)
 start=2.;g=2. if quadratic else 10.;h=1. if quadratic else 13.;end=start-g/h
 z=np.linspace(-.8,2.2,400);ax.plot(z,f(z),color=BLUE,lw=2)
 ax.set(xlim=(-.8,2.4),ylim=(-.15,2.8 if quadratic else 8))
 if not quadratic:
  q=lambda x:f(start)+g*(x-start)+.5*h*(x-start)**2
  t=np.linspace(.4,2.2,200);ax.plot(t,q(t),color=GRAY,ls='--',lw=1.5)
  ax.plot([end,end],[f(end),q(end)],color=GRAY,ls=':',lw=1.3)
  ax.scatter(end,q(end),s=34,facecolor='white',edgecolor=GRAY,zorder=5)
 ax.scatter([start,end],[f(start),f(end)],color=ORANGE,s=32,zorder=6)
 ax.scatter(0,0,color=GREEN,s=28,zorder=5)
 ax.annotate('',xy=(end,f(end)),xytext=(start,f(start)),arrowprops={'arrowstyle':'->','lw':1.7,'color':ORANGE,'shrinkA':5,'shrinkB':5})
 ax.text(start+.10,f(start),'$x_k$',va='center')
 ax.text(-.12,-.05,'$x^*$',color=GREEN,ha='right',va='top')
 if quadratic:ax.text(.45,.55,'Newton',color=ORANGE)
 else:ax.text(.45,2.7,'Newton',color=ORANGE,bbox={'facecolor':'white','edgecolor':'none','pad':1})
 if compare:
  gd=start-.04*g;ax.scatter(gd,f(gd),color=PURPLE,s=32,zorder=6)
  ax.annotate('',xy=(gd,f(gd)),xytext=(start,f(start)),arrowprops={'arrowstyle':'->','lw':1.7,'color':PURPLE,'shrinkA':5,'shrinkB':5})
  ax.text(gd+.12,f(gd)-.1,'GD',color=PURPLE)
 legend(fig,not quadratic);save(fig,name)
fig,ax=canvas();z=np.linspace(-9,3,400);f=lambda x:np.sqrt(1+x*x)
ax.plot(z,f(z),color=BLUE,lw=2);ax.set(xlim=(-9,3),ylim=(.5,9.8))
for end,color,label in [(-8,ORANGE,'Full step'),(-.5,GREEN,'Reduced step')]:
 ax.annotate('',xy=(end,f(end)),xytext=(2,f(2)),arrowprops={'arrowstyle':'->','color':color,'lw':1.7,'shrinkA':5,'shrinkB':5})
 ax.scatter(end,f(end),color=color,s=32,zorder=5)
 ax.text(end+.1 if end == -8 else -4.7, f(end)+.55 if end == -8 else 1.9, label,color=color,bbox={'facecolor':'white','edgecolor':'none','pad':1})
ax.scatter(2,f(2),color=ORANGE,s=32);ax.text(2.1,f(2)-.6,'$x_k$')
legend(fig,False);save(fig,'newton_full_step_limit')
