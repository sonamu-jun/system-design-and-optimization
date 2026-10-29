"""Compare a gradient step and a curvature-adjusted step on one landscape."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size':17,'mathtext.fontset':'stix','svg.fonttype':'path','lines.solid_capstyle':'round'})
current=np.array([2.,1.2])
def objective(x,y): return .5*x*x+4*y*y+.02*x**4
gradient=np.array([current[0]+.08*current[0]**3,8*current[1]])
curvature=np.diag([1+.24*current[0]**2,8.])
newton=current-np.linalg.solve(curvature,gradient)
gd=current-.08*gradient
x,y=np.meshgrid(np.linspace(-1.7,3.3,420),np.linspace(-1.6,1.8,350))
dx,dy=x-current[0],y-current[1]
q=objective(*current)+gradient[0]*dx+gradient[1]*dy+.5*(curvature[0,0]*dx*dx+curvature[1,1]*dy*dy)
qmin=objective(*current)-.5*gradient@np.linalg.solve(curvature,gradient)
fig,ax=plt.subplots(figsize=(5.5,3.8),dpi=180)
fig.subplots_adjust(left=.08,right=.97,bottom=.16,top=.80)
blue,gray,orange,purple,green='#1680ff','#8a8d96','#e77715','#8354b3','#15956c'
ax.contour(x,y,objective(x,y),levels=[.7,3.2,objective(*current)],colors=blue,linewidths=1.25,alpha=.7)
ax.contour(x,y,q,levels=[qmin+.7,objective(*current)],colors=gray,linewidths=1.2,linestyles='dashed')
for point,color in [(gd,purple),(newton,orange)]:
 ax.annotate('',xy=point,xytext=current,arrowprops={'arrowstyle':'->','lw':2,'color':color,'shrinkA':5,'shrinkB':5})
 ax.scatter(*point,s=35,color=color,zorder=5)
ax.scatter(*current,s=42,color=orange,zorder=6)
ax.scatter(0,0,s=35,color=green,zorder=6)
ax.text(2.12,1.29,r'$\mathbf{x}_k$',ha='left')
ax.text(gd[0]+.18,gd[1]+.08,'GD',color=purple,ha='left')
ax.text(newton[0]+.08,newton[1]-.36,'Newton',color=orange,ha='left',bbox={'facecolor':'white','edgecolor':'none','pad':1})
ax.text(-.18,-.33,r'$\mathbf{x}^*$',color=green,ha='right')
ax.set(xlim=(-1.4,3.05),ylim=(-1.45,1.6))
ax.set_aspect('equal',adjustable='box')
ax.set_xticks([]);ax.set_yticks([])
for spine in ax.spines.values():spine.set_visible(False)
for start,end in [((-1.32,-1.32),(2.96,-1.32)),((-1.32,-1.32),(-1.32,1.47))]:
 ax.annotate('',xy=end,xytext=start,arrowprops={'arrowstyle':'->','lw':1,'color':'#444'})
ax.text(2.94,-1.42,r'$x_1$',ha='center',va='top')
ax.text(-1.43,1.48,r'$x_2$',ha='right',va='center')
fig.text(.16,.94,r'Objective: $f(\mathbf{x})$',color=blue,ha='left',fontsize=15)
fig.text(.16,.86,r'Quadratic approximation: $q_k(\mathbf{x})$',color=gray,ha='left',fontsize=15)
fig.lines.extend([plt.Line2D([.08,.13],[.952,.952],transform=fig.transFigure,color=blue,lw=1.5),plt.Line2D([.08,.13],[.872,.872],transform=fig.transFigure,color=gray,lw=1.5,ls='--')])
path=Path(__file__).with_name('newton_comparison_landscape.svg')
fig.savefig(path);fig.savefig(path.with_suffix('.png'));plt.close(fig)
